from fastapi import FastAPI
import pandas as pd
from sklearn.ensemble import IsolationForest
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
@app.get("/health")
def health():
    return {"status": "running"}

# Main analysis endpoint
@app.post("/analyze")
def analyze_logs(data: dict):

    # Convert incoming JSON to DataFrame
    df = pd.DataFrame(data["logs"])

    # Run anomaly detection
    model = IsolationForest(contamination=0.02, random_state=42)
    df["anomaly"] = model.fit_predict(df[["error_rate", "latency_ms", "request_count"]])

    # Get anomalous rows
    anomalies = df[df["anomaly"] == -1]

    # Ask GPT to explain each anomaly
    results = []
    for _, row in anomalies.iterrows():

        prompt = f"""
        A backend system logged these metrics and were flagged as anomalous:
        - Error rate: {row['error_rate']:.2%}
        - Latency: {row['latency_ms']:.0f}ms
        - Request count: {row['request_count']:.0f}

        In 2-3 sentences, explain what might be causing this anomaly
        and what an engineer should investigate first.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        results.append({
            "error_rate": round(row["error_rate"], 4),
            "latency_ms": round(row["latency_ms"], 2),
            "request_count": round(row["request_count"], 0),
            "explanation": response.choices[0].message.content
        })

    return {
        "total_logs_analyzed": len(df),
        "anomalies_found": len(results),
        "details": results
    }