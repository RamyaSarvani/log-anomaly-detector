import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("logs.csv")
print(f"Loaded {len(df)} log entries")

model = IsolationForest(contamination= 0.02, random_state=42)
df["anomaly"] = model.fit_predict(df)
anomalies = df[df["anomaly"] == -1]
print(f"\nTotal anomalies found: {len(anomalies)} out of {len(df)} entries")
print(f"\nHere are the anomalous log entries:")
print(anomalies[["error_rate","latency_ms","request_count"]].to_string())
