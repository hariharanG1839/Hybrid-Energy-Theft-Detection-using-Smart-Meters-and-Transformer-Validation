import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv(r"C:\2026\ENERGY THEFT\smart_grid_featured.csv")

# Clean Day/Night
df['Day_Night'] = df['Day_Night'].map({'Day': 0, 'Night': 1})

# Fill feature NaNs
df['Rolling_Var'] = df['Rolling_Var'].fillna(0)
df['Weather_Adjusted'] = df['Weather_Adjusted'].fillna(0)
df['Deviation'] = df['Deviation'].fillna(0)

# ---- FIX FOR ANOMALY LABEL ---- #

# Remove spaces, make lowercase
df['Anomaly_Label'] = df['Anomaly_Label'].astype(str).str.strip().str.lower()

# Keep only valid rows
df = df[df['Anomaly_Label'].isin(['normal', 'anomaly'])]

# Convert to 0/1
df['Anomaly_Label'] = df['Anomaly_Label'].map({'normal': 0, 'anomaly': 1})


# ---------------- FEATURES ---------------- #
features = [
    'Hour',
    'Day_Night',
    'Rolling_Var',
    'Weather_Adjusted'
]


X = df[features]
y = df['Anomaly_Label']

# ---------------- TRAIN TEST SPLIT ---------------- #

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL ---------------- #

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
