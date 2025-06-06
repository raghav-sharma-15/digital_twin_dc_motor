# Digital Twin DC Motor Simulation

![MIT License](https://img.shields.io/badge/license-MIT-green)

This repository contains a modularized Python simulation of a DC motor’s degradation (health) and remaining useful life (RUL) over time, based on sensor-generated inputs. The code is organized under the `src/` directory to follow best practices in project structure.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Sensor Simulation** (`src/sensors.py`): Generates synthetic readings for load, temperature, RPM, current, noise, and vibration under different operational modes (`idle`, `active`, `stressed`).
- **Health & RUL Calculation** (`src/health_rul.py`): Computes motor health percentage, estimates remaining useful life (RUL), classifies health status (Normal/Warning/Critical), and logs maintenance events when health falls below a threshold.
- **Visualization** (`src/plotting.py`): Produces a 2×2 panel plot of motor health, temperatures, load, RPM, and current over time for easy analysis.
- **Main Script** (`src/main.py`): Orchestrates the simulation for 10,000 hours, saves results to CSV, and displays summary statistics and plots.

## Project Structure

```
digital_twin_dc_motor/
├── README.md
├── requirements.txt
├── LICENSE
├── data/
│   └── complex_digital_twin_output_10000hrs         
└── src/
    ├── sensors.py            # Sensor simulation module
    ├── health_rul.py         # Health & RUL calculation module
    ├── plotting.py           # Plotting utilities module
    └── main.py               # Main entry-point script
```

- **`README.md`**: This file.
- **`requirements.txt`**: Lists Python dependencies.
- **`LICENSE`**: MIT License file.
- **`data/`**: sample output file.
- **`src/`**: Contains all source code modules.

## Installation

1. **Clone** this repository:
   ```bash
   git clone https://github.com/<your-username>/digital_twin_dc_motor.git
   cd digital_twin_dc_motor
   ```

2. **(Optional)** Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate         # macOS/Linux
   # or venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

There are two common ways to run the simulation.

### 1. From within the `src/` directory

```bash
cd src
python main.py
```

- Generates `complex_digital_twin_output_10000hrs.csv` in `src/`.
- Displays a four-panel plot of health, temperature, load, RPM, and current over time.
- Prints any maintenance events and final health & RUL statistics to the console.

### 2. From the project root using Python’s module mode

```bash
cd digital_twin_dc_motor
python -m src.main
```

- This assumes that imports in `src/main.py` remain relative (i.e., `from sensors import ...`), allowing Python to treat `src/` as a package.

## Example Output

1. **Sample Data**:  
   - After running, you will find `src/complex_digital_twin_output_10000hrs.csv` containing all simulated sensor readings, health percentages, RUL estimates, and status labels.

2. **Plots**:  
   - A window displaying a 2×2 panel plot:
     1. Motor Health (%) vs. Time with maintenance event markers.
     2. Motor & Ambient Temperatures vs. Time.
     3. Load (%) vs. Time.
     4. RPM & Current (A) vs. Time (dual-axis).

3. **Console Summary**:
   ```
   Maintenance events occurred at the following hours:
   [1234, 3456, 6789, ...]  # examples
   Final Motor Health: XX.XX%
   Estimated RUL at final hour: YY.YY hrs
   ```

## Dependencies

- Python 3.x
- `numpy`
- `pandas`
- `matplotlib`

Install all required packages via:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes, write tests if applicable, and update the documentation.
4. Submit a pull request, describing your changes and why they improve the project.

Please follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines for Python code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full terms.

> **MIT License**
> 
> Copyright (c) 2025 Raghav Sharma
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.

## Acknowledgments

- Inspired by DC motor predictive maintenance research and digital twin frameworks.
- Data and method ideas adapted from standard reliability engineering models.
