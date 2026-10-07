import pandas as pd
import pymysql
from datetime import date

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ashesh2708",
    database="healthcare_analytics"
)

cursor = conn.cursor()

risk_df = pd.read_csv("readmission_risk_output.csv")

risk_df.insert(0, "risk_id", range(1, len(risk_df) + 1))
risk_df["prediction_date"] = date.today()

for _, row in risk_df.iterrows():

    cursor.execute("""
    INSERT INTO readmission_risk
    (risk_id, admission_id, prediction_date, risk_score, risk_level)
    VALUES (%s,%s,%s,%s,%s)
    """,
    (
        int(row["risk_id"]),
        int(row["admission_id"]),
        row["prediction_date"],
        float(row["risk_score"]),
        row["risk_level"]
    ))

conn.commit()

print("Readmission Risk table populated successfully")

cursor.close()
conn.close()