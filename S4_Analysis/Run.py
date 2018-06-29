# import pandas as pd
# import SpectralAnalysis

# (frequency, amplitude, phase) = SpectralAnalysis.FFT([1, 2, 3, 4, 5], 50, True)

# series = pd.Series(frequency, amplitude)
# series.plot()

# input('press <ENTER> to continue')

#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()



