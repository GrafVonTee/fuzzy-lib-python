from fuzzy_lib.term import Gaussian
import numpy as np
import matplotlib.pyplot as plt

x_array = np.arange(0, 300+1)

thurst_low = Gaussian("low", 0, 300, 0, 65)
thurst_low.make_range()

thurst_mid = Gaussian("mid", 0, 300, 150, 65)
thurst_mid.make_range()

thurst_high = Gaussian("high", 0, 300, 300, 65)
thurst_high.make_range()

plt.plot(x_array, thurst_low.value_range, label=thurst_low.name)
plt.plot(x_array, thurst_mid.value_range, label=thurst_mid.name)
plt.plot(x_array, thurst_high.value_range, label=thurst_high.name)

plt.legend()
plt.show()
