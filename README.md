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



This project demonstrates:
  - Analytical thinking on behavioral data
  - Threat detection with machine learning
  - Clear visual storytelling of risk signals




