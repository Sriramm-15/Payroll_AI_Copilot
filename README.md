# 🧠 ZENVY – Local GenAI Payroll Copilot (API‑Free)

A **fully local, free, and explainable Generative AI Payroll Copilot** built without using any paid or external AI APIs.  
ZENVY demonstrates **real GenAI fundamentals** by training a probabilistic language model on payroll policy data and generating responses safely.

---

## 📌 Problem Statement

Most modern payroll assistants rely on cloud‑based LLM APIs, which introduce:

- Cost overhead  
- Privacy and compliance concerns  
- Vendor lock‑in  
- Hallucination and over‑generalization risks  

**ZENVY** solves this by providing a **local GenAI system** that:

- Trains on payroll policy text  
- Generates context‑aware answers  
- Enforces safety and domain restrictions  
- Works completely offline  

---

## 🎯 Objectives

- Build a **context‑aware payroll assistant**  
- Use **Generative AI trained on data**, not APIs  
- Prevent hallucinations with strict domain constraints  
- Ensure privacy, control, and explainability  
- Keep the solution **free, offline, and reproducible**  

---

## 🧠 Generative AI Approach

ZENVY uses a **probabilistic language model (Markov‑based text generator)** over payroll policy text.

### Why this is GenAI

- The model is **trained** on payroll policy data  
- It **learns word transition probabilities**  
- It **generates unseen text**, not predefined answers  
- Generation is **non‑deterministic**, so outputs can vary across runs  

This showcases **core Generative AI principles** without relying on large cloud LLMs.

---

## 🏗️ Architecture

```text
Client (Swagger UI / API Client)
          |
          v
    FastAPI Application
          |
          v
 Local GenAI Model (Markov Text Generator)
          |
          v
 Payroll Policy Corpus (Training Data)

```

## 📁 Project Structure
```
Payroll_AI_Agent/
├── app.py              # FastAPI application
├── model.py            # Local Generative AI model (Markov generator)
├── payroll_corpus.txt  # Training data (payroll policies)
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```
⚙️ Tech Stack​
Language: Python 3.14​

Backend: FastAPI (ASGI)​

Server: Uvicorn​

Model: Custom probabilistic NLP (no external ML libraries)​

APIs: No paid APIs, no external AI services​

