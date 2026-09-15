"""
Cognevance Technologies - Level 1: Student Performance Analysis
Cleaning, EDA, visualization, and insight generation.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 110

# ---------- 1. Load ----------
df = pd.read_csv("student_performance_raw.csv")
print("Raw shape:", df.shape)

# ---------- 2. Clean ----------
before = len(df)
df = df.drop_duplicates(subset="student_id")
print(f"Removed {before - len(df)} duplicate rows")

# Fill missing attendance / study hours with median (robust to outliers)
df["attendance_pct"] = df["attendance_pct"].fillna(df["attendance_pct"].median())
df["study_hours_per_week"] = df["study_hours_per_week"].fillna(df["study_hours_per_week"].median())

df["attendance_pct"] = df["attendance_pct"].round(1)
df["study_hours_per_week"] = df["study_hours_per_week"].round(1)

df.to_csv("student_performance_clean.csv", index=False)
print("Clean shape:", df.shape)

# ---------- 3. Analyze ----------
summary = df[["attendance_pct", "study_hours_per_week", "math_marks", "science_marks",
              "english_marks", "social_studies_marks", "average_marks"]].describe().round(1)
summary.to_csv("summary_statistics.csv")

pass_rate = (df["result"] == "Pass").mean() * 100
corr_attendance_avg = df["attendance_pct"].corr(df["average_marks"])
corr_study_avg = df["study_hours_per_week"].corr(df["average_marks"])

# attendance bucket vs avg marks
df["attendance_band"] = pd.cut(df["attendance_pct"], bins=[0, 60, 75, 90, 100],
                                labels=["<60%", "60-75%", "75-90%", "90-100%"])
band_avg = df.groupby("attendance_band", observed=True)["average_marks"].mean().round(1)
band_avg.to_csv("attendance_band_avg_marks.csv")

gender_avg = df.groupby("gender")["average_marks"].mean().round(1)

print("\n--- KEY STATS ---")
print("Pass rate: {:.1f}%".format(pass_rate))
print("Correlation attendance vs average marks: {:.2f}".format(corr_attendance_avg))
print("Correlation study hours vs average marks: {:.2f}".format(corr_study_avg))
print("\nAverage marks by attendance band:\n", band_avg)
print("\nAverage marks by gender:\n", gender_avg)

# ---------- 4. Visualizations ----------

# Chart 1: Distribution of average marks (histogram)
plt.figure(figsize=(7, 4.5))
sns.histplot(df["average_marks"], bins=20, kde=True, color="#4C72B0")
plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("chart_01_marks_distribution.png")
plt.close()

# Chart 2: Pass vs Fail pie chart
plt.figure(figsize=(5, 5))
counts = df["result"].value_counts()
plt.pie(counts, labels=counts.index, autopct="%1.1f%%", colors=["#55A868", "#C44E52"],
        startangle=90)
plt.title("Pass vs Fail Rate")
plt.tight_layout()
plt.savefig("chart_02_pass_fail_pie.png")
plt.close()

# Chart 3: Average marks by attendance band (bar chart)
plt.figure(figsize=(7, 4.5))
band_avg.plot(kind="bar", color="#DD8452")
plt.title("Average Marks by Attendance Band")
plt.xlabel("Attendance Band")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_03_attendance_band_bar.png")
plt.close()

# Chart 4: Attendance vs Average Marks scatter with trend line
plt.figure(figsize=(7, 4.5))
sns.regplot(data=df, x="attendance_pct", y="average_marks",
            scatter_kws={"alpha": 0.5, "color": "#4C72B0"}, line_kws={"color": "#C44E52"})
plt.title(f"Attendance vs Average Marks (corr = {corr_attendance_avg:.2f})")
plt.xlabel("Attendance %")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("chart_04_attendance_vs_marks_scatter.png")
plt.close()

# Chart 5: Subject-wise average marks bar chart
plt.figure(figsize=(7, 4.5))
subj_avg = df[["math_marks", "science_marks", "english_marks", "social_studies_marks"]].mean()
subj_avg.index = ["Math", "Science", "English", "Social Studies"]
subj_avg.round(1).plot(kind="bar", color="#8172B2")
plt.title("Subject-wise Average Marks")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_05_subject_avg_bar.png")
plt.close()

print("\nAll charts saved.")
