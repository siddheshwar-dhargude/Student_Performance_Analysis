"""
Generate a realistic synthetic student performance dataset for
Cognevance Technologies - Level 1 Project: Student Performance Analysis
"""
import numpy as np
import pandas as pd

np.random.seed(42)

N = 300  # number of students

first_names = ["Aarav","Vivaan","Aditya","Vihaan","Arjun","Sai","Reyansh","Krishna",
               "Ishaan","Rohan","Ananya","Diya","Saanvi","Aadhya","Myra","Anika",
               "Kavya","Riya","Pari","Ira","Aryan","Kabir","Shaurya","Dhruv","Yash",
               "Neha","Priya","Sneha","Pooja","Meera"]
last_names = ["Sharma","Verma","Patel","Gupta","Iyer","Nair","Reddy","Kulkarni",
              "Joshi","Mehta","Singh","Rao","Desai","Chavan","Pillai"]

student_id = [f"STU{1000+i}" for i in range(N)]
names = [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(N)]
gender = np.random.choice(["Male", "Female"], size=N, p=[0.52, 0.48])
grade = np.random.choice([9, 10, 11, 12], size=N)

# Attendance % - roughly normal, clipped 40-100
attendance = np.clip(np.random.normal(80, 12, N), 40, 100).round(1)

# Study hours per week - correlated loosely with attendance
study_hours = np.clip(np.random.normal(10, 4, N) + (attendance - 80) * 0.05, 1, 25).round(1)

# Base performance driven by attendance + study hours + noise
base_score = (
    0.55 * attendance +
    1.3 * study_hours +
    np.random.normal(0, 8, N)
)
base_score = np.clip(base_score, 20, 100)

def subject_score(base, spread=6):
    return np.clip(base + np.random.normal(0, spread, N), 0, 100).round(1)

math = subject_score(base_score)
science = subject_score(base_score)
english = subject_score(base_score, spread=8)
social_studies = subject_score(base_score, spread=8)

df = pd.DataFrame({
    "student_id": student_id,
    "name": names,
    "gender": gender,
    "grade": grade,
    "attendance_pct": attendance,
    "study_hours_per_week": study_hours,
    "math_marks": math,
    "science_marks": science,
    "english_marks": english,
    "social_studies_marks": social_studies,
})

df["total_marks"] = (df.math_marks + df.science_marks + df.english_marks + df.social_studies_marks).round(1)
df["average_marks"] = (df.total_marks / 4).round(1)
df["result"] = np.where(df.average_marks >= 40, "Pass", "Fail")

# Introduce a few realistic messy values to give the cleaning step something to do
messy_idx = np.random.choice(df.index, size=12, replace=False)
for i in messy_idx[:6]:
    df.loc[i, "attendance_pct"] = np.nan
for i in messy_idx[6:10]:
    df.loc[i, "study_hours_per_week"] = np.nan
# duplicate a couple of rows
df = pd.concat([df, df.iloc[[5, 20]]], ignore_index=True)

df.to_csv("student_performance_raw.csv", index=False)
print("Saved student_performance_raw.csv with", len(df), "rows")
print(df.head())
