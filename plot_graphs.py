import pandas as pd
import matplotlib.pyplot as plt

# Load files from same folder
tr_df = pd.read_csv("transformer_monitoring.csv")
final_df = pd.read_csv("final_output.csv")

# Fix timestamps
tr_df['Timestamp'] = pd.to_datetime(tr_df['Timestamp'], format='mixed', dayfirst=True)
final_df['Timestamp'] = pd.to_datetime(final_df['Timestamp'], format='mixed', dayfirst=True)

# ---------------- Graph 1 ----------------
plt.figure()
plt.plot(tr_df['Timestamp'], tr_df['Transformer_Load'])
plt.plot(tr_df['Timestamp'], tr_df['Billed_Load'])
plt.title("Transformer Load vs Billed Load")
plt.xlabel("Time")
plt.ylabel("Load")
plt.show()

# ---------------- Graph 2 ----------------
plt.figure()
plt.plot(tr_df['Timestamp'], tr_df['Loss'])
plt.title("Energy Loss at Transformer")
plt.xlabel("Time")
plt.ylabel("Loss")
plt.show()

# ---------------- Graph 3 ----------------
suspicious_count = final_df.groupby('Timestamp')['Suspicious'].sum().reset_index()

plt.figure()
plt.plot(suspicious_count['Timestamp'], suspicious_count['Suspicious'])
plt.title("Number of Suspicious Houses Over Time")
plt.xlabel("Time")
plt.ylabel("Suspicious Count")
plt.show()

# ---------------- Graph 4 ----------------
theft_count = final_df.groupby('Timestamp')['Theft_Confirmed'].sum().reset_index()

plt.figure()
plt.plot(theft_count['Timestamp'], theft_count['Theft_Confirmed'])
plt.title("Confirmed Theft Instances (Hybrid)")
plt.xlabel("Time")
plt.ylabel("Theft Confirmed")
plt.show()
