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

def simulate_machine_breakdown(machine_schedule, failed_machine):
    print(f"\nALERT: {failed_machine} has broken down!")

    updated_schedule = machine_schedule[
        machine_schedule["Machine"] != failed_machine
    ]
    return updated_schedule