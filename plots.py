import matplotlib.pyplot as plt
import pandas as pd

results = pd.read_csv(
    r"C:\Users\user\Desktop\newpypsa\simulation_results06.csv",
    index_col=0,
    parse_dates=True
)

# -----------------------------
# 1. PV, Grid and Load
# -----------------------------

plt.figure(figsize=(12, 5))

plt.plot(results.index, results["PV Power"], label="PV Power")
plt.plot(results.index, results["Wind Power"], label="Wind Power")
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