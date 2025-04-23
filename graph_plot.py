import pandas as pd
import matplotlib.pyplot as plt
import os

# Read CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'slam_results.csv')
df = pd.read_csv(csv_path)

# Bar chart: ATE
fig, ax = plt.subplots()
w = 0.35
x = range(len(df))

# Use the exact column names from the CSV (including "(m)")
ax.bar([i-w/2 for i in x], df["ATE_RMSE_VIS (m)"], width=w, label="Visual-only")
ax.bar([i+w/2 for i in x], df["ATE_RMSE_VI (m)"], width=w, label="Visual + IMU")

ax.set_xticks(x)
ax.set_xticklabels(df["Dataset"])
ax.set_ylabel("ATE RMSE [m]")
ax.legend()
plt.tight_layout()
plt.show()