import pandas as pd

# Load simulation results
results = pd.read_csv(
    r"C:\Users\user\Desktop\newpypsa\simulation_results08.csv",
    index_col="snapshot",
    parse_dates=True
)

# Renewable generation
results["Renewable Power"] = (
    results["PV Power"] + results["Wind Power"]
)

# Excess renewable energy
results["Excess Renewable"] = (
    results["Renewable Power"] - results["Load"]
)

# Only keep positive excess
results["Excess Renewable"] = results["Excess Renewable"].clip(lower=0)

# KPIs
total_excess = results["Excess Renewable"].sum()
max_excess = results["Excess Renewable"].max()
hours_excess = (results["Excess Renewable"] > 0).sum()

print("===== BATTERY / EXCESS ENERGY ANALYSIS =====")
print(f"Total excess renewable energy: {total_excess:.2f} kWh")
print(f"Maximum excess power: {max_excess:.2f} kW")
print(f"Hours with excess renewable energy: {hours_excess}")

# Save hourly excess data
results[[
    "PV Power",
    "Wind Power",
    "Load",
    "Renewable Power",
    "Excess Renewable",
    "Battery SOC"
]].to_csv(
    r"C:\Users\user\Desktop\newpypsa\excess_analysis.csv"
)

print("\nSaved: excess_analysis.csv")