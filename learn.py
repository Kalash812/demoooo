from fmpy import read_model_description, simulate_fmu
from fmpy.fmucontainer import create_fmu_container, Variable, Connection, Configuration, Component

# Configuration for FMUs
configuration = Configuration(
    components=[
        Component(filename='path_to_fmu1.fmu', name='FMU1'),
        Component(filename='path_to_fmu2.fmu', name='FMU2')
    ],
    connections=[
        Connection('FMU1', 'Voltage', 'FMU2', 'Voltage'),           # FMU1's Voltage to FMU2's Voltage
        Connection('FMU2', 'Current', 'FMU1', 'Current'),           # FMU2's Current back to FMU1's Current
    ]
)

# Create an FMU container with the configuration
filename = 'combined_model.fmu'
create_fmu_container(configuration, filename)

# Define the simulation parameters
start_time = 0
stop_time = 10
step_size = 0.1

# Simulate the combined model
result = simulate_fmu(filename, start_values={'FMU1.Current': 1.0}, stop_time=stop_time, step_size=step_size)

# Post-processing to plot results
import matplotlib.pyplot as plt
plt.plot(result['time'], result['FMU2.Output_Voltage'], label='Output Voltage from FMU2')
plt.plot(result['time'], result['FMU2.Current'], label='Current from FMU2')
plt.xlabel('Time')
plt.legend()
plt.show()
