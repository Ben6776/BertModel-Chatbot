from fastapi import FastAPI
from pydantic import BaseModel
from bertmodel import answer_question, context  # Make sure this matches where you've defined your function

# FastAPI app instance
app = FastAPI()

# Create a model for the incoming question
class QuestionRequest(BaseModel):
    question: str

# Define a route for asking questions
@app.post("/ask")
async def ask_question(req: QuestionRequest):
    answer = answer_question(req.question, context)
    return {"answer": answer}

# Route for Swagger UI (FastAPI provides this automatically)
@app.get("/")
async def root():
    return {"message": "Chatbot is ready! Go to /docs to interact with it."}
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use ["http://localhost:8080"] for specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
