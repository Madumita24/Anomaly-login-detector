import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the original dataset (to retain timestamp)
df_orig = pd.read_csv("../Synthetic_User_Login_Dataset.csv", parse_dates=["timestamp"])

# Load the features
df_features = pd.read_csv("../login_features.csv")

# Train Isolation Forest
model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
model.fit(df_features)

# Predict anomaly scores and labels
df_orig['anomaly_score'] = model.decision_function(df_features)
df_orig['anomaly_label'] = model.predict(df_features)
df_orig['anomaly'] = df_orig['anomaly_label'].apply(lambda x: 1 if x == -1 else 0)

# Save final result
df_orig.to_csv("../login_anomaly_results.csv", index=False)
print("login_anomaly_results.csv updated with timestamp included.")
