import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv(r"C:\2026\ENERGY THEFT\smart_grid_featured.csv")

# Clean Day/Night
df['Day_Night'] = df['Day_Night'].map({'Day': 0, 'Night': 1})
df['Rolling_Var'] = df['Rolling_Var'].fillna(0)
df['Weather_Adjusted'] = df['Weather_Adjusted'].fillna(0)

# Features (no leakage)
features = [
    'Hour',
    'Day_Night',
    'Rolling_Var',
    'Weather_Adjusted'
]

X = df[features]

# Unsupervised anomaly detection
model = IsolationForest(contamination=0.1, random_state=42)
df['Suspicious'] = model.fit_predict(X)

# Convert output: -1 = anomaly, 1 = normal
df['Suspicious'] = df['Suspicious'].map({1: 0, -1: 1})

# Save
df.to_csv(r"C:\2026\ENERGY THEFT\ml_output.csv", index=False)

print(df[['Timestamp','House_ID','Suspicious']].head(20))
