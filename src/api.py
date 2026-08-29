from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Terra Data Platform API")

@app.get("/")
def root():
    return {"message": "Terra Data Platform API"}

@app.get("/loads")
def get_loads():
    df = pd.read_csv("processed_loads.csv")
    return df.to_dict(orient="records")

@app.get("/summary")
def get_summary():
    df = pd.read_csv("processed_loads.csv")

    return {
        "total_loads": len(df),
        "total_revenue": round(df["revenue"].sum(), 2),
        "average_revenue_per_mile": round(df["revenue_per_mile"].mean(), 2)
    }