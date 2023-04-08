import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Generate a noisy signal
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.randn(1000)

# Plot the original signal
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Apply a lowpass filter to the signal
b, a = signal.butter(4, 0.2, 'lowpass')
y = signal.filtfilt(b, a, x)

# Plot the filtered signal
plt.subplot(2, 1, 2)
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
