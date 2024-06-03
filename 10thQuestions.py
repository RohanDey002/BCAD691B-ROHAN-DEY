from collections import Counter

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Data
data = [17, 21, 22, 22, 26, 30, 38, 59, 67, 85]

# Mean
mean_value = np.mean(data)
print(f"Mean: {mean_value}")

# Median
median_value = np.median(data)
print(f"Median: {median_value}")

# Mode
data_counter = Counter(data)
mode_value, mode_count = data_counter.most_common(1)[0]
print(f"Mode: {mode_value} (appears {mode_count} times)")

# Box plot
plt.boxplot(data, vert=False)
plt.title('Box plot of the data')
plt.xlabel('Values')
plt.show()
