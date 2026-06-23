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

## Future Improvements

* Live IoT sensor integration
* Reinforcement learning-based scheduling
* Multi-machine balancing
* Energy consumption optimization
* Scrap rate prediction
* Shift-level scheduling
