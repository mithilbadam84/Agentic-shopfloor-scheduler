# Agentic Shopfloor Scheduler for Manufacturing

## Overview

This project simulates an intelligent manufacturing scheduling system that combines production planning, machine health monitoring, autonomous decision-making, and industrial KPI visualization.

The system mimics real-world ERP and MES workflows by using production execution data to monitor machine conditions, detect risks, reroute work orders, and evaluate operational KPIs.

## Problem Statement

In manufacturing environments, unexpected machine failures, rework loops, and urgent work orders can disrupt production schedules, reduce throughput, and increase delays.

Traditional static scheduling systems struggle to adapt to dynamic shopfloor conditions.

This project demonstrates an agentic AI-based scheduling approach capable of:

* detecting machine failure risks
* autonomously rerouting production operations
* monitoring production KPIs
* visualizing operational performance

## System Architecture

Simulated ERP/MES Data (CSV)
↓
Python Scheduling Engine
↓
Health-Based Risk Detection
↓
Autonomous Work Order Rerouting
↓
KPI Calculation
↓
Power BI Dashboard

## Features

* Dynamic production scheduling
* Machine allocation logic
* Health-based predictive maintenance
* Autonomous rerouting of risky operations
* KPI monitoring:

  * active work orders
  * average machine health
  * total production load
  * rework operations
* Power BI industrial dashboard
* Risk monitoring table for critical machines

## Tech Stack

* Python
* Pandas
* Power BI
* CSV-based simulated ERP/MES data

## Project Workflow

1. Load shopfloor production data
2. Detect risky machines using health thresholds
3. Identify affected work orders
4. Automatically reroute operations to backup machines
5. Calculate operational KPIs
6. Export updated schedule
7. Visualize shopfloor insights in Power BI

## Example Scenario

Machine:
M2_Milling

Health Score:
42%

System Action:
Work Order WO003 automatically rerouted to:

M2_Backup_Milling

## Dashboard KPIs

* Active Orders
* Average Machine Health
* Total Production Load
* Rework Operations
* Critical Machine Risk Monitor
* Machine Workload Distribution

## How to Run This Project

### 1. Clone the repository

```bash
git clone <your-github-repo-link>
cd agentic-shopfloor-scheduler
```

---

### 2. Install dependencies

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install required packages:

```bash
pip install pandas
```

---

### 3. Prepare shopfloor data

Inside the `data/` folder, create:

```text
shopfloor_schedule.csv
```

This file simulates ERP/MES production execution data.

Required columns:

* Work_Order_ID
* Machine
* Setup_Time
* Process_Time
* Queue_Time
* Start_Time
* End_Time
* Shift
* Machine_Health
* Rework_Flag
* Priority
* Due_Date
* Status

---

### 4. Run the scheduling engine

Execute:

```bash
python main.py
```

The system will:

✅ Load production execution data
✅ Detect risky machines
✅ Identify machine health below threshold
✅ Automatically reroute work orders to backup machines
✅ Calculate production KPIs
✅ Export updated schedule

Generated output:

```text
data/updated_shopfloor_schedule.csv
```

---

### 5. Open Power BI dashboard

Import:

```text
data/updated_shopfloor_schedule.csv
```

into Power BI.

Recommended dashboard components:

* KPI cards
* Machine workload chart
* Critical machine risk monitor
* Work-order slicers
* Machine slicers
* Shift filters

---

## Build Your Own Version

Want to customize?

You can extend the project by:

* Adding new machines
* Changing machine health thresholds
* Creating multiple shifts
* Simulating urgent work orders
* Adding rework loops
* Expanding machine routing logic
* Integrating live sensor data

Example:

Change health threshold:

```python
if Machine_Health < 50:
```

to:

```python
if Machine_Health < 60:
```

to make the system more sensitive.



## Future Improvements

* Live IoT sensor integration
* Reinforcement learning-based scheduling
* Multi-machine balancing
* Energy consumption optimization
* Scrap rate prediction
* Shift-level scheduling
* Real-time MES integration
* Dynamic shift balancing



