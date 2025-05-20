# 🔐 Anomaly Detection in User Login Patterns

A machine learning project that detects suspicious login behavior using Isolation Forest — inspired by real-world digital identity threats.



## 🎯 Objective

Identify unusual login events that may indicate account compromise, bot access, or insider misuse by analyzing login patterns over time.



## 🛠️ Tools & Tech Stack

- **Python 3.x**
- `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
- VSCode (local development)
- GitHub (version control & showcase)



## 🔍 Methodology

1. **Preprocessing**
   - Time-based features: hour, day
   - Categorical encoding: location, device, login method
   - Behavior: per-user login failure rate

2. **Modeling**
   - Isolation Forest trained on engineered features
   - Each login scored for anomaly likelihood
   - Labels assigned: Normal (0), Anomalous (1)

3. **Visualization**
   - Histogram of anomaly score distribution
   - Time-series scatterplot of anomalies

## 🧠 Results & Insights

- The Isolation Forest model flagged ~2% of logins as **anomalous**, based on behavioral deviation.
- High anomaly scores were associated with:
  - Logins during **odd hours (e.g., 2–5 AM)**
  - **Device switching** (e.g., sudden move from iOS to Linux)
  - **Geographical inconsistency** (e.g., frequent location changes)
  - Users with unusually **high login failure rates**
- These behaviors may indicate:
  - Account compromise
  - Credential stuffing attempts
  - Insider misuse or bot activity

This shows how machine learning can help detect threats **without needing labeled attack data** — a powerful use case for real-time identity protection systems.

This project demonstrates:
  - Analytical thinking on behavioral data
  - Threat detection with machine learning
  - Clear visual storytelling of risk signals




