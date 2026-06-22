from src.scheduler import (
    load_jobs,
    schedule_jobs,
    allocate_machines,
    display_schedule,
    display_machine_schedule,
    insert_urgent_order,
    calculate_kpis,
    detect_health_based_failure
)
from src.visualization import plot_gantt_chart

jobs = load_jobs("data/production_data.csv")

# Step 1: Prioritize jobs
schedule = schedule_jobs(jobs)
display_schedule(schedule)

# Step 2: Allocate to machines
machine_schedule = allocate_machines(schedule)
display_machine_schedule(machine_schedule)

# Step 3: Insert urgent order
new_schedule = insert_urgent_order(schedule)
print("\n--- Updated Schedule After Urgent Order ---")
display_schedule(new_schedule)

#step 4: Re-allocate machines after inserting urgent order
machine_schedule = allocate_machines(new_schedule)
calculate_kpis(new_schedule, machine_schedule)
plot_gantt_chart(machine_schedule)

# Step 5: Detect health-based machine failure
shopfloor_data = load_jobs("data/shopfloor_schedule.csv")

risky_machines = detect_health_based_failure(shopfloor_data)
