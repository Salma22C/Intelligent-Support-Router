
# 🏢 Intelligent Support Router & Triage

An end-to-end NLP application that automatically classifies incoming customer support tickets using a fine-tuned **BERT** model built with **TensorFlow** and **Hugging Face Transformers**.

The system routes customer tickets into predefined categories, generates an initial draft response, and deploys the solution through a Flask web application.

---

## 🚀 Project Overview

Customer support teams receive hundreds of emails and tickets every day. Manually reviewing and routing each request is time-consuming and prone to human error.

This project automates the process by:

- 📩 Understanding customer support messages
- 🤖 Classifying tickets using a fine-tuned BERT model
- 💬 Generating an initial response
- 🌐 Deploying the application with Flask and ngrok

---
## 📂 Repository Structure

├── Tests/
│   ├── Colab Notebook
│   ├── Presentation
│   ├── Architecture Diagram
│   └── Demo 
├── README.md
└── requirements.txt
---
## 🎯 Features

- Customer Ticket Classification
- Fine-Tuned BERT Model
- TensorFlow Implementation
- Hugging Face Transformers
- Automated Response Generation
- Flask Web Application
- Public Deployment via ngrok
- Classification Report
- Confusion Matrix
- Stress Testing

---

## 🧠 Ticket Categories

| Label | Description |
|-------|-------------|
| 🔴 Urgent Complaint | Critical customer issues requiring immediate attention |
| 🟢 Feature Suggestion | Requests for new functionality or improvements |
| 🔵 General Inquiry | Questions about products, pricing, documentation, or services |

---

## 🏗️ System Architecture

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
Rule-Based Response Generator
        │
        ▼
Display Results
        │
        ▼
Public Demo (ngrok)
````

---

## 🤗 Hugging Face Workflow

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

## 📊 Dataset Evolution

### Initial Dataset

| Category           | Samples |
| ------------------ | ------: |
| Urgent Complaint   |       6 |
| Feature Suggestion |       6 |
| General Inquiry    |       6 |

**Total:** 18 samples

### Observation

The dataset was balanced but too small for effective BERT fine-tuning. The classifier frequently predicted **General Inquiry**.

---

### Expanded Dataset

| Category           | Samples |
| ------------------ | ------: |
| Urgent Complaint   |      30 |
| Feature Suggestion |      30 |
| General Inquiry    |      30 |

**Total:** 90 samples

### Result

Increasing the dataset improved the model's ability to distinguish between the three ticket categories during manual stress testing.

---

## ⚙️ Tech Stack

### Programming

* Python

### Deep Learning

* TensorFlow

### NLP

* Hugging Face Transformers
* BERT (Encoder-only Transformer)

### Machine Learning

* Scikit-learn

### Data Processing

* Pandas
* NumPy

### Deployment

* Flask
* ngrok

---

## 📈 Model Evaluation

The model was evaluated using:

* Classification Report
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🌐 Web Application

The application workflow:

1. User enters a customer support ticket.
2. The ticket is tokenized using Hugging Face.
3. BERT predicts the ticket category.
4. The application generates an appropriate draft response.
5. Results are displayed through the Flask interface.

---

## 🧪 Stress Testing

After expanding the dataset, multiple customer support scenarios were tested.

The system successfully classified:

* ✅ Urgent Complaint
* ✅ Feature Suggestion
* ✅ General Inquiry

and generated category-specific responses.

---

## ⚠️ Engineering Challenges

During development, several real-world engineering issues were resolved:

* TensorFlow dependency conflicts
* Transformers version incompatibility
* ngrok authentication
* Flask routing issues
* Secure secret management using Google Colab Secrets
* Dataset size limitations

---

## 📚 Key Learnings

* Fine-tuning pretrained Transformer models
* Hugging Face Transformers workflow
* TensorFlow model training
* Transfer learning
* Flask deployment
* ngrok tunneling
* Dependency management
* End-to-end NLP application development

---


## 📸 Demo

> Add screenshots of:
>
> * Feature Suggestion prediction
> * Urgent Complaint prediction
> * General Inquiry prediction

---

## 👩‍💻 Author

**Salma Mohamed**

Advanced AI Diploma Capstone Project

TensorFlow • Hugging Face Transformers • BERT • NLP • Flask

```
```
