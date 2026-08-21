import pypsa
import pandas as pd
import numpy as np

# Create an empty network
network = pypsa.Network()
network.set_snapshots(pd.date_range(
    "2022-02-24 00:00",
    periods=24,
    freq="h"
))
print("Network created successfully!")

network.add(
    "Bus",
    "Supermarket Bus",
    carrier="AC"
)
print(network.buses)
network.add(
    "Generator",
    "Grid",
    bus="Supermarket Bus",
    carrier="grid",
    p_nom=1000,
    marginal_cost=100
)
print(network.generators)
network.add(
    "Load",
    "Supermarket Load",
    bus="Supermarket Bus",
)
print(network.loads)
load_profile = [
    150, 140, 130, 120, 120, 130,
    180, 250, 320, 380, 420, 450,
    470, 460, 440, 420, 400, 380,
    350, 300, 260, 220, 180, 160
]
network.loads_t.p_set["Supermarket Load"] = load_profile
print(network.loads_t.p_set)

network.add(
    "Generator",
    "PV",
    bus="Supermarket Bus",
    carrier="solar",
    p_nom=500
)
print(network.generators)
import pandas as pd

# Load processed PV data
df_pv = pd.read_csv(
    r"C:\Users\user\Desktop\pypsaproject\PV_processed.csv",
    index_col="Timestamp",
    parse_dates=True
)

# Select one simulation day
one_day = df_pv.loc["2022-02-24"]

# Extract PV profile for PyPSA
pv_profile = one_day["PV_pu"].values

print("PV profile:")
print(pv_profile) 
network.generators_t.p_max_pu["PV"] = pv_profile
print(network.generators_t.p_max_pu)

network.add(
    "Bus",
    "Battery Bus",
    carrier="AC"
)
print(network.buses)

network.add(
    "Store",
    "Battery",
    bus="Battery Bus",
    e_nom=500,
    e_initial=250,      # 50% of the new capacity
    e_min_pu=0.2,
    standing_loss=0.001,
    marginal_cost=1,
) 
print(network.stores)

network.add(
    "Link",
    "Battery Charger",
    bus0="Supermarket Bus",
    bus1="Battery Bus",
    p_nom=100,
    efficiency=0.95,
    p_min_pu=-1,
)
print(network.links)

network.sanitize()
network.optimize()
print("Objective value:", network.objective)
results = pd.DataFrame({
    "PV Power": network.generators_t.p["PV"],
    "Grid Power": network.generators_t.p["Grid"],
    "Load": network.loads_t.p["Supermarket Load"],
    "Battery SOC": network.stores_t.e["Battery"],
    "Battery Charger": network.links_t.p0["Battery Charger"]
})

print(results)
import matplotlib.pyplot as plt

# -----------------------------
# 1. PV, Grid and Load
# -----------------------------
plt.figure(figsize=(12, 5))

plt.plot(results.index, results["PV Power"], label="PV Power")
plt.plot(results.index, results["Grid Power"], label="Grid Power")
plt.plot(results.index, results["Load"], label="Load")

plt.xlabel("Time")
plt.ylabel("Power (kW)")
plt.title("Supermarket Energy Flow")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -----------------------------
# 2. Battery SOC
# -----------------------------
plt.figure(figsize=(12, 5))

plt.plot(
    results.index,
    results["Battery SOC"],
    label="Battery SOC"
)

plt.xlabel("Time")
plt.ylabel("Energy (kWh)")
plt.title("Battery State of Charge")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -----------------------------
# 3. Battery Charging / Discharging
# -----------------------------
plt.figure(figsize=(12, 5))

plt.plot(
    results.index,
    results["Battery Charger"],
    label="Battery Charger Power"
)

plt.axhline(0, linestyle="--")

plt.xlabel("Time")
plt.ylabel("Power (kW)")
plt.title("Battery Charging / Discharging")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()