import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the anomaly results
df = pd.read_csv("../login_anomaly_results.csv", parse_dates=["timestamp"])

# Set a seaborn theme
sns.set(style="whitegrid")

# 1. Distribution of Anomaly Scores
plt.figure(figsize=(10, 5))
sns.histplot(df['anomaly_score'], bins=50, kde=True, color="purple")
plt.title("Distribution of Anomaly Scores")
plt.xlabel("Anomaly Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("anomaly_score_distribution.png")
plt.show()

# 2. Anomalies Over Time
plt.figure(figsize=(12, 5))
sns.scatterplot(x='timestamp', y='anomaly_score', hue='anomaly', data=df, palette={1: "red", 0: "blue"}, alpha=0.6)
plt.title("Anomaly Scores Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Anomaly Score")
plt.legend(title="Anomaly")
plt.tight_layout()
plt.savefig("anomaly_over_time.png")
plt.show()
