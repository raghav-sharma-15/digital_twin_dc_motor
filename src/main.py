import pandas as pd
from sensors import generate_operational_modes, simulate_sensor_inputs
from health_rul import calculate_health_and_rul
from plotting import plot_results

# =========================
# MAIN SCRIPT
# =========================

def main():
    # 1. INITIAL SETUP & PARAMETERS
    SIM_HOURS = 10000  # Simulation duration in hours

    # Generate time array and operational modes
    time, modes = generate_operational_modes(SIM_HOURS)

    # 2. SIMULATE SENSOR INPUTS
    load, ambient_temp, motor_temp, rpm, current, noise, vibration = simulate_sensor_inputs(time, modes)

    # 3. CALCULATE HEALTH AND RUL
    health, rul, statuses, maintenance_events = calculate_health_and_rul(
        time, load, ambient_temp, motor_temp, rpm, current, noise, vibration
    )

    # 4. COMPILE RESULTS INTO A DATAFRAME AND SAVE
    df = pd.DataFrame({
        'Time (hrs)': time,
        'Mode': modes,
        'Load (%)': load,
        'Ambient Temp (°C)': ambient_temp,
        'Motor Temp (°C)': motor_temp,
        'RPM': rpm,
        'Current (A)': current,
        'Noise (dB)': noise,
        'Vibration': vibration,
        'Health (%)': health,
        'RUL (hrs)': rul,
        'Status': statuses
    })

    # Save the simulation data to CSV for later analysis or documentation
    df.to_csv("complex_digital_twin_output_10000hrs.csv", index=False)

    # 5. MULTI-PANEL VISUALIZATION OF RESULTS
    plot_results(time, health, maintenance_events, ambient_temp, motor_temp, load, rpm, current)

    # 6. PRINT SUMMARY OF RESULTS
    if maintenance_events:
        print("Maintenance events occurred at the following hours:")
        print(maintenance_events)
    else:
        print("No maintenance events were triggered during the simulation.")

    print(f"\nFinal Motor Health: {health[-1]:.2f}%")
    print(f"Estimated RUL at final hour: {rul[-1]:.2f} hrs")

if __name__ == "__main__":
    main()