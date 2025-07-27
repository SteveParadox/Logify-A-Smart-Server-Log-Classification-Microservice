# Log Message Classification System

A powerful hybrid log classification pipeline using regex, BERT-based embeddings, and LLM fallback — built for production log intelligence.

---
## Business Applications

Unlock real-world value across multiple industries with this intelligent log classification microservice:

---

### 🔐 Security & Compliance Monitoring  
**Industry:** Finance, Healthcare, Government  
**Use Case:** Detect anomalous user behavior, unauthorized access patterns, or deprecated API usage.

---

### ⚙️ IT Operations & Incident Response  
**Industry:** SaaS, Telecom, Cloud Infrastructure  
**Use Case:** Automate triaging of logs to classify performance issues, workflow breakdowns, or deployment anomalies.

---

### 📊 Business Intelligence & Root Cause Analysis  
**Industry:** Retail, Logistics, E-commerce  
**Use Case:** Extract structured insights from noisy logs for trend analysis and operational optimization.

---

### 🧠 Smart Observability in AIOps Pipelines  
**Industry:** DevOps Tooling, Monitoring Platforms  
**Use Case:** Embed the microservice in platforms like Datadog, Splunk, or Prometheus to enable semantic alerting and anomaly classification.

---

### 🏛️ Legacy System Modernization  
**Industry:** Enterprises with Mainframes, Old CRMs  
**Use Case:** Improve visibility into legacy logs (e.g., from `LegacyCRM`) that modern systems struggle to interpret.


---

##  Features

-  Rule-based classification with regex
-  ML-based classification using Sentence-BERT + Logistic Regression
-  LLM fallback for hard-to-classify legacy logs (Groq + LLaMA3)
-  Clustering & Visualization with UMAP
-  Modular pipeline (easy to extend and integrate into APIs or batch systems)
-  FastAPI endpoint for real-time log file classification

---

##  Installation

Ensure Python 3.9 or higher is installed.

```bash
git clone https://github.com/SteveParadox/Logify-A-Smart-Server-Log-Classification-Microservice.git
pip install -r requirements.txt
cd app
```

Create a `.env` file with your Groq API key:

```env
GROQ_API_KEY=your_groq_key_here
```

---

## 🛠️ Usage

###  Classify Logs from CSV

```bash
python classify.py
```

This reads `resources/test.csv` and writes the classified logs to `resources/output.csv`.

### 📡 Classify via FastAPI

Run the API:

```bash
uvicorn server:app --reload
```

Send a POST request to:

```
POST /classify/
```

With form-data including a `.csv` file having the columns: `source` and `log_message`.

---

### 📜 Example CSV Format

```csv
source,log_message
LegacyCRM,System reboot initiated by user Admin
ModernApp,User User12 logged in.
```

---

## 🧪 API Overview

| Module              | Role                            |
|---------------------|----------------------------------|
| `processor_regex.py`| Regex-based classifier           |
| `processor_bert.py` | BERT embedding + ML classifier   |
| `processor_llm.py`  | LLM fallback via Groq            |
| `classify.py`       | Orchestration & CSV classification |
| `server.py`         | FastAPI for real-time classification |

---

## 🧠 Model Architecture

```
                   +-----------------+
                   |   Regex Rules   |
                   +--------+--------+
                            |
                            v
                Match? --> Yes --> Label
                            |
                            v
            +----------- No (Fallback) ------------+
            |                                      |
            v                                      v
     BERT + Classifier                   →     LLM via Groq
```

---

## 🔐 License

MIT License © 2025 Your Highness

---

## 🤝 Contributions

Pull requests and feature suggestions are welcome!
