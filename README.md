# 🏢 Intelligent Support Router & Triage

An end-to-end NLP application that automatically classifies incoming customer support tickets using a fine-tuned **BERT** model built with **TensorFlow** and **Hugging Face Transformers**.

The system routes customer tickets into predefined categories, generates an initial AI draft response using a generative language model, and deploys the solution through a Flask web application.

---

# 🚀 Project Overview

Customer support teams receive hundreds of emails and tickets every day. Manually reviewing and routing each request is time-consuming and prone to human error.

This project automates the process by:

- 📩 Understanding customer support messages
- 🤖 Classifying tickets using a fine-tuned BERT model
- 💬 Generating an initial AI draft response
- 🌐 Deploying the application through Flask with temporary public access using ngrok

---

# ⚡ Installation

## Clone the repository

```bash
git clone https://github.com/Salma22C/Intelligent-Support-Router.git
```

## Navigate to the project folder

```bash
cd Intelligent-Support-Router
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Launch Jupyter Notebook

# For training and experimentation
```jupyter notebook```

# For running the deployed application
```python app.py```
Open the project notebook and run all cells sequentially.

> **Note:** The Flask application is demonstrated using Google Colab together with ngrok. The generated ngrok URL is temporary and remains active only while the Colab runtime is running.

---

# 📂 Repository Structure

```text
.
├── Tests/
│   ├── Colab Notebook
│   ├── Presentation
│   ├── Architecture Diagram
│   └── Demo
├── README.md
└── requirements.txt
```

---

# 🎯 Features

- Customer Ticket Classification
- Fine-Tuned BERT Model
- TensorFlow Implementation
- Hugging Face Transformers
- AI Draft Response Generation
- Flask Web Application
- Temporary Public Access via ngrok
- Classification Report
- Confusion Matrix
- Manual Stress Testing

---

# 🧠 Ticket Categories

| Label | Description |
|-------|-------------|
| 🔴 Urgent Complaint | Critical customer issues requiring immediate attention |
| 🟢 Feature Suggestion | Requests for new functionality or improvements |
| 🔵 General Inquiry | Questions about products, pricing, documentation, or services |

---

# 🏗️ System Architecture

```text
Customer Ticket / Email
        │
        ▼
Flask Web Interface
        │
        ▼
AutoTokenizer
(Hugging Face)
        │
        ▼
Fine-Tuned BERT Encoder
(TensorFlow)
        │
        ▼
Classification Head
        │
        ▼
Predicted Category
        │
        ▼
Generative LLM Response Drafting
        │
        ▼
Display Results
        │
        ▼
Temporary Public Access (ngrok)
```

---

# 🤗 Hugging Face Workflow

```text
Install Transformers
        │
        ▼
Import AutoTokenizer
        │
        ▼
Import TFAutoModelForSequenceClassification
        │
        ▼
Download Pretrained BERT
        │
        ▼
Tokenize Customer Tickets
        │
        ▼
Fine-Tune on Custom Dataset
        │
        ▼
Evaluate Performance
        │
        ▼
Deploy with Flask
```

---

# 📊 Dataset Evolution

## Initial Dataset

| Category | Samples |
|----------|---------:|
| Urgent Complaint | 6 |
| Feature Suggestion | 6 |
| General Inquiry | 6 |

**Total:** **18 samples**

### Observation

The dataset was balanced but too small for effective BERT fine-tuning. The classifier frequently predicted the **General Inquiry** category.

---

## Expanded Dataset

| Category | Samples |
|----------|---------:|
| Urgent Complaint | 30 |
| Feature Suggestion | 30 |
| General Inquiry | 30 |

**Total:** **90 samples**

### Result

Expanding the balanced dataset improved the model's ability to distinguish between the three ticket categories during manual stress testing.

---

# ⚙️ Tech Stack

## Programming

- Python

## Deep Learning

- TensorFlow

## NLP

- Hugging Face Transformers
- BERT (Encoder-only Transformer)

## Machine Learning

- Scikit-learn

## Data Processing

- Pandas
- NumPy

## Deployment

- Flask
- ngrok

---

# 📈 Model Evaluation

The model was evaluated using:

- Classification Report
- Precision
- Recall
- F1-score
- Confusion Matrix

The evaluation was performed on the available labeled dataset, followed by manual stress testing using representative customer support scenarios.

---

# 🌐 Web Application

Application workflow:

1. User submits a customer support ticket.
2. Hugging Face AutoTokenizer tokenizes the input.
3. The fine-tuned BERT model predicts the ticket category.
4. A generative language model creates an initial draft response based on the predicted category.
5. The predicted category and generated response are displayed through the Flask interface.

---

# 🧪 Stress Testing

After expanding the dataset from **18** to **90** balanced samples, multiple representative customer support scenarios were manually tested.

The application successfully classified:

- ✅ Urgent Complaint
- ✅ Feature Suggestion
- ✅ General Inquiry

and generated category-specific AI draft responses through the Flask interface.

---

# ⚠️ Engineering Challenges

During development, several real-world engineering challenges were encountered and resolved:

- TensorFlow dependency conflicts
- Hugging Face Transformers version compatibility
- ngrok authentication and deployment
- Flask routing configuration
- Secure secret management using Google Colab Secrets
- Dataset expansion and refinement for improved model performance

---

# 📚 Key Learnings

- Fine-tuning pretrained BERT models with TensorFlow
- Building NLP pipelines using Hugging Face Transformers
- Applying transfer learning for text classification
- Integrating a generative language model for response drafting
- Deploying AI applications with Flask
- Securely exposing local applications using ngrok
- Managing Python package dependencies
- Designing an end-to-end NLP system from training to deployment

---

# 📸 Demo

The **Tests/** directory contains:

- Colab Notebook
- Presentation
- Architecture Diagram
- Demo assets

Example demonstrations include:

- ✅ Urgent Complaint prediction
- ✅ Feature Suggestion prediction
- ✅ General Inquiry prediction

---

# 👩‍💻 Author

**Salma Mohamed**

Advanced AI Diploma Capstone Project

**Technologies:** TensorFlow • Hugging Face Transformers • BERT • Flask • NLP
