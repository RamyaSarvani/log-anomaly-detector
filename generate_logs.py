import pandas as pd
import numpy as np


np.random.seed(42)

n = 500

data = {
    "error_rate" : np.random.normal(0.02, 0.005, n),
    "latency_ms" : np.random.normal(200,30,n),
    "request_count" : np.random.normal(1000,100,n),
}

for i in range(10):
    idx = np.random.randint(0, n)
    data["error_rate"][idx] = np.random.uniform(0.3, 0.8)
    data["latency_ms"][idx] = np.random.uniform(1500, 3000)

df = pd.DataFrame(data)
df.to_csv("logs.csv", index= False)

print("Done! logs.csv created successfully")
print(f"Total log entries generated: {len(df)}")
print(f"Preview of first 5 rows:")
print(df.head())
