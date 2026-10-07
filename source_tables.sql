USE healthcare_analytics;

CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contact_no VARCHAR(15) NOT NULL,
    address VARCHAR(255),
    chronic_conditions VARCHAR(255)
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(255) NOT NULL,
    contact_no VARCHAR(15) NOT NULL
);

CREATE TABLE admissions (
    admission_id INT PRIMARY KEY,
    patient_id INT,
    admission_date DATE NOT NULL,
    discharge_date DATE,
    diagnosis VARCHAR(255) NOT NULL,
    doctor_id INT,
    room_no VARCHAR(10),

    FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    FOREIGN KEY (doctor_id)
        REFERENCES doctors(doctor_id)
);

CREATE TABLE vitals (
    vital_id INT PRIMARY KEY,
    admission_id INT,
    recorded_time DATETIME NOT NULL,
    heart_rate INT NOT NULL,
    blood_pressure VARCHAR(10) NOT NULL,
    oxygen_level INT NOT NULL,
    temperature DECIMAL(5,2) NOT NULL,

    FOREIGN KEY (admission_id)
        REFERENCES admissions(admission_id)
);

CREATE TABLE treatments (
    treatment_id INT PRIMARY KEY,
    admission_id INT,
    treatment_date DATE NOT NULL,
    `procedure` VARCHAR(255),
    medication VARCHAR(255) NOT NULL,
    dosage VARCHAR(50),

    FOREIGN KEY (admission_id)
        REFERENCES admissions(admission_id)
);

CREATE TABLE readmission_risk (
    risk_id INT PRIMARY KEY,
    admission_id INT,
    prediction_date DATE NOT NULL,
    risk_score DECIMAL(5,2) NOT NULL,
    risk_level VARCHAR(10) NOT NULL,

    FOREIGN KEY (admission_id)
        REFERENCES admissions(admission_id)
);