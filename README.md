# Log Anomaly Detector

## Project Overview

**Log Anomaly Detector** is a Machine Learning-powered observability tool that automatically identifies unusual behavior in backend server logs and explains the findings in plain English using AI.

The system simulates realistic backend monitoring data, detects anomalies using the Isolation Forest algorithm, and leverages OpenAI GPT-4o-mini to generate human-readable explanations that help engineers quickly understand potential issues.

The entire workflow is exposed through a FastAPI REST API, making it easy to integrate into monitoring dashboards, alerting systems, or internal developer tools.

---

## How It Works

```text
Generate Log Data
        │
        ▼
Extract Metrics
(Error Rate, Latency, Requests)
        │
        ▼
Isolation Forest Model
(Detect Anomalies)
        │
        ▼
OpenAI GPT-4o-mini
(Generate Explanation)
        │
        ▼
FastAPI REST Endpoint
(Return Results)
```

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* OpenAI API (GPT-4o-mini)
* FastAPI
* Uvicorn
* python-dotenv

---

## Project Structure

```text
log-anomaly-detector/
│
├── main.py              # FastAPI application and main entry point
├── generate_logs.py     # Generates synthetic log data
├── detector.py          # Isolation Forest anomaly detection
├── explain.py           # OpenAI GPT-4o-mini integration
├── logs.csv             # Generated log dataset
├── requirements.txt     # Project dependencies
├── .gitignore           # Excludes .env from version control
└── README.md
```

---

## How To Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/ramyasarvani/log-anomaly-detector.git
cd log-anomaly-detector
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

### 5. Start the API

```bash
uvicorn main:app --reload
```

### 6. Access API

```text
http://localhost:8000/docs
```

Interactive Swagger documentation will be available automatically.

---

## Example API Output

```json
{
  "timestamp": "2026-06-01T14:32:11Z",
  "error_rate": 0.38,
  "latency_ms": 2450,
  "request_count": 105,
  "anomaly": true,
  "explanation": "This server instance experienced unusually high latency and error rates compared to normal traffic patterns. The low request volume suggests the issue is likely related to backend service degradation or a dependency failure rather than increased user load."
}
```

---

## Key Concepts Used

* Synthetic log generation for observability simulations
* Feature engineering from operational metrics
* Unsupervised anomaly detection using Isolation Forest
* AI-powered root-cause style explanations with GPT-4o-mini
* REST API development with FastAPI
* Environment-based configuration using python-dotenv
* Production-style service architecture and API design

---

## Future Enhancements

* Real-time log ingestion from Kafka
* Support for Elasticsearch and Splunk data sources
* Historical anomaly trend visualization
* Automated alerting through Slack and Microsoft Teams
* Model retraining using production log datasets

This project demonstrates practical applications of Machine Learning, Generative AI, and backend engineering to improve system observability and incident investigation workflows.
