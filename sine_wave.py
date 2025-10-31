import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生成x轴数据点
x = np.linspace(0, 4*np.pi, 1000)  # 从0到4π，共1000个点

# 生成y轴数据点（正弦波）
y = np.sin(x)

# 创建图形
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)

# 添加标题和标签
plt.title('正弦波图像 (Sine Wave)', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.6)

# 添加图例
plt.legend()

# 设置x轴刻度标签为π的倍数
plt.xticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi], 
           ['0', 'π', '2π', '3π', '4π'])

# 显示图形
plt.tight_layout()
plt.savefig('/workspace/sine_wave.png', dpi=300, bbox_inches='tight')
plt.show()

print("正弦波图像已保存为 sine_wave.png")