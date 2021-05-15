import math

# -----------------------------------------------------------------
# 画图基础设置
import matplotlib
import matplotlib.pyplot as plt
import random

matplotlib.use('TkAgg')  # 解决pycharm不显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.xlabel('X坐标')  # 设置X轴标签
plt.ylabel('Y坐标')  # 设置Y轴标签
plt.title('test绘图函数')  # 按需修改

# **Colors**
# The following color abbreviations are supported:
# =============    ===============================
# character        color
# =============    ===============================
# ``'b'``          blue
# ``'g'``          green
# ``'r'``          red
# ``'c'``          cyan
# ``'m'``          magenta
# ``'y'``          yellow
# ``'k'``          black
# ``'w'``          white
# =============    ===============================

# **Markers**
# =============    ===============================
# character        description
# =============    ===============================
# ``'.'``          point marker
# ``','``          pixel marker
# ``'o'``          circle marker
# ``'v'``          triangle_down marker
# ``'^'``          triangle_up marker
# ``'<'``          triangle_left marker
# ``'>'``          triangle_right marker
# ``'1'``          tri_down marker
# ``'2'``          tri_up marker
# ``'3'``          tri_left marker
# ``'4'``          tri_right marker
# ``'s'``          square marker
# ``'p'``          pentagon marker
# ``'*'``          star marker
# ``'h'``          hexagon1 marker
# ``'H'``          hexagon2 marker
# ``'+'``          plus marker
# ``'x'``          x marker
# ``'D'``          diamond marker
# ``'d'``          thin_diamond marker
# ``'|'``          vline marker
# ``'_'``          hline marker
# =============    ===============================

# **Line Styles**
# =============    ===============================
# character        description
# =============    ===============================
# ``'-'``          solid line style
# ``'--'``         dashed line style
# ``'-.'``         dash-dot line style
# ``':'``          dotted line style
# =============    ===============================
# ------------------------------------------------------------------

if __name__ == '__main__':
    # 圆形方程 : (x-a)^2 + (y-b)^2 = r^2

    a = 100
    b = 100
    r = 50

    minX = a - r
    maxX = a + r
    minY = b - r
    maxY = b + r

    # 画圆
    x = minX
    X = []
    Y = []
    while x < maxX:
        m = (r ** 2 - (x - a) ** 2) ** 0.5
        y1 = m + b
        y2 = b - m
        X.append(x)
        Y.append(y1)
        X.append(x)
        Y.append(y2)
        # plt.plot(x, y1, 'b.')
        # plt.plot(x, y2, 'b.')
        x += 0.2
    plt.plot(X,Y, 'k.')

    # 生成圆内的随机数据

    for i in range(100):
        x = random.randint(minX, maxX)
        y = random.randint(minY, maxY)
        plt.plot(x, y, 'ro')
        plt.pause(0.1)

    plt.pause(5)
