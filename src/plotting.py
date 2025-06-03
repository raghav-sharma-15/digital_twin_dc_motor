import matplotlib.pyplot as plt

# =========================
# PLOTTING UTILITIES MODULE
# =========================

def plot_results(time, health, maintenance_events, ambient_temp, motor_temp, load, rpm, current):
    """
    Generate a 2x2 panel plot showing health, temperatures, load, rpm, and current over time.
    """
    fig, axs = plt.subplots(2, 2, figsize=(20, 12))

    # Panel 1: Motor Health vs. Time (with maintenance events)
    axs[0, 0].plot(time, health, label="Motor Health (%)", linewidth=2, color='blue')
    maintenance_threshold = 50  # Must match threshold used in health calculation
    axs[0, 0].axhline(
        y=maintenance_threshold,
        color='red',
        linestyle='--',
        label=f"Maintenance Threshold ({maintenance_threshold}%)"
    )
    # Mark maintenance events
    for idx, event in enumerate(maintenance_events):
        if event < len(time):
            axs[0, 0].plot(event, health[event], 'ko', markersize=6,
                           label="Maintenance Event" if idx == 0 else "")
    axs[0, 0].set_xlabel("Time (hrs)")
    axs[0, 0].set_ylabel("Health (%)")
    axs[0, 0].set_title("Motor Health Over Time")
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    # Panel 2: Temperatures vs. Time (Motor and Ambient)
    axs[0, 1].plot(time, motor_temp, label="Motor Temp (°C)", color='magenta')
    axs[0, 1].plot(time, ambient_temp, label="Ambient Temp (°C)", color='cyan')
    axs[0, 1].set_xlabel("Time (hrs)")
    axs[0, 1].set_ylabel("Temperature (°C)")
    axs[0, 1].set_title("Motor & Ambient Temperature")
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    # Panel 3: Load vs. Time
    axs[1, 0].plot(time, load, label="Load (%)", color='green')
    axs[1, 0].set_xlabel("Time (hrs)")
    axs[1, 0].set_ylabel("Load (%)")
    axs[1, 0].set_title("Load Profile Over Time")
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    # Panel 4: RPM and Current vs. Time (Dual Axis)
    ax4 = axs[1, 1]
    ax4.plot(time, rpm, label="RPM", color='orange')
    ax4.set_xlabel("Time (hrs)")
    ax4.set_ylabel("RPM", color='orange')
    ax4.set_title("RPM and Current Over Time")
    ax4.grid(True)

    # Create a twin axis for Current
    ax4b = ax4.twinx()
    ax4b.plot(time, current, label="Current (A)", color='blue', alpha=0.7)
    ax4b.set_ylabel("Current (A)", color='blue')
    ax4b.tick_params(axis='y', labelcolor='blue')

    # Legends for both axes
    ax4.legend(loc="upper left")
    ax4b.legend(loc="upper right")

    plt.tight_layout()
    plt.show()