# test-001-2l

## 项目简介
本项目包含一个灵活的 Java 加法计算器，支持任意两个整数的加法运算，默认演示 `1 + 2 = 3`。

## 文件结构
- `FlexibleAddition.java` - 主程序文件，包含灵活的加法计算方法
- `SimpleAddition.java` - 基础版本，仅实现固定的 1+2=3 功能
- `README.md` - 项目说明文档（本文件）
- `LICENSE` - 开源许可证

## 功能特性
- ✅ **基础加法**：计算任意两个整数的和
- ✅ **可变参数**：支持多个整数同时相加
- ✅ **格式化输出**：美观打印加法表达式（如 `1 + 2 = 3`）
- ✅ **灵活调用**：可在其他程序中复用 `add()` 方法

## 快速开始

### 编译代码
```bash
javac FlexibleAddition.java
```

### 运行程序
```bash
java FlexibleAddition
```

### 预期输出
```
=== 基础演示 ===
1 + 2 = 3

=== 灵活调用 ===
5 + 7 = 12
100 + 250 = 350

=== 多数相加 ===
1 + 2 + 3 + 4 + 5 = 15

=== 链式计算 ===
(1 + 2) + (3 + 4) = 10
```

## 代码示例

### 基本用法
```java
int result = FlexibleAddition.add(1, 2);  // 返回 3
System.out.println("1 + 2 = " + result);
```

### 多数相加
```java
int sum = FlexibleAddition.add(1, 2, 3, 4, 5);  // 返回 15
```

### 格式化输出
```java
FlexibleAddition.printAddition(10, 20);  // 输出：10 + 20 = 30
```

## 技术栈
- **语言**：Java 8+
- **编译工具**：javac
- **运行环境**：JRE 8+

## 许可证
本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。