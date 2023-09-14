from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.FibbonacciGenerator import generate_fibonacci_sequence

app = FastAPI()


class FibRequestModel(BaseModel):
    elementos: int


@app.get("/api/health")
def health():
    return "Estou saudavel"


@app.post("/api/fibonacci")
def fibonacci_route(request_data: FibRequestModel):
    elementos = request_data.elementos
    if elementos < 0:
        raise HTTPException(status_code=400, detail="elementos não pode ser negativos")

    return generate_fibonacci_sequence(elementos)
