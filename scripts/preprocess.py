import pandas as pd

# Load dataset
df = pd.read_csv("../Synthetic_User_Login_Dataset.csv", parse_dates=["timestamp"])


# 1. Extract time-based features
df['hour_of_day'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek

# 2. Compute per-user login failure rate
failure_rate = df.groupby('user_id')['login_success'].apply(lambda x: 1 - x.mean()).rename('failure_rate')
df = df.merge(failure_rate, on='user_id')

# 3. One-hot encode 
df_encoded = pd.get_dummies(df, columns=['location', 'device_type', 'login_method'], drop_first=True)

# 4. Select modeling features
features = ['hour_of_day', 'day_of_week', 'failure_rate'] + \
           [col for col in df_encoded.columns if col.startswith(('location_', 'device_type_', 'login_method_'))]
df_model = df_encoded[features]

# 5. Save processed features
df_model.to_csv("login_features.csv", index=False)
print("Feature-engineered dataset saved as 'login_features.csv'")
