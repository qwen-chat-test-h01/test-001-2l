import Foundation

/**
 * 冒泡排序算法实现
 * - Parameter arr: 待排序的数组
 * - Returns: 排序后的数组
 */
func bubbleSort(_ arr: [Int]) -> [Int] {
    // 创建数组副本以避免修改原数组
    var sortedArr = arr
    let n = sortedArr.count

    // 遍历所有数组元素
    for i in 0..<n {
        // 标记是否发生了交换，用于优化
        var swapped = false

        // 最后i个元素已经排好序了
        for j in 0..<(n - i - 1) {
            // 如果当前元素比下一个元素大，则交换
            if sortedArr[j] > sortedArr[j + 1] {
                // 交换元素
                sortedArr.swapAt(j, j + 1)
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

/**
 * 带步骤显示的冒泡排序
 * - Parameter arr: 待排序的数组
 * - Returns: 排序后的数组
 */
func bubbleSortWithSteps(_ arr: [Int]) -> [Int] {
    var sortedArr = arr
    let n = sortedArr.count
    
    print("初始数组: \(sortedArr)")

    for i in 0..<n {
        var swapped = false
        print("\n第 \(i + 1) 轮排序:")

        for j in 0..<(n - i - 1) {
            if sortedArr[j] > sortedArr[j + 1] {
                print("  交换 \(sortedArr[j]) 和 \(sortedArr[j + 1])")
                // 交换元素
                sortedArr.swapAt(j, j + 1)
                swapped = true
                print("  当前数组: \(sortedArr)")
            }
        }

        if !swapped {
            print("  没有发生交换，排序完成")
            break
        } else {
            print("第 \(i + 1) 轮结束: \(sortedArr)")
        }
    }

    return sortedArr
}

/**
 * 打印数组
 * - Parameter arr: 要打印的数组
 */
func printArray(_ arr: [Int]) {
    print("[\(arr.map(String.init).joined(separator: ", "))]")
}

// 测试用例
print("=== Swift冒泡排序测试 ===")

// 测试基本冒泡排序
let testArray = [64, 34, 25, 12, 22, 11, 90]
print("原始数组: ", terminator: "")
printArray(testArray)

let sortedArray = bubbleSort(testArray)
print("排序后数组: ", terminator: "")
printArray(sortedArray)

print()
for _ in 0..<50 {
    print("=", terminator: "")
}
print()

// 测试带步骤显示的冒泡排序
let testArray2 = [64, 34, 25, 12, 22, 11, 90]
_ = bubbleSortWithSteps(testArray2)

print()
for _ in 0..<50 {
    print("=", terminator: "")
}
print()

// 测试已经排序的数组（验证优化效果）
let sortedTest = [1, 2, 3, 4, 5]
print("\n已排序数组测试: \(sortedTest)")
let result = bubbleSort(sortedTest)
print("结果: \(result)")

// 测试边界情况
print("\n测试边界情况:")
print("空数组排序: \(bubbleSort([]))")
print("单元素数组排序: \(bubbleSort([42]))")
print("两个元素数组排序: \(bubbleSort([2, 1]))")

// 泛型版本的冒泡排序，支持遵循Comparable协议的任意类型
func genericBubbleSort<T: Comparable>(_ arr: [T]) -> [T] {
    var sortedArr = arr
    let n = sortedArr.count

    for i in 0..<n {
        var swapped = false

        for j in 0..<(n - i - 1) {
            if sortedArr[j] > sortedArr[j + 1] {
                sortedArr.swapAt(j, j + 1)
                swapped = true
            }
        }

        if !swapped {
            break
        }
    }

    return sortedArr
}

// 测试字符串数组
let stringArray = ["banana", "apple", "cherry", "date"]
print("\n字符串数组排序: \(genericBubbleSort(stringArray))")