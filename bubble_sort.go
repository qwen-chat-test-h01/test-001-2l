package main

import (
	"fmt"
)

// BubbleSort 冒泡排序算法实现
func BubbleSort(arr []int) []int {
	// 创建数组副本以避免修改原数组
	sortedArr := make([]int, len(arr))
	copy(sortedArr, arr)
	
	n := len(sortedArr)

	// 遍历所有数组元素
	for i := 0; i < n; i++ {
		// 标记是否发生了交换，用于优化
		swapped := false

		// 最后i个元素已经排好序了
		for j := 0; j < n-i-1; j++ {
			// 如果当前元素比下一个元素大，则交换
			if sortedArr[j] > sortedArr[j+1] {
				// 交换元素
				sortedArr[j], sortedArr[j+1] = sortedArr[j+1], sortedArr[j]
				swapped = true
			}
		}

		// 如果没有发生交换，说明数组已经有序
		if !swapped {
			break
		}
	}

	return sortedArr
}

// BubbleSortWithSteps 带步骤显示的冒泡排序
func BubbleSortWithSteps(arr []int) []int {
	sortedArr := make([]int, len(arr))
	copy(sortedArr, arr)
	
	n := len(sortedArr)
	
	fmt.Println("初始数组:", sortedArr)

	for i := 0; i < n; i++ {
		swapped := false
		fmt.Printf("\n第 %d 轮排序:\n", i+1)

		for j := 0; j < n-i-1; j++ {
			if sortedArr[j] > sortedArr[j+1] {
				fmt.Printf("  交换 %d 和 %d\n", sortedArr[j], sortedArr[j+1])
				// 交换元素
				sortedArr[j], sortedArr[j+1] = sortedArr[j+1], sortedArr[j]
				swapped = true
				fmt.Printf("  当前数组: %v\n", sortedArr)
			}
		}

		if !swapped {
			fmt.Println("  没有发生交换，排序完成")
			break
		} else {
			fmt.Printf("第 %d 轮结束: %v\n", i+1, sortedArr)
		}
	}

	return sortedArr
}

// PrintArray 打印数组
func PrintArray(arr []int) {
	fmt.Print("[")
	for i, v := range arr {
		fmt.Print(v)
		if i < len(arr)-1 {
			fmt.Print(", ")
		}
	}
	fmt.Println("]")
}

// 主函数，用于测试
func main() {
	fmt.Println("=== Go语言冒泡排序测试 ===")

	// 测试基本冒泡排序
	testArray := []int{64, 34, 25, 12, 22, 11, 90}
	fmt.Print("原始数组: ")
	fmt.Println(testArray)

	sortedArray := BubbleSort(testArray)
	fmt.Print("排序后数组: ")
	fmt.Println(sortedArray)

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
	result := BubbleSort(sortedTest)
	fmt.Printf("结果: %v\n", result)

	// 测试边界情况
	fmt.Println("\n测试边界情况:")
	fmt.Println("空数组排序: ", BubbleSort([]int{}))
	fmt.Println("单元素数组排序: ", BubbleSort([]int{42}))
	fmt.Println("两个元素数组排序: ", BubbleSort([]int{2, 1}))
}