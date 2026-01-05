from fastapi import FastAPI
from pydantic import BaseModel
from model import MarkovTextGenerator

app = FastAPI(title="ZENVY Local GenAI Payroll Copilot")

# Train model on startup
generator = MarkovTextGenerator()
with open("payroll_corpus.txt", encoding="utf-8") as f:
    generator.train(f.read())

class Query(BaseModel):
    role: str
    question: str

def is_payroll_question(q: str) -> bool:
    keywords = ["pf", "salary", "payroll", "tds", "tax", "pt", "hra"]
    return any(k in q.lower() for k in keywords)

@app.post("/ask")
def ask(query: Query):
    if not is_payroll_question(query.question):
        return {
            "answer": "Information not available in payroll policy."
        }

    seed_word = query.question.lower().split()[0]
    answer = generator.generate(seed_word)

    return {
        "role": query.role,
        "question": query.question,
        "answer": answer.capitalize() + "."
    }

@app.get("/")
def home():
    return {"status": "Local GenAI Payroll Copilot running"}
