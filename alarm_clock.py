#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一个简单的闹钟小程序
功能：设置闹钟时间，到点提醒
"""

import time
import datetime
import sys
import os

def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_time():
    """获取当前时间"""
    return datetime.datetime.now()

def display_clock():
    """显示当前时间"""
    now = get_current_time()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d %A")
    
    print("\n" + "="*50)
    print(f"  当前日期: {current_date}")
    print(f"  当前时间: {current_time}")
    print("="*50)

def set_alarm():
    """设置闹钟时间"""
    print("\n--- 设置闹钟 ---")
    print("请输入闹钟时间 (格式: HH:MM 或 HH:MM:SS)")
    print("例如: 08:30 或 08:30:00")
    
    while True:
        alarm_input = input("\n闹钟时间: ").strip()
        
        try:
            # 尝试解析时间
            if len(alarm_input.split(':')) == 2:
                alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M").time()
            elif len(alarm_input.split(':')) == 3:
                alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M:%S").time()
            else:
                print("❌ 时间格式错误，请重新输入！")
                continue
            
            return alarm_time
            
        except ValueError:
            print("❌ 时间格式错误，请重新输入！")
            continue

def alarm_sound():
    """闹钟响起时的提示"""
    print("\n" + "🔔"*20)
    print("\n  ⏰ 闹钟响了！⏰")
    print("\n" + "🔔"*20)
    
    # 播放系统提示音
    if os.name == 'nt':  # Windows
        import winsound
        winsound.Beep(1000, 2000)  # 频率1000Hz，持续2秒
    else:  # Linux/Mac
        print('\a')  # 系统蜂鸣声
    
    print("\n按 Ctrl+C 停止闹钟")

def wait_for_alarm(alarm_time):
    """等待闹钟响起"""
    print(f"\n✅ 闹钟已设置为: {alarm_time.strftime('%H:%M:%S')}")
    print("按 Ctrl+C 取消闹钟\n")
    
    try:
        while True:
            current = get_current_time().time()
            
            # 显示倒计时
            display_clock()
            
            # 检查是否到达闹钟时间
            if current >= alarm_time:
                alarm_sound()
                
                # 等待用户确认
                try:
                    input("\n按 Enter 键关闭闹钟...")
                    break
                except KeyboardInterrupt:
                    break
            
            # 每秒更新一次
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n❌ 闹钟已取消")
        return False
    
    return True

def main():
    """主函数"""
    print("\n" + "="*50)
    print("         🕐 欢迎使用闹钟小程序 🕐")
    print("="*50)
    
    try:
        # 设置闹钟
        alarm_time = set_alarm()
        
        # 等待闹钟
        wait_for_alarm(alarm_time)
        
        print("\n✅ 闹钟程序结束")
        
    except KeyboardInterrupt:
        print("\n\n程序被中断")
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
    finally:
        print("\n感谢使用，再见！👋\n")

if __name__ == "__main__":
    main()
