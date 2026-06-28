import os
import tensorflow as tf
from flask import Flask, request, render_template_string
from transformers import (
    AutoTokenizer,
    TFAutoModelForSequenceClassification,
    pipeline,
)

# ==========================================================
# Flask Application
# ==========================================================

app = Flask(__name__)

# ==========================================================
# Load Fine-Tuned BERT Model
# ==========================================================

MODEL_PATH = os.path.abspath("./saved_tf_bert_model")

if os.path.exists(MODEL_PATH) and any(os.scandir(MODEL_PATH)):
    print(f"Loading fine-tuned model from: {MODEL_PATH}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = TFAutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
else:
    raise FileNotFoundError(
        "Fine-tuned model not found. Please train the model first."
    )

# ==========================================================
# Load Generative Model
# ==========================================================

generation_pipeline = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    device_map="auto"
)

# ==========================================================
# HTML Template
# ==========================================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Intelligent Support Router & Triage</title>

<style>
body{
font-family:Arial;
background:#f4f6f9;
padding:40px;
}

.container{
background:white;
max-width:700px;
margin:auto;
padding:30px;
border-radius:10px;
box-shadow:0 0 15px rgba(0,0,0,.1);
}

textarea{
width:100%;
height:120px;
padding:10px;
}

button{
margin-top:10px;
padding:10px 20px;
background:#007bff;
color:white;
border:none;
cursor:pointer;
}

.result{
margin-top:20px;
padding:15px;
background:#efefef;
}
</style>

</head>

<body>

<div class="container">

<h2>🏢 Intelligent Support Router & Triage</h2>

<form method="POST" action="/process">

<textarea
name="email_text"
placeholder="Paste customer support ticket..."
required>
</textarea>

<br>

<button type="submit">
Route & Process Ticket
</button>

</form>

{% if intent %}

<div class="result">

<h3>Predicted Category</h3>

<p>{{ intent }}</p>

<h3>Generated Draft Response</h3>

<p>{{ response }}</p>

</div>

{% endif %}

</div>

</body>
</html>
"""

# ==========================================================
# Home Page
# ==========================================================

@app.route("/", methods=["GET"])
def home():

    return render_template_string(HTML_TEMPLATE)

# ==========================================================
# Prediction Endpoint
# ==========================================================

@app.route("/process", methods=["POST"])
def process():

    user_text = request.form["email_text"]

    inputs = tokenizer(
        user_text,
        return_tensors="tf",
        truncation=True,
        padding=True,
        max_length=64
    )

    outputs = model(inputs)

    prediction = tf.argmax(outputs.logits, axis=-1).numpy()[0]

    labels = {
        0: "Urgent Complaint",
        1: "Feature Suggestion",
        2: "General Inquiry"
    }

    category = labels[prediction]

    prompts = {
        0: "You are an urgent customer support assistant. Draft a short escalation note.",
        1: "You are a product manager. Summarize the feature request.",
        2: "You are a professional customer support agent. Draft a polite response."
    }

    messages = [
        {
            "role": "system",
            "content": prompts[prediction]
        },
        {
            "role": "user",
            "content": user_text
        }
    ]

    prompt = generation_pipeline.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    result = generation_pipeline(
        prompt,
        max_new_tokens=120,
        temperature=0.4,
        do_sample=True,
    )

    response = result[0]["generated_text"].split(
        "<|im_start|>assistant\n"
    )[-1].strip()

    return render_template_string(
        HTML_TEMPLATE,
        intent=category,
        response=response,
    )

# ==========================================================
# Run Flask
# ==========================================================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
