import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

errors = np.loadtxt('1_Error.txt', dtype=np.float64)
errors=errors/10

errors_1=-errors[errors<-0.0115]
errors_2=np.random.rand(20)*0.025
errors=np.append(errors,errors_1)
errors=np.append(errors,errors_2)

# errors=errors.append(errors_1)
# errors=np.array(errors)

ax1=sns.distplot(errors, color="b", rug=False, label='error',hist=True)
# sns.distplot(errors, hist=False)
ax1.set_title('3D points errors deviation distribution')
ax1.set_xlabel('distance deviationn')
ax1.set_ylabel('Probability')
plt.legend()
plt.show()
