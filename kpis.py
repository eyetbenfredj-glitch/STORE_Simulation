import pandas as pd

results = pd.read_csv(
    r"C:\Users\user\Desktop\newpypsa\simulation_results07.csv"
)

kpis = {
    "Total PV Energy (kWh)": results["PV Power"].sum(),
    "Total Wind Energy (kWh)": results["Wind Power"].sum(),
    "Total Grid Energy (kWh)": results["Grid Power"].sum(),
    "Total Load Supplied (kWh)": results["Load"].sum(),
    "Average Battery SOC (kWh)": results["Battery SOC"].mean(),
    "Battery Throughput (kWh)": results["Battery Charger"].abs().sum(),
    "Maximum Grid Power (kW)": results["Grid Power"].max(),
    "Renewable Energy Share (%)":
        (results["PV Power"].sum() + results["Wind Power"].sum())
        / results["Load"].sum() * 100
}

kpi_df = pd.DataFrame(kpis.items(), columns=["KPI", "Value"])

kpi_df.to_csv(
    r"C:\Users\user\Desktop\newpypsa\simulation_kpis07.csv",
    index=False
)

print("KPIs saved to simulation_kpis06.csv")