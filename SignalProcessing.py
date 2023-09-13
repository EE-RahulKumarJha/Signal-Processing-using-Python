import numpy as np
from scipy import signal

# Generate a test signal with noise
t = np.linspace(0, 10, 1000, endpoint=False)
x = np.sin(2*np.pi*t) + 0.5*np.random.randn(1000)

# Filter the signal using a butterworth filter
b, a = signal.butter(4, 0.2, 'lowpass')
y = signal.filtfilt(b, a, x)

# Compute the power spectral density of the filtered signal
f, Pxx = signal.welch(y, fs=100)

# Plot the original signal, filtered signal, and power spectral density
import matplotlib.pyplot as plt
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(6, 10))

ax0.set_ylabel('Original signal')
ax1.plot(t, y)
ax1.set_ylabel('Filtered signal')
ax2.semilogy(f, Pxx)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('PSD')
plt.show()
