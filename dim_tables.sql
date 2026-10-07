CREATE TABLE dim_patient AS
SELECT
    patient_id,
    first_name,
    last_name,
    gender,
    dob,
    chronic_conditions
FROM patients;
ALTER TABLE dim_patient
ADD PRIMARY KEY (patient_id);


CREATE TABLE dim_doctor AS
SELECT
    doctor_id,
    first_name,
    last_name,
    specialization
FROM doctors;
ALTER TABLE dim_doctor
ADD PRIMARY KEY (doctor_id);


CREATE TABLE dim_date (
    date_key DATE PRIMARY KEY,
    year INT,
    quarter_no INT,
    month_no INT,
    month_name VARCHAR(20),
    day_no INT
);



INSERT INTO dim_date
SELECT DISTINCT
    admission_date AS date_key,
    YEAR(admission_date),
    QUARTER(admission_date),
    MONTH(admission_date),
    MONTHNAME(admission_date),
    DAY(admission_date)
FROM admissions

UNION

SELECT DISTINCT
    discharge_date,
    YEAR(discharge_date),
    QUARTER(discharge_date),
    MONTH(discharge_date),
    MONTHNAME(discharge_date),
    DAY(discharge_date)
FROM admissions
WHERE discharge_date IS NOT NULL;