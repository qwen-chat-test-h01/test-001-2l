package main

import (
	"fmt"
)

// BubbleSort 冒泡排序算法实现
// arr: 待排序的切片
func BubbleSort(arr []int) {
	n := len(arr)
	
	// 遍历所有数组元素
	for i := 0; i < n; i++ {
		// 标记是否发生了交换，用于优化
		swapped := false
		
		// 最后i个元素已经排好序了
		for j := 0; j < n-i-1; j++ {
			// 如果当前元素比下一个元素大，则交换
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		
		// 如果没有发生交换，说明数组已经有序
		if !swapped {
			break
		}
	}
}

// BubbleSortWithSteps 带步骤显示的冒泡排序
// arr: 待排序的切片
func BubbleSortWithSteps(arr []int) {
	n := len(arr)
	fmt.Printf("初始数组: %v\n", arr)
	
	for i := 0; i < n; i++ {
		swapped := false
		fmt.Printf("\n第 %d 轮排序:\n", i+1)
		
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				fmt.Printf("  交换 %d 和 %d\n", arr[j], arr[j+1])
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
				fmt.Printf("  当前数组: %v\n", arr)
			}
		}
		
		if !swapped {
			fmt.Println("  没有发生交换，排序完成")
			break
		} else {
			fmt.Printf("第 %d 轮结束: %v\n", i+1, arr)
		}
	}
}

// PrintArray 打印数组
// arr: 要打印的切片
func PrintArray(arr []int) {
	fmt.Printf("%v\n", arr)
}

// 主函数，用于测试
func main() {
	// 测试基本冒泡排序
	testArray := []int{64, 34, 25, 12, 22, 11, 90}
	fmt.Printf("原始数组: %v\n", testArray)
	
	sortedArray := make([]int, len(testArray))
	copy(sortedArray, testArray)
	BubbleSort(sortedArray)
	
	fmt.Printf("排序后数组: %v\n", sortedArray)
	
	fmt.Println()
	for i := 0; i < 50; i++ {
		fmt.Print("=")
	}
	fmt.Println()
	
	// 测试带步骤显示的冒泡排序
	testArray2 := []int{64, 34, 25, 12, 22, 11, 90}
	BubbleSortWithSteps(testArray2)
	
	fmt.Println()
	for i := 0; i < 50; i++ {
		fmt.Print("=")
	}
	fmt.Println()
	
	// 测试已经排序的数组（验证优化效果）
	sortedTest := []int{1, 2, 3, 4, 5}
	fmt.Printf("\n已排序数组测试: %v\n", sortedTest)
	BubbleSort(sortedTest)
	fmt.Printf("结果: %v\n", sortedTest)
}