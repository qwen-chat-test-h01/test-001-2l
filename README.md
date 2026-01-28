# SVG 圆柱体项目

## 项目简介

本项目包含一个使用 SVG 绘制的圆柱体示例。

## 文件说明

- `cylinder.svg` - 使用 SVG 绘制的圆柱体图形
- `bubble_sort.py` - Python 实现的冒泡排序算法
- `README.md` - 项目说明文档

## 圆柱体说明

`cylinder.svg` 文件包含一个 300x400 像素的圆柱体，具有：
- 蓝灰色渐变填充效果
- 阴影和高光效果
- 立体视觉呈现

您可以直接在浏览器中打开 `cylinder.svg` 查看效果。

## 使用方法

### 查看圆柱体
直接在浏览器中打开 `cylinder.svg` 文件即可查看绘制的圆柱体。

### 运行冒泡排序
```bash
python bubble_sort.py
```

## 技术实现

圆柱体使用 SVG 的以下特性：
- `<linearGradient>` 实现渐变效果
- `<ellipse>` 绘制椭圆端面
- `<path>` 绘制圆柱侧面
- 阴影和高光效果增强立体感

## 许可证

本项目遵循 MIT 许可证。详见 [LICENSE](LICENSE) 文件。