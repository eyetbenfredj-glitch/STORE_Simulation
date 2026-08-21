import pandas as pd

# Path to the dataset
file_path = r"C:\Users\user\Desktop\stage2om\PV_dataset(in).csv"

# Read the CSV file
df = pd.read_csv(file_path)
# Rename timestamp column
df = df.rename(columns={"Unnamed: 0": "Timestamp"})

# Convert timestamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Display the first 5 rows
print("===== First 5 Rows =====")
print(df.head())
print(df.dtypes)




# Display column names
print("\n===== Columns =====")
print(df.columns)

# General information
print("\n===== Dataset Information =====")
print(df.info())

# Statistical summary
print("\n===== Statistical Summary =====")
print(df.describe())

print("\n===== Power Statistics =====")
print(f"Mean Power : {df['Power'].mean():.2f}")
print(f"Maximum Power : {df['Power'].max():.2f}")
print(f"Minimum Power : {df['Power'].min():.2f}")

print("\nMissing values:")
print(df.isnull().sum()) 
print("Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()
# Set timestamp as index
df = df.set_index("Timestamp")

# Convert 5-minute data to hourly averages
df_hourly = df.resample("1h").mean()

print(df_hourly.head(24))
print(df_hourly.shape)

import numpy as np

# ==========================
# Wind turbine power curve
# ==========================

wind_speed_points = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18,
    19, 20
]

power_points = [
    0, 4, 7, 12, 18, 24, 35, 48, 60, 60,
    60, 60, 60, 60, 60, 60, 60, 60,
    60, 60
]

# Convert wind speed to turbine power
df_hourly["Wind_Power"] = np.interp(
    df_hourly["Wind_speed"],
    wind_speed_points,
    power_points
)

print(df_hourly[["Wind_speed", "Wind_Power"]].head(24))

# PV nominal power
PV_nominal = 2400  # Watts

# Normalize PV power for PyPSA
df_hourly["PV_pu"] = df_hourly["Power"] / PV_nominal

# Limit values between 0 and 1 (safety)
df_hourly["PV_pu"] = df_hourly["PV_pu"].clip(0, 1)

print(df_hourly[["Power", "PV_pu"]].head(24))

# Wind turbine rated power (kW)
Wind_nominal = 60

# Normalize wind power
df_hourly["Wind_pu"] = df_hourly["Wind_Power"] / Wind_nominal

# Safety
df_hourly["Wind_pu"] = df_hourly["Wind_pu"].clip(0, 1)

print(df_hourly[["Wind_Power", "Wind_pu"]].head(24))

# Select one day for simulation
one_day = df_hourly.loc["2022-02-24"]

# Extract normalized PV profile
pv_profile = one_day["PV_pu"].values

print(pv_profile)

# Extract normalized Wind profile
wind_profile = one_day["Wind_pu"].values

print(wind_profile)

# Save processed hourly dataset
df_hourly.to_csv(
    r"C:\Users\user\Desktop\pypsaproject\renewable_processed.csv"
)

print("Processed renewable dataset saved!")