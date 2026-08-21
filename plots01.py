import pandas as pd
import matplotlib.pyplot as plt

results = pd.read_csv(
    r"C:\Users\user\Desktop\newpypsa\simulation_results07.csv",
    index_col="snapshot",
    parse_dates=True
)
#Representative Day (24 hours) 
day = results.loc["2022-06-15"]

plt.figure(figsize=(12,5))

plt.plot(day.index, day["PV Power"], label="PV")
plt.plot(day.index, day["Wind Power"], label="Wind")
plt.plot(day.index, day["Grid Power"], label="Grid")
plt.plot(day.index, day["Load"], label="Load")

plt.title("Power Flows on 15 June 2022")
plt.xlabel("Time")
plt.ylabel("Power (kW)")
plt.grid(True)
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    r"C:\Users\user\Desktop\newpypsa\Representative_Day.png",
    dpi=300
)

plt.show()
plt.close()

#Representative Week
week = results.loc["2022-06-15":"2022-06-22"]

plt.figure(figsize=(13,5))

plt.plot(week.index, week["PV Power"], label="PV")
plt.plot(week.index, week["Wind Power"], label="Wind")
plt.plot(week.index, week["Grid Power"], label="Grid")
plt.plot(week.index, week["Load"], label="Load")

plt.title("Power Flows During One Week")
plt.xlabel("Date")
plt.ylabel("Power (kW)")
plt.grid(True)
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    r"C:\Users\user\Desktop\newpypsa\Representative_Week.png",
    dpi=300
)

plt.show()
plt.close()

#Monthly Energy
monthly = results.resample("M").sum()

plt.figure(figsize=(14,5))

plt.plot(monthly.index, monthly["PV Power"], label="PV")
plt.plot(monthly.index, monthly["Wind Power"], label="Wind")
plt.plot(monthly.index, monthly["Grid Power"], label="Grid")
plt.plot(monthly.index, monthly["Load"], label="Load")

plt.title("Monthly Energy")
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    r"C:\Users\user\Desktop\newpypsa\Monthly_Energy.png",
    dpi=300
)

plt.show()
plt.close()

#Battery SOC
day = results.loc["2022-06-15"]

plt.figure(figsize=(12,4))

plt.plot(day.index, day["Battery SOC"])

plt.title("Battery State of Charge Flows on 15 June 2022")
plt.xlabel("Time")
plt.ylabel("SOC (kWh)")
plt.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    r"C:\Users\user\Desktop\newpypsa\Battery_SOC_Day.png",
    dpi=300
)

plt.show()
plt.close()