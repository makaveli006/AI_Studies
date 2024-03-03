import numpy as np
from sklearn.utils import resample

# Original dataset
data = np.array([1, 2, 3, 4, 5])

# Resample with replacement (bootstrapping)
resampled_with_replacement = resample(data, replace=True, n_samples=10, random_state=1)

# Resample without replacement (simply shuffling the array)
resampled_without_replacement = resample(data, replace=False, n_samples=5, random_state=1)

print("Original data:", data)
print("Resampled with replacement:", resampled_with_replacement)
print("Resampled without replacement:", resampled_without_replacement)