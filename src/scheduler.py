import pandas as pd

machines = ["M1_Cutting", "M2_Milling", "M3_Drilling", "M4_Inspection"]

def load_jobs(file_path):
    df = pd.read_csv(file_path)
    return df

def schedule_jobs(df):
    scheduled_df = df.sort_values(
        by=["Priority", "Due_Date"],
        ascending=[True, True]
    )
    return scheduled_df

def allocate_machines(schedule):
    machine_schedule = []

    for _, job in schedule.iterrows():
        process_time = job["Process_Time"]

        for machine in machines:
            machine_schedule.append({
                "Job_ID": job["Job_ID"],
                "Machine": machine,
                "Process_Time": process_time
            })

    return pd.DataFrame(machine_schedule)

def display_schedule(schedule):
    print("\n--- Job Priority Schedule ---")
    print(schedule.to_string(index=False))

def display_machine_schedule(machine_schedule):
    print("\n--- Machine Allocation Schedule ---")
    print(machine_schedule.to_string(index=False))



    return updated_schedule, failed_machine

def insert_urgent_order(schedule):
    urgent_order = pd.DataFrame([{
        "Job_ID": "WO016",
        "Process_Time": 18,
        "Due_Date": 2,
        "Priority": 1,
        "Quantity": 200,
        "Status": "Pending"
    }])

    print("\nALERT: New urgent work order received!")

    updated_schedule = pd.concat(
        [schedule, urgent_order],
        ignore_index=True
    )

    updated_schedule = updated_schedule.sort_values(
        by=["Priority", "Due_Date"],
        ascending=[True, True]
    )
    return updated_schedule

def calculate_kpis(schedule, machine_schedule):

    total_orders = len(schedule)

    total_machine_time = machine_schedule["Process_Time"].sum()

    available_machine_time = 8 * 60 * 4   # 8-hour shift × 4 machines

    machine_utilization = (
        total_machine_time / available_machine_time
    ) * 100

    late_orders = schedule[
        schedule["Process_Time"] > (schedule["Due_Date"] * 60)
    ]

    print("\n--- KPI Dashboard ---")
    print(f"Total Work Orders: {total_orders}")
    print(f"Total Throughput: {total_orders}")
    print(f"Machine Utilization: {machine_utilization:.2f}%")
    print(f"Late Orders: {len(late_orders)}")

def detect_health_based_failure(df):
    risky_machines = df[df["Machine_Health"] < 50]

    if risky_machines.empty:
        print("\nNo machine failure risk detected.")
        return None

    print("\nALERT: Machine failure risk detected!")

    print(risky_machines[
        ["Work_Order_ID", "Machine", "Machine_Health"]
    ])

    return risky_machines
def reroute_risky_operations(df):
    rerouted_df = df.copy()

    risky_rows = rerouted_df["Machine_Health"] < 50

    rerouted_df.loc[
        risky_rows, "Machine"
    ] = "M2_Backup_Milling"

    print("\nAutomatic rerouting completed!")

    print(rerouted_df[
        ["Work_Order_ID", "Machine", "Machine_Health"]
    ])

    return rerouted_df

def export_updated_schedule(df):
    df.to_csv(
        "data/updated_shopfloor_schedule.csv",
        index=False
    )

    print("\nUpdated schedule exported successfully!")