import numpy as np
import matplotlib.pyplot as plt

# Generate x-axis data points
x = np.linspace(0, 4*np.pi, 1000)  # From 0 to 4π, with 1000 points

# Generate y-axis data points (sine wave)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)

# Add title and labels
plt.title('Sine Wave', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend
plt.legend()

# Set x-axis tick labels as multiples of π
plt.xticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi], 
           ['0', 'π', '2π', '3π', '4π'])

# Save and show the plot
plt.tight_layout()
plt.savefig('/workspace/sine_wave_simple.png', dpi=300, bbox_inches='tight')
plt.show()

print("Sine wave image has been saved as sine_wave_simple.png")