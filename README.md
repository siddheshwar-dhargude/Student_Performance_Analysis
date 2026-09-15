# cognevance_studentPerformanceAnalysis

**Level 1 (Easy) — Student Performance Analysis**
Cognevance Technologies | Data Science & Data Analytics

## Overview
Analyzes student academic performance data to identify patterns between attendance,
study habits, and marks using basic data analytics techniques in Python.

## Project Structure
```
├── student_performance_raw.csv        # Raw dataset (with missing values & duplicates)
├── student_performance_clean.csv      # Cleaned dataset
├── generate_dataset.py                # Script that generated the sample dataset
├── analysis.py                        # Standalone analysis script (cleaning → charts)
├── Student_Performance_Analysis.ipynb # Full Jupyter notebook workflow
├── charts/
│   ├── chart_01_marks_distribution.png
│   ├── chart_02_pass_fail_pie.png
│   ├── chart_03_attendance_band_bar.png
│   ├── chart_04_attendance_vs_marks_scatter.png
│   └── chart_05_subject_avg_bar.png
├── summary_statistics.csv             # Descriptive statistics table
├── Project_Report.md                  # Full written report with findings
└── README.md
```

## Workflow
1. **Collect** — synthetic dataset generated with `generate_dataset.py` (swap for a
   real Kaggle dataset if preferred; just keep the column names).
2. **Clean** — remove duplicates, impute missing attendance/study-hour values with
   the median.
3. **Analyze** — descriptive stats, correlations between attendance/study hours and
   marks, pass/fail rate.
4. **Visualize** — histogram, pie chart, bar charts, and a scatter/trend chart.
5. **Insight** — attendance is the strongest driver of academic performance; see
   `Project_Report.md` for full findings and recommendations.

## Tools Used
Python, pandas, numpy, matplotlib, seaborn, Jupyter Notebook

## How to Run
```bash
pip install pandas numpy matplotlib seaborn jupyter
python generate_dataset.py      # (optional — raw CSV already included)
jupyter notebook Student_Performance_Analysis.ipynb
```

## Key Result
Overall pass rate: **93.3%** | Attendance–marks correlation: **0.63**

Full findings and recommendations are in [`Project_Report.md`](./Project_Report.md).
