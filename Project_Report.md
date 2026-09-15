# Student Performance Analysis — Project Report

**Cognevance Technologies | Level 1 — Easy | Data Science & Data Analytics**

## 1. Objective
Analyze student academic performance data to identify patterns between attendance,
study habits, and academic scores using basic data analytics techniques.

## 2. Dataset
- 300 students (after cleaning), synthetically generated to resemble a realistic
  Kaggle-style student performance dataset.
- Fields: student ID, name, gender, grade, attendance %, weekly study hours, marks in
  Math/Science/English/Social Studies, total & average marks, pass/fail result.
- Raw file: `student_performance_raw.csv` (302 rows, includes intentional missing
  values and duplicates)
- Cleaned file: `student_performance_clean.csv` (300 rows)

## 3. Tools Used
- Python 3
- pandas, numpy — data cleaning & analysis
- matplotlib, seaborn — visualization
- Jupyter Notebook — workflow documentation

## 4. Data Cleaning Steps
1. Removed 2 duplicate student records (matched on `student_id`).
2. Filled missing `attendance_pct` and `study_hours_per_week` values with the column
   median (chosen over mean for robustness to outliers).
3. Rounded numeric fields to 1 decimal place for consistency.

## 5. Key Findings

| Metric | Value |
|---|---|
| Overall pass rate | 93.3% |
| Correlation: attendance vs average marks | 0.63 |
| Correlation: study hours vs average marks | 0.52 |
| Avg marks, attendance < 60% | 42.5 |
| Avg marks, attendance 90–100% | 68.9 |

- **Attendance is the strongest single driver of performance** in this dataset. Marks
  rise steadily as attendance rises, with an average ~26-point gap between the lowest
  and highest attendance bands.
- **Study hours have a moderate positive relationship** with marks (corr = 0.52),
  weaker than attendance but still meaningful.
- **Gender gap is small**: average marks were 59.5 (female) vs 56.9 (male) — a modest
  difference not likely to be practically significant given normal variation.
- **Subject performance is balanced** across Math, Science, English, and Social
  Studies — no subject stands out as a systemic weak point.

## 6. Visualizations
See the `charts/` folder (also embedded in the notebook):
1. `chart_01_marks_distribution.png` — Histogram of average marks
2. `chart_02_pass_fail_pie.png` — Pass/fail pie chart
3. `chart_03_attendance_band_bar.png` — Average marks by attendance band
4. `chart_04_attendance_vs_marks_scatter.png` — Attendance vs marks scatter + trend line
5. `chart_05_subject_avg_bar.png` — Subject-wise average marks

## 7. Recommendations
1. **Target attendance below 75%** with interventions (reminders, mentoring, parent
   outreach) — this is where the steepest performance drop-off occurs.
2. **Encourage consistent study habits**, not just cramming — study hours correlate
   with marks but less strongly than attendance, suggesting quality/consistency of
   study time matters too.
3. **Monitor at-risk students proactively** using a simple rule (e.g., attendance
   < 65% AND average marks < 50%) to flag students for early support.

## 8. Conclusion
This analysis demonstrates a clear, quantifiable link between attendance and academic
performance. Of the two levers examined (attendance and study hours), attendance has
the larger and more consistent effect, making it the most actionable target for
school interventions aimed at improving outcomes.

---
*Note: This project uses a synthetically generated dataset for demonstration.
Swap in a real Kaggle dataset (with matching column names) in `generate_dataset.py`
/ the notebook's Section 2 to reproduce this workflow on real-world data.*
