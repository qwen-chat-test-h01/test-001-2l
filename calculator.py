#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单计算器程序
支持加、减、乘、除四则运算
"""

def add(x, y):
    """加法"""
    return x + y

def subtract(x, y):
    """减法"""
    return x - y

def multiply(x, y):
    """乘法"""
    return x * y

def divide(x, y):
    """除法"""
    if y == 0:
        return "错误：除数不能为零！"
    return x / y

def main():
    print("=" * 40)
    print("欢迎使用简单计算器".center(40))
    print("=" * 40)
    print("\n支持的操作：")
    print("  +  加法")
    print("  -  减法")
    print("  *  乘法")
    print("  /  除法")
    print("  q  退出程序")
    print("=" * 40)
    
    while True:
        # 获取用户输入
        choice = input("\n请选择操作符 (+, -, *, /) 或输入 q 退出：").strip()
        
        # 检查是否退出
        if choice.lower() == 'q':
            print("\n感谢使用计算器，再见！")
            break
        
        # 验证操作符
        if choice not in ['+', '-', '*', '/']:
            print("无效的操作符，请重新输入！")
            continue
        
        # 获取数字
        try:
            num1 = float(input("请输入第一个数字："))
            num2 = float(input("请输入第二个数字："))
        except ValueError:
            print("无效的数字输入，请重新输入！")
            continue
        
        # 执行计算
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        
        # 显示结果
        print(f"\n结果：{num1} {choice} {num2} = {result}")

if __name__ == "__main__":
    main()
