# STORE_Simulation
# Smart Energy System Digital Twin

## Overview

This project develops a **Digital Twin simulation of a smart energy system** using **Python and PyPSA**.

The objective is to simulate energy flows between renewable generation, battery storage, electrical loads, EV charging demand, and the electrical grid. Different scenarios are evaluated to understand system performance and the impact of battery configurations and renewable energy integration.

The project focuses on **energy management and system simulation**, with the results evaluated using key performance indicators (KPIs).

## System Architecture

The simulated energy system consists of:

- Photovoltaic (PV) generation
- Wind generation
- Battery energy storage
- Electrical load
- EV charging demand
- Electrical grid

The different components are connected through the PyPSA network and simulated using time-series data.

## Project Structure
```text 
├── simulations/
│   ├── sim01.py
│   ├── sim02.py
│   ├── sim03.py
│   ├── sim04.py
│   ├── sim05.py
│   ├── sim06.py
│   ├── sim07.py
│   ├── sim08.py
│   └── sim09.py
│
├── analysis/
│   ├── kpis.py
│   ├── battery_analysis.py
│   ├── battery_sizing.py
│   ├── plots.py
│   └── plots01.py
│
├── results/
│   ├── simulation_kpis.csv
│   ├── simulation_kpis04.csv
│   ├── simulation_kpis05.csv
│   ├── simulation_kpis06.csv
│   ├── simulation_kpis07.csv
│   └── excess_analysis.csv
│
├── figures/
│   ├── Figure_1.png
│   ├── Figure_2.png
│   ├── Figure_3.png
│   ├── Battery_SOC_Day.png
│   ├── Monthly_Energy.png
│   ├── Representative_Day.png
│   └── Representative_Week.png
│
├── data.py
└── README.md
```
## Simulations

The `simulations/` directory contains the different simulation scenarios developed using PyPSA.

Each simulation investigates a specific system configuration or operating condition.

## Data Preparation

The `data.py` script is used to **inspect, configure, and prepare the input data** required by the simulations.

The original input datasets are not included in this repository.

## Analysis

The `analysis/` directory contains scripts used to evaluate the simulation results, including:

- KPI calculation
- Battery performance analysis
- Battery sizing
- Energy and system performance plots

## Key Performance Indicators

The main simulation is evaluated using the following KPIs:

- Total PV Energy (kWh)
- Total Wind Energy (kWh)
- Total Grid Energy (kWh)
- Total Load Supplied (kWh)
- Average Battery SOC (kWh)
- Battery Throughput (kWh)
- Maximum Grid Power (kW)
- Renewable Energy Share (%)

The detailed numerical results and interpretation of these KPIs are presented in the project report.

## Results

The repository includes generated figures illustrating the behavior and performance of the simulated energy system.

These include:

- Daily battery state of charge
- Monthly energy production
- Representative operating days
- Representative operating weeks
- Other system performance visualizations

The full simulation results are also stored as CSV files for reference.

## Technologies

- **Python**
- **PyPSA**
- **Pandas**
- **NumPy**
- **Matplotlib**

## Project Objective

The overall objective is to develop a simulation-based Digital Twin capable of representing the behavior of a smart energy system and evaluating different energy management scenarios.

Future developments can include integrating **AI-based forecasting** and extending the Digital Twin toward real-time monitoring and optimization.

## Author

Developed as part of an **internship project** focused on smart energy systems, energy management, and Digital Twin applications.

