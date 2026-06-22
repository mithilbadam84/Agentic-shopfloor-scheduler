from src.scheduler import (
    load_jobs,
    detect_health_based_failure,
    calculate_kpis,
    reroute_risky_operations,
    export_updated_schedule
)

# Load realistic shopfloor execution data
shopfloor_data = load_jobs("data/shopfloor_schedule.csv")

# Detect risky machines
risky_machines = detect_health_based_failure(shopfloor_data)

# Calculate KPIs
calculate_kpis(shopfloor_data, shopfloor_data)
# Reroute risky operations
rerouted_schedule = reroute_risky_operations(
    shopfloor_data
)
# Export the updated schedule with rerouted operations
export_updated_schedule(rerouted_schedule)