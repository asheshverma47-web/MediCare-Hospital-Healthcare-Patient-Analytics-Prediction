CREATE TABLE fact_admissions AS
SELECT
    admission_id,
    patient_id,
    doctor_id,
    admission_date,
    discharge_date,
    diagnosis,
    room_no,
    DATEDIFF(discharge_date, admission_date) AS length_of_stay
FROM admissions;


CREATE TABLE fact_vitals AS
SELECT *
FROM vitals;


CREATE TABLE fact_treatments AS
SELECT *
FROM treatments;


CREATE TABLE fact_readmission_risk AS
SELECT *
FROM readmission_risk;

SHOW TABLES;