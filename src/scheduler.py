import pandas as pd

def load_jobs(file_path):
    df = pd.read_csv(file_path)
    return df

def schedule_jobs(df):
    # Sort by Priority first, then Due Date
    scheduled_df = df.sort_values(
        by=["Priority", "Due_Date"],
        ascending=[True, True]
    )

    return scheduled_df

def display_schedule(schedule):
    print("\n--- Production Schedule ---")
    print(schedule.to_string(index=False))


if __name__ == "__main__":
    jobs = load_jobs("data/production_data.csv")
    schedule = schedule_jobs(jobs)
    display_schedule(schedule)