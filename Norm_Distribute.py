import scipy.stats
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

plt.rcParams['font.family'] = 'Arial'
# matplotlib.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'# 中文设置成宋体，除此之外的字体设置成New Roman
# 创建画布
fig = plt.figure()
# 使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)

# 将绘图区对象添加到画布中
fig.add_axes(ax)
ax.axis[:].set_visible(False)

ax.axis["x"] = ax.new_floating_axis(0, 0)
ax.axis["x"].set_axisline_style("->", size=1.0)
# ax.axis["x"].set_label('deviation')
# ax.axis["x"].set_label_coords(1.05, -0.025)
ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["y"].set_axisline_style("->", size=1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("top")
ax.set_xticks([])
ax.set_yticks([])
# ax.spines['top'].set_visible(True)s
# ax.spines['right'].set_visible(True)
# ax.spines['bottom'].set_visible(True)
# ax.spines['left'].set_visible(True)


standard_norm = scipy.stats.norm(1, 1)  # 标准正态分布
x = np.arange(-3, 5, 0.01)
y = standard_norm.pdf(x)
ax.plot(x, y, label='standard distribution', color='b')
# 填充正常
ax.fill_between(x, y, where=((x >= -1) & (x <= 3)), facecolor='deepskyblue')
# 填充不正常
ax.fill_between(x, y, where=((x < -1) | (x > 3)), facecolor='r')
# 中间竖线
ax.axvline(x=1, color='r', linewidth=1, linestyle="--")
ax.set_title('3D points errors deviation distribution')
# plt.xlabel('deviation')

# 标记 x label
ax.annotate('deviation', xy=(1, 1), xytext=(480, 10), ha='left', va='top', xycoords='axes pixels',
            textcoords='axes pixels', fontsize=12)

ax.annotate('μ', xy=(0, 0), xytext=(290, 60), ha='left', va='top', xycoords='axes pixels', textcoords='axes pixels',
            fontsize=30, fontfamily='Times New Roman', fontweight='ultralight')
ax.annotate('-2σ', xy=(1, 1), xytext=(145, 10), ha='left', va='top', xycoords='axes pixels',
            textcoords='axes pixels', fontsize=12)
ax.annotate('2σ', xy=(1, 1), xytext=(400, 10), ha='left', va='top', xycoords='axes pixels',
            textcoords='axes pixels', fontsize=12)
# ax.annotate('deviation', xy=(0, 1), xytext=(15,2), ha='left', va='top', xycoords='axes fraction', textcoords='offset points', fontsize=20)

ax.legend()
plt.show()
