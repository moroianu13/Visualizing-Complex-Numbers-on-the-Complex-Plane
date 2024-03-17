import matplotlib.pyplot as plt
import numpy as np
import math 

# Part 1: Plotting Complex Numbers as Dots
# Generate the given list of complex numbers using list comprehension
x_values = np.arange(0, 2*math.pi, math.pi/4) 
complex_nums = [np.exp(1j*x) for x in x_values]

# Extract the real and imaginary parts of these complex numbers
real_parts = [z.real for z in complex_nums]
imaginary_parts = [z.imag for z in complex_nums]

# Use matplotlib to plot these complex numbers on the complex plane as dots
plt.figure()
plt.scatter(real_parts, imaginary_parts)
plt.title('Complex Numbers as Dots')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid(True)
plt.show()

# Part 2: Representing Complex Numbers as Vectors
# Generate the vector plot
plt.figure()
plt.quiver([0]*len(real_parts), [0]*len(imaginary_parts), real_parts, imaginary_parts, angles='xy', scale_units='xy', scale=1, color='r')
plt.title('Complex Numbers as Vectors')

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid()
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.show()