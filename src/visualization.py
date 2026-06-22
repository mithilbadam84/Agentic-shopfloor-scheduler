import matplotlib.pyplot as plt

def plot_gantt_chart(machine_schedule):
    fig, ax = plt.subplots(figsize=(12, 6))

    start_time = 0

    for index, row in machine_schedule.iterrows():
        ax.barh(
            row["Machine"],
            row["Process_Time"],
            left=start_time,
            label=row["Job_ID"]
        )

        start_time += row["Process_Time"]

    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Machines")
    ax.set_title("Shopfloor Production Gantt Chart")

    plt.show()