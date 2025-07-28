from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import google.generativeai as genai
from schema import db_schema  # ✅ Ensure schema.py exists with db_schema variable

# ✅ Configure Google Gemini API with your API key
genai.configure(api_key="AIzaSyAySapw7eA-rQU4Q2j4gJngJRI45RiCslQ")  # Replace with your actual key if needed

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load schema text
SCHEMA_TEXT = db_schema.strip()

# ✅ Request model for user input
class QuestionInput(BaseModel):
    question: str

# ✅ Response model for SQL output
class SQLResponse(BaseModel):
    sql_query: str

# ✅ SQL generator function using Gemini
def generate_sql_from_question(question: str) -> str:
    prompt = f"""
You are a helpful SQL assistant. Based on the database schema below, generate a valid SQL query that answers the user question.

Schema:
{SCHEMA_TEXT}

Question:
{question}

Respond ONLY with the SQL query (no explanations, no markdown).
"""
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini Error: {e}")

# ✅ POST endpoint: SQL query generation
@app.post("/generate-sql/", response_model=SQLResponse)
def generate_sql_endpoint(payload: QuestionInput):
    sql = generate_sql_from_question(payload.question)
    return {"sql_query": sql}

# ✅ GET endpoint: general LLM prompt or joke
@app.get("/llm/")
def generate_sql_from_question_joke(prompt: str = "Tell me a joke about SQL databases."):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return {"response": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini Error: {e}")

# ✅ Root route to avoid 404 on "/"
@app.get("/")
def root():
    return {"message": "Welcome to the Gemini SQL Assistant API! Visit /docs to test endpoints."}

# ✅ Run FastAPI with uvicorn when executing app.py directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
