# Python 正弦波与 SVG 图形生成项目

## 项目简介
本项目包含三个独立的示例：
1. 使用 Python 生成正弦波图像
2. 使用 SVG 绘制三维圆柱体
3. 使用 SVG 绘制三维长方体

## 文件结构
- `sine_wave.py` - Python 脚本，生成正弦波图像
- `cylinder.svg` - SVG 文件，展示三维圆柱体效果
- `cuboid.svg` - SVG 文件，展示三维长方体效果
- `README.md` - 项目说明文档（本文件）

## 功能特性

### 1. 正弦波生成 (sine_wave.py)
- ✅ **精确计算**：使用 NumPy 生成高精度的正弦波数据
- ✅ **平滑曲线**：1000 个采样点确保波形平滑
- ✅ **美观展示**：包含标题、坐标轴标签、网格和图例
- ✅ **π刻度**：x 轴以 π的倍数显示（0, π/2, π, 3π/2, 2π）
- ✅ **高清输出**：保存为 300 DPI 的 PNG 图片

### 2. SVG 圆柱体 (cylinder.svg)
- ✅ **渐变效果**：线性渐变模拟圆柱侧面光影
- ✅ **立体顶部**：径向渐变创建椭圆形顶面的立体感
- ✅ **细节丰富**：包含高光、阴影和底部轮廓线
- ✅ **矢量图形**：可无限缩放而不失真
- ✅ **浏览器兼容**：所有现代浏览器均可直接查看

### 3. SVG 长方体 (cuboid.svg)
- ✅ **三面透视**：展示顶面、左侧面和右侧面三个可见面
- ✅ **光影效果**：每个面使用不同的线性渐变模拟光照
- ✅ **立体边缘**：强调边缘线增强三维立体感
- ✅ **矢量图形**：可无限缩放而不失真
- ✅ **浏览器兼容**：所有现代浏览器均可直接查看

## 快速开始

### 运行正弦波脚本
```bash
# 安装依赖
pip install numpy matplotlib

# 运行脚本
python sine_wave.py
```

**预期输出：**
```
正弦波图像已保存为 sine_wave.png
```

### 查看圆柱体
直接用浏览器打开 `cylinder.svg` 文件即可查看效果。

### 查看长方体
直接用浏览器打开 `cuboid.svg` 文件即可查看效果。

## 代码示例

### 正弦波核心代码
```python
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

# 绘制图形
plt.plot(x, y, 'b-', linewidth=2)
plt.savefig('sine_wave.png', dpi=300)
```

### SVG 圆柱体核心代码
```svg
<!-- 圆柱体主体 -->
<rect x="75" y="100" width="150" height="250" 
      fill="url(#cylinderGradient)"/>

<!-- 顶部椭圆 -->
<ellipse cx="150" cy="100" rx="75" ry="30" 
         fill="url(#topGradient)"/>
```

### SVG 长方体核心代码
```svg
<!-- 左侧面 (平行四边形) -->
<polygon points="0,60 80,20 80,140 0,180" 
         fill="url(#leftGradient)"/>

<!-- 右侧面 (平行四边形) -->
<polygon points="80,20 200,60 200,180 80,140" 
         fill="url(#rightGradient)"/>

<!-- 顶面 (平行四边形) -->
<polygon points="0,60 80,20 200,60 120,100" 
         fill="url(#topGradient)"/>
```

## 依赖项

### Python 环境
```bash
pip install numpy matplotlib
```

### 浏览器
任何现代浏览器（Chrome、Firefox、Edge、Safari 等）均可查看 SVG 文件。

## 输出文件
- `sine_wave.png` - 生成的正弦波图像（PNG 格式，300 DPI）
- `cylinder.svg` - SVG 圆柱体矢量图形
- `cuboid.svg` - SVG 长方体矢量图形

## 技术栈
- **Python**: 用于科学计算和可视化
- **NumPy**: 数值计算库
- **Matplotlib**: 绘图库
- **SVG**: 可缩放矢量图形标准

## 许可证
本项目采用 MIT 许可证。