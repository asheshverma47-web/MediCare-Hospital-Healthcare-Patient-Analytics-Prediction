import pandas as pd
import pymysql
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ashesh2708",
    database="healthcare_analytics"
)

query = """
SELECT *
FROM vw_readmission_features
"""

df = pd.read_sql(query, conn)

conn.close()

# Age Calculation
df['dob'] = pd.to_datetime(df['dob'])
df['age'] = ((pd.Timestamp.now() - df['dob']).dt.days / 365).astype(int)

# Target Variable
df['readmission_flag'] = df['previous_admissions'].apply(
    lambda x: 1 if x > 0 else 0
)

# Fill missing values
df['avg_heart_rate'] = df['avg_heart_rate'].fillna(df['avg_heart_rate'].mean())
df['avg_oxygen_level'] = df['avg_oxygen_level'].fillna(df['avg_oxygen_level'].mean())
df['avg_temperature'] = df['avg_temperature'].fillna(df['avg_temperature'].mean())

# Encode categorical columns
le_gender = LabelEncoder()
df['gender'] = le_gender.fit_transform(df['gender'])

le_condition = LabelEncoder()
df['chronic_conditions'] = le_condition.fit_transform(
    df['chronic_conditions'].astype(str)
)

X = df[
    [
        'age',
        'gender',
        'chronic_conditions',
        'previous_admissions',
        'avg_heart_rate',
        'avg_oxygen_level',
        'avg_temperature'
    ]
]

y = df['readmission_flag']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

df['risk_score'] = model.predict_proba(X)[:,1]

def risk_level(score):
    if score >= 0.70:
        return "High"
    elif score >= 0.40:
        return "Medium"
    else:
        return "Low"

df['risk_level'] = df['risk_score'].apply(risk_level)

risk_data = df[
    [
        'admission_id',
        'risk_score',
        'risk_level'
    ]
]

print(risk_data.head())

risk_data.to_csv(
    'readmission_risk_output.csv',
    index=False
)

print("Risk file created successfully")