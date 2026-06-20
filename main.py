from src.scheduler import (
    load_jobs,
    schedule_jobs,
    allocate_machines,
    display_schedule,
    display_machine_schedule,
    simulate_machine_breakdown
)

jobs = load_jobs("data/production_data.csv")

# Step 1: Prioritize jobs
schedule = schedule_jobs(jobs)
display_schedule(schedule)

# Step 2: Allocate to machines
machine_schedule = allocate_machines(schedule)
display_machine_schedule(machine_schedule)

# Step 3: Simulate machine breakdown
updated_schedule = simulate_machine_breakdown(
    machine_schedule,
    "M2_Milling"
)

print("\n--- Updated Schedule After Breakdown ---")
display_machine_schedule(updated_schedule)