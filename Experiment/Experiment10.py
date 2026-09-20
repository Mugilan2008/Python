import pandas as pd
import numpy as np
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Arun", "Bala", "Charan", "Divya", "Ezhil", "Farah", "Gokul", "Hari", "Indhu", "Jaya"],
    "Age": [20, 21, 20, 22, 21, np.nan, 20, 21, 20, 22],
    "Attendance": [92, 85, np.nan, 78, 88, 95, np.nan, 82, 90, 76],
    "Maths": [85, 76, 91, np.nan, 69, 88, 74, np.nan, 95, 68],
    "Physics": [78, np.nan, 89, 72, 75, 92, np.nan, 85, 94, 70],
    "Programming": [88, 82, 95, 80, np.nan, 90, 78, 87, np.nan, 75]
}
df = pd.DataFrame(data)
print("Missing values in each column:\n", df.isnull().sum())
threshold = len(df) - 1
cleaned_df = df.dropna(thresh=threshold, axis=1)
print("\nCleaned DataFrame (Columns with excessive missing values removed):\n", cleaned_df)
