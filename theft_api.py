from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("ml_output_fixed.csv")

@app.get("/summary")
def get_summary():
    suspicious = int((df["Suspicious"] == 1).sum())
    normal = int((df["Suspicious"] == 0).sum())
    return {
        "total": len(df),
        "suspicious": suspicious,
        "normal": normal
    }

@app.get("/houses")
def get_houses():
    df = pd.read_csv("ml_output_fixed.csv")

    data = df.groupby("House_ID").first().reset_index()

    result = []

    for _, row in data.iterrows():
        result.append({
            "houseId": row["House_ID"],
            "status": "Suspicious" if row["Suspicious"] == 1 else "Normal",
            "is_theft": True if row["Suspicious"] == 1 else False,
            "deviation_score": row.get("Deviation", 0),
            "records": 5000
        })

    return result

@app.get("/houses/{house_id}")
def get_house_detail(house_id: str):
    rows = df[df["House_ID"] == house_id]
    if rows.empty:
        return {"error": "House not found"}
    latest = rows.sort_values("Timestamp").iloc[-1]
    return {
        "House_ID": house_id,
        "Suspicious": int(latest["Suspicious"]),
        "Deviation": float(latest["Deviation"]),
        "Electricity_Consumed": float(latest["Electricity_Consumed"]),
        "Actual_Consumption": float(latest["Actual_Consumption"]),
        "Reported_Consumption": float(latest["Reported_Consumption"]),
        "Timestamp": str(latest["Timestamp"]),
        "Anomaly_Label": int(latest["Anomaly_Label"])
    }

@app.get("/top-suspicious")
def get_top_suspicious(limit: int = 10):
    suspicious_df = df[df["Suspicious"] == 1]
    top = suspicious_df.groupby("House_ID")["Deviation"].max().nlargest(limit).reset_index()
    return top.to_dict(orient="records")