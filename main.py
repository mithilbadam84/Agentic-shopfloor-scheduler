from src.scheduler import load_jobs, schedule_jobs, display_schedule

jobs = load_jobs("data/production_data.csv")
schedule = schedule_jobs(jobs)
display_schedule(schedule)