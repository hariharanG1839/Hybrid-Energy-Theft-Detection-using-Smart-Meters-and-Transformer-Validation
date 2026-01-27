import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\2026\ENERGY THEFT\smart_grid_with_theft.csv")

# Make sure values are numeric
df['Actual_Consumption'] = pd.to_numeric(df['Actual_Consumption'], errors='coerce')
df['Reported_Consumption'] = pd.to_numeric(df['Reported_Consumption'], errors='coerce')

# Group by timestamp (simulating transformer)
transformer_df = df.groupby('Timestamp').agg(
    Transformer_Load=('Actual_Consumption', 'sum'),
    Billed_Load=('Reported_Consumption', 'sum')
).reset_index()

# Compute energy loss
transformer_df['Loss'] = transformer_df['Transformer_Load'] - transformer_df['Billed_Load']

# Save result
transformer_df.to_csv(r"C:\2026\ENERGY THEFT\transformer_monitoring.csv", index=False)

print(transformer_df.head())

