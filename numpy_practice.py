import numpy as np

# : omits the start and stop slicing syntax, -1 accesses the elements in reverse order (negative indexing)
vector = np.array([1, 2, 3])
reversed_vector = vector[::-1]
print("Reversed Vector:", reversed_vector)

array = np.ones((5, 5))
array[0, :] = 0 # All of first row
array[-1, :] = 0 # All of last row
array[:, 0] = 0 # All of first column
array[:, -1] = 0 # All of last column
print("2D Array with Borders of Zeros:\n", array)

# .random implicitly generates random floating-point numbers between 0 and 1
random_array = np.random.random(10)
print(random_array)
random_array[(random_array >= 0.2) & (random_array < 0.7)] += 10
print("Modified Random Array", random_array)

# NumPy follows Banker's rounding AKA round half to even, minimising cumulative rounding errors
print("np.round(0.5):", np.round(0.5))  # Outputs 0.0
print("np.round(1.5):", np.round(1.5))  # Outputs 2.0

# np.ceil rounds to nearest integer (towards positive infinity); np.floor rounds down to nearest integer towards negative infinity
print("np.ceil(2.3):", np.ceil(2.3))    # 3.0
print("np.ceil(-2.3):", np.ceil(-2.3))  # -2.0
print("np.floor(2.3):", np.floor(2.3))  # 2.0
print("np.floor(-2.3):", np.floor(-2.3))  # -3.0

# Create a 1D array with 10 random elements and sort it
random_array = np.random.random(10)
sorted_array = np.sort(random_array)
print("Original Array:", random_array)
print("Sorted Array", sorted_array)

# Perform indirect sort
indices = np.argsort(random_array)
print("Indices for Sorted Order", indices)
# probably useful for non-parametric tests using ranks

# Create a 4x4 array of zeroes, a 4x4  array of ones, and combine them
zeroes = np.zeros((4, 4))
ones = np.ones((4, 4))

combined_horizontal = np.hstack((zeroes, ones))
print("Combined Horizontally\n", combined_horizontal)

combined_vertical = np.vstack((zeroes, ones))
print("Combined vertically\n", combined_vertical)


##
""""
Two clinicians measure the inter-pupillary distance (PD) for 100 patients in cm
Use numpy to report some statistics for this data in order to describe it
E.g. mean, standard deviation, what is the most common bin, mean disagreement
between clinicians
Find the anomalous cases where the clinicians disagree by more than 1 cm so
they can be re-evaluated
Present your findings and tell everyone what numpy functions you used for each
"""""

with open("clinician_1.txt", "r") as file:
    measurement1 = [float(x) for x in file.read().splitlines()]

# use float(x) for x in file... to cast the strings (even though they appear to be floats in the txt files) to float to prevent dtype error

with open("clinician_2.txt", "r") as file:
    measurement2 = [float(x) for x in file.read().splitlines()]

measurement1 = np.array(measurement1)
measurement2 = np.array(measurement2)

mean1 = np.mean(measurement1)
mean2 = np.mean(measurement2)
std1 = np.std(measurement1)
std2 = np.std(measurement2)

print(f"Clinician 1 - Mean: {mean1:.2f}, Standard Deviation: {std1:.2f}")
print(f"Clinician 2 - Mean: {mean2:.2f}, Standard Deviation: {std2:.2f}")

disagreement = np.abs(measurement1 - measurement2)

mean_disagreement = np.mean(disagreement)

print(f"Mean disagreement between clinicians: {mean_disagreement:.2f} cm")

# Find anomalous cases where disagreement is > 1cm
anomalous_indices = np.where(disagreement >=1)[0]

print(f"Anomalous cases where disagreement is >1cm: {anomalous_indices}")

# Finding the most common bin

hist, bin_edges = np.histogram(disagreement, bins=10)
most_common_bin = np.argmax(hist)
print(f"The most common bin for disagreements is between {bin_edges[most_common_bin]:.2f} and {bin_edges[most_common_bin + 1]:.2f} cm")