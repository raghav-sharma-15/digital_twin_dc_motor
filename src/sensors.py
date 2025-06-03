import numpy as np

# =========================
# SENSOR SIMULATION MODULE
# =========================

def generate_operational_modes(sim_hours, seed=42):
    """
    Generate time array and randomly assigned operational modes for each hour.
    """
    np.random.seed(seed)
    time = np.arange(sim_hours)
    modes = np.random.choice(['idle', 'active', 'stressed'], sim_hours, p=[0.2, 0.6, 0.2])
    return time, modes

def simulate_sensor_inputs(time, modes):
    """
    Simulate sensor inputs (load, temperatures, rpm, current, noise, vibration) based on operational modes.
    """
    sim_hours = len(time)

    # Mode-specific parameters: ranges/values vary per mode
    mode_params = {
        'idle': {
            'load_range': (20, 30),
            'temp_rise': 2,             # Temperature rise (°C) above ambient
            'vibration_base': 0.1,      # Base vibration amplitude
            'noise_base': 40            # Base noise level (dB)
        },
        'active': {
            'load_range': (40, 70),
            'temp_rise': 5,
            'vibration_base': 0.5,
            'noise_base': 45
        },
        'stressed': {
            'load_range': (70, 100),
            'temp_rise': 8,
            'vibration_base': 0.9,
            'noise_base': 50
        }
    }

    # Initialize lists for each parameter
    load = []
    ambient_temp = []
    motor_temp = []
    rpm = []
    current = []
    noise = []
    vibration = []

    # Generate sensor readings for each hour using the mode parameters
    for i in range(sim_hours):
        mode = modes[i]
        params = mode_params[mode]

        # Load (%) within the mode's range
        base_load = np.random.uniform(*params['load_range'])
        load.append(base_load)

        # Ambient temperature (°C) uniformly between 25 and 40
        amb_temp = np.random.uniform(25, 40)
        ambient_temp.append(amb_temp)

        # Motor temperature: ambient plus mode-specific rise and some noise
        mot_temp = amb_temp + params['temp_rise'] + np.random.normal(0, 1)
        motor_temp.append(mot_temp)

        # RPM: centered around 1400, influenced by load and random noise
        motor_rpm = 1400 + (base_load - 50) * 5 + np.random.normal(0, 15)
        rpm.append(motor_rpm)

        # Current draw (A): base value increases with load
        motor_current = 1.2 + (base_load / 100) * 3.0 + np.random.normal(0, 0.1)
        current.append(motor_current)

        # Noise level (dB): determined by the mode with added randomness
        motor_noise = params['noise_base'] + np.random.normal(0, 1)
        noise.append(motor_noise)

        # Vibration: base level with small random fluctuations
        motor_vibration = params['vibration_base'] + np.random.normal(0, 0.1)
        vibration.append(motor_vibration)

    return load, ambient_temp, motor_temp, rpm, current, noise, vibration