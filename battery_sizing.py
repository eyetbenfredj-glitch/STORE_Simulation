import pandas as pd

# Load simulation results
results = pd.read_csv(
    r"C:\Users\user\Desktop\newpypsa\simulation_results07.csv",
    parse_dates=["snapshot"]
)

# Renewable generation
results["Renewable"] = results["PV Power"] + results["Wind Power"]

# Excess renewable before battery
results["Excess"] = (results["Renewable"] - results["Load"]).clip(lower=0)

# Battery charging power
# Negative values mean charging in your model
results["Charge"] = (-results["Battery Charger"]).clip(lower=0)

# Curtailed (unused) renewable energy
results["Curtailment"] = (results["Excess"] - results["Charge"]).clip(lower=0)

# Battery full
battery_full = results["Battery SOC"] >= 499.9

# Statistics
hours_full = battery_full.sum()
hours_full_with_excess = (battery_full & (results["Excess"] > 0)).sum()
total_curtailment = results["Curtailment"].sum()
max_curtailment = results["Curtailment"].max()

print("Battery full hours:", hours_full)
print("Battery full + excess hours:", hours_full_with_excess)
print("Total curtailed energy (kWh):", round(total_curtailment,2))
print("Maximum curtailed power (kW):", round(max_curtailment,2))