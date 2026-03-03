from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI DeFi Agent Backend Running"}

@app.get("/analyze")
def analyze():
    return {
        "signal": "BUY",
        "confidence": 0.75,
        "reasoning": "Mock EMA crossover detected",
        "risk_score": 0.32
    }