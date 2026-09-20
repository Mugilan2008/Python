import pandas as pd
import numpy as np
data = {
    "Time": ["09:00", "10:00", "11:00", "12:00", "13:00","14:00", "15:00", "16:00", "17:00", "18:00"],
    "Voltage (V)": [230, 232, np.nan, 235, 238, np.nan, 240, 237, 235, 233],
    "Current (A)": [12.5, np.nan, 13.2, 13.8, 14.1, 14.5, np.nan, 15.2, 14.8, 14.0],
    "Power (kW)": [2.75, 2.81, np.nan, 3.10, 3.25, 3.38, np.nan, 3.50, 3.40, 3.26],
    "Temperature (°C)": [32, 34, 36, np.nan, 40, 42, 43, 45, np.nan, 44],
    "Power Factor": [0.92, 0.91, 0.90, 0.89, np.nan, 0.87, 0.86, 0.85, 0.88, np.nan]
}
df = pd.DataFrame(data)
df["Power Factor"] = df["Power Factor"].bfill()
print("Cleaned Dataset:\n", df)
