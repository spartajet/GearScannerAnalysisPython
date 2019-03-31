import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

errors = np.loadtxt('1_Error.txt', dtype=np.float64)
errors=errors/10

sns.distplot(errors, color="b", bins=100, rug=False, label='error')
# sns.distplot(errors, hist=False)
plt.legend()
plt.show()
