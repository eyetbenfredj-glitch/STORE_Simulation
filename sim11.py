import pypsa
import pandas as pd
import numpy as np

# Create an empty network
network = pypsa.Network()
network.set_snapshots(pd.date_range(
    "2024-01-01 00:00",
    "2024-05-31 23:00",
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
    p_nom=2000,
    marginal_cost=100
)
print(network.generators)
network.add(
    "Load",
    "EV Load",
    bus="Supermarket Bus",
)
print(network.loads)
# Load EV data
df_ev = pd.read_csv(
    r"C:\Users\user\Desktop\newpypsa\ev_A1_hourly.csv",
    parse_dates=["datetime"]
)

# Select simulation period  
ev_period = df_ev.loc[
    (df_ev["datetime"] >= "2024-01-01 00:00") &
    (df_ev["datetime"] <= "2024-05-31 23:00")
]

# Extract EV hourly load
ev_load = ev_period["power"].values


print("EV load:")
print(ev_load)

network.loads_t.p_set["EV Load"] = ev_load
print(network.loads_t.p_set)

# Load processed renewable data
df_pv = pd.read_csv(
    r"C:\Users\user\Desktop\pypsaproject\renewable_processed.csv",
    index_col="Timestamp",
    parse_dates=True
)

# Select simulation period
one_period = df_pv.loc[
    (df_pv.index >= "2024-01-01 00:00") &
    (df_pv.index <= "2024-05-31 23:00")
]

# Extract PV profile for PyPSA
pv_profile = one_period["PV_pu"].values
wind_profile = one_period["Wind_pu"].values 
print("PV profile:")
print(pv_profile) 
print("Wind profile:")
print(wind_profile) 

pv_series = pd.Series(pv_profile, index=network.snapshots)
wind_series = pd.Series(wind_profile, index=network.snapshots)

network.add(
    "Generator",
    "PV",
    bus="Supermarket Bus",
    carrier="solar",
    p_nom=500,
    p_max_pu=pv_series,
)
print(network.generators)

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
    p_nom=200,
    efficiency=0.95,
    p_min_pu=-1,
)
print(network.links)

network.add(
    "Generator",
    "Wind",
    bus="Supermarket Bus",
    carrier="wind",
    p_nom=120,
    p_max_pu=wind_series,
)
print(network.generators)
print("Generators:", network.generators.index.tolist())

network.sanitize()
network.optimize()

print("Objective value:", network.objective)
print("Generators:")
print(network.generators)

print("Dispatch:")
print(network.generators_t.p)

print("Status:")
print(network.model.status)
print("Termination condition:")
print(network.model.termination_condition)


print("Objective value:", network.objective)
results = pd.DataFrame({
    "PV Power": network.generators_t.p["PV"],
    "Wind Power": network.generators_t.p["Wind"],
    "Grid Power": network.generators_t.p["Grid"],
    "EV Load": network.loads_t.p["EV Load"],
    "Battery SOC": network.stores_t.e["Battery"],
    "Battery Charger": network.links_t.p0["Battery Charger"]
})

print(results)
results.to_csv("simulation_results11.csv")
print("Simulation results saved successfully!") 
