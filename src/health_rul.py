import numpy as np

# =========================
# HEALTH DEGRADATION & RUL MODULE
# =========================

def calculate_health_and_rul(time, load, ambient_temp, motor_temp, rpm, current, noise, vibration):
    """
    Calculate health percentage, remaining useful life (RUL), status classification, and maintenance events.
    Returns:
      health: ndarray of health percentages per hour
      rul: ndarray of RUL estimates per hour
      statuses: list of status strings ('Normal', 'Warning', 'Critical') per hour
      maintenance_events: list of hours when maintenance occurred
    """
    sim_hours = len(time)

    # Initialize arrays and lists
    health = np.zeros(sim_hours)
    rul = np.zeros(sim_hours)
    statuses = []
    maintenance_events = []

    # Initial conditions
    health[0] = 100.0  # Start at full health
    rul[0] = health[0] / 0.1  # Initial RUL estimate (avoid division by zero)
    statuses.append('Normal')

    # Maintenance parameters
    maintenance_threshold = 50  # Trigger maintenance if health falls below 50%
    min_recovery = 60           # Minimum health after maintenance
    max_recovery = 90           # Maximum health after maintenance

    # Simulate degradation and perform maintenance when needed
    for i in range(1, sim_hours):
        # --- Calculate Stress Contributions ---
        # Thermal stress: only if motor temperature exceeds 60°C
        thermal_stress = max(0, motor_temp[i] - 60) * 0.05

        # Mechanical stress: contributed by vibration and noise
        mech_stress = vibration[i] * 0.1 + (noise[i] - 40) * 0.02

        # Electrical stress: penalize if current exceeds 2.5 A (quadratic penalty)
        excess_current = max(0, current[i] - 2.5)
        elec_stress = (excess_current ** 2) * 0.4

        # Combined degradation with additional random fluctuation
        degradation = thermal_stress + mech_stress + elec_stress + np.random.normal(0, 0.1)

        # Update temporary health
        temp_health = health[i - 1] - degradation

        # If the health would drop below the threshold, perform maintenance
        if temp_health < maintenance_threshold:
            # Instead of fixed recovery, use a recovery value between min_recovery and max_recovery
            recovery = np.random.uniform(min_recovery, max_recovery)
            health[i] = recovery
            maintenance_events.append(time[i])
            # Reduce maximum potential recovery slightly (simulate cumulative wear)
            max_recovery = max(min_recovery, max_recovery - 0.5)
        else:
            health[i] = temp_health

        # --- Calculate Remaining Useful Life (RUL) ---
        # Use current degradation rate to estimate RUL (if degradation is zero, carry forward previous value)
        if degradation > 0:
            rul[i] = health[i] / degradation
        else:
            rul[i] = rul[i - 1]

        # --- Health Status Classification ---
        if health[i] > 75:
            statuses.append("Normal")
        elif health[i] > 50:
            statuses.append("Warning")
        else:
            statuses.append("Critical")

    return health, rul, statuses, maintenance_events