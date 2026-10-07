import pandas as pd
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ashesh2708",
    database="healthcare_analytics"
)

cursor = conn.cursor()

patients = pd.read_csv("patients.csv").fillna("")
doctors = pd.read_csv("doctors.csv").fillna("")
admissions = pd.read_csv("admissions.csv").fillna("")
vitals = pd.read_csv("vitals.csv").fillna("")
treatments = pd.read_csv("treatments.csv").fillna("")

cursor.executemany(
    "INSERT INTO patients VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
    patients.values.tolist()
)

cursor.executemany(
    "INSERT INTO doctors VALUES (%s,%s,%s,%s,%s)",
    doctors.values.tolist()
)

cursor.executemany(
    "INSERT INTO admissions VALUES (%s,%s,%s,%s,%s,%s,%s)",
    admissions.values.tolist()
)

cursor.executemany(
    "INSERT INTO vitals VALUES (%s,%s,%s,%s,%s,%s,%s)",
    vitals.values.tolist()
)

cursor.executemany(
    "INSERT INTO treatments VALUES (%s,%s,%s,%s,%s,%s)",
    treatments.values.tolist()
)

conn.commit()

print("Data Loaded Successfully")

cursor.close()
conn.close()