import numpy as np
import matplotlib.pyplot as plt

# 生成正弦波数据
x = np.linspace(0, 2 * np.pi, 1000)  # 从0到2π，1000个点
y = np.sin(x)  # 计算正弦值

# 创建图形
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')

# 添加标题和标签
plt.title('正弦波 (Sine Wave)', fontsize=16)
plt.xlabel('x (弧度)', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)

# 添加网格
plt.grid(True, alpha=0.3)

# 添加图例
plt.legend()

# 设置x轴刻度为π的倍数
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'])

# 设置y轴范围
plt.ylim(-1.5, 1.5)

# 保存图像
plt.savefig('sine_wave.png', dpi=300, bbox_inches='tight')

# 显示图像
plt.show()

print("正弦波图像已保存为 sine_wave.png")
