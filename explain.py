import pandas as pd
from sklearn.ensemble import IsolationForest
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Load logs and run the model
df = pd.read_csv("logs.csv")
model = IsolationForest(contamination=0.02, random_state=42)
df["anomaly"] = model.fit_predict(df)

#  Get only anomalies
anomalies = df[df["anomaly"] == -1]
print(f"Found {len(anomalies)} anomalies — asking GPT to explain each one...\n")

# Loop through each anomaly and ask GPT to explain it
for i, (_, row) in enumerate(anomalies.iterrows()):

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

    explanation = response.choices[0].message.content

    print(f"--- Anomaly {i+1} ---")
    print(f"Error Rate : {row['error_rate']:.2%}")
    print(f"Latency    : {row['latency_ms']:.0f}ms")
    print(f"Requests   : {row['request_count']:.0f}")
    print(f"GPT Says   : {explanation}")
    print()