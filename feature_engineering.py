import pandas as pd

df = pd.read_csv(r"C:\2026\ENERGY THEFT\smart_grid_with_theft.csv")

df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst=True)

df['Deviation'] = df['Reported_Consumption'] - df['Avg_Past_Consumption']

df['Hour'] = df['Timestamp'].dt.hour

df['Day_Night'] = df['Hour'].apply(lambda x: 'Night' if x < 6 or x > 20 else 'Day')

df['Rolling_Var'] = (
    df.groupby('House_ID')['Reported_Consumption']
      .rolling(window=5)
      .var()
      .reset_index(0, drop=True)
)

df['Weather_Adjusted'] = df['Reported_Consumption'] / (df['Temperature'] + 0.1)

df.to_csv(r"C:\2026\ENERGY THEFT\smart_grid_featured.csv", index=False)

print(df.head())
