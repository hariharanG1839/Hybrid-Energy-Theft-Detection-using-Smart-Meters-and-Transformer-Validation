import pandas as pd

ml_df = pd.read_csv(r"C:\2026\ENERGY THEFT\ml_output.csv")
tr_df = pd.read_csv(r"C:\2026\ENERGY THEFT\transformer_monitoring.csv")

# FIX TIMESTAMP FORMAT FOR BOTH
ml_df['Timestamp'] = pd.to_datetime(
    ml_df['Timestamp'], 
    format='mixed', 
    dayfirst=True
)

tr_df['Timestamp'] = pd.to_datetime(
    tr_df['Timestamp'], 
    format='mixed', 
    dayfirst=True
)


# Now merge
merged = pd.merge(ml_df, tr_df, on='Timestamp')

# Hybrid rule
merged['Theft_Confirmed'] = (
    (merged['Suspicious'] == 1) &
    (merged['Loss'] > 0)
).astype(int)

merged.to_csv(r"C:\2026\ENERGY THEFT\final_output.csv", index=False)

print("Rows after merge:", len(merged))
print(merged[['Timestamp','House_ID','Suspicious','Loss','Theft_Confirmed']].head(20))
