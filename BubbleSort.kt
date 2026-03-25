/**
 * 冒泡排序算法实现
 * @param arr 待排序的数组
 * @return 排序后的数组
 */
fun bubbleSort(arr: IntArray): IntArray {
    // 创建数组副本以避免修改原数组
    val sortedArr = arr.copyOf()
    val n = sortedArr.size

    // 遍历所有数组元素
    for (i in 0 until n) {
        // 标记是否发生了交换，用于优化
        var swapped = false

        // 最后i个元素已经排好序了
        for (j in 0 until n - i - 1) {
            // 如果当前元素比下一个元素大，则交换
            if (sortedArr[j] > sortedArr[j + 1]) {
                // 交换元素
                val temp = sortedArr[j]
                sortedArr[j] = sortedArr[j + 1]
                sortedArr[j + 1] = temp
                swapped = true
            }
        }

        // 如果没有发生交换，说明数组已经有序
        if (!swapped) {
            break
        }
    }

    return sortedArr
}

/**
 * 带步骤显示的冒泡排序
 * @param arr 待排序的数组
 * @return 排序后的数组
 */
fun bubbleSortWithSteps(arr: IntArray): IntArray {
    val sortedArr = arr.copyOf()
    val n = sortedArr.size
    
    println("初始数组: [${sortedArr.joinToString(", ")}]")

    for (i in 0 until n) {
        var swapped = false
        println("\n第 ${i + 1} 轮排序:")

        for (j in 0 until n - i - 1) {
            if (sortedArr[j] > sortedArr[j + 1]) {
                println("  交换 ${sortedArr[j]} 和 ${sortedArr[j + 1]}")
                // 交换元素
                val temp = sortedArr[j]
                sortedArr[j] = sortedArr[j + 1]
                sortedArr[j + 1] = temp
                swapped = true
                println("  当前数组: [${sortedArr.joinToString(", ")}]")
            }
        }

        if (!swapped) {
            println("  没有发生交换，排序完成")
            break
        } else {
            println("第 ${i + 1} 轮结束: [${sortedArr.joinToString(", ")}]")
        }
    }

    return sortedArr
}

/**
 * 打印数组
 * @param arr 要打印的数组
 */
fun printArray(arr: IntArray) {
    println("[${arr.joinToString(", ")}]")
}

// 主函数，用于测试
fun main() {
    println("=== Kotlin冒泡排序测试 ===")

    // 测试基本冒泡排序
    val testArray = intArrayOf(64, 34, 25, 12, 22, 11, 90)
    print("原始数组: ")
    printArray(testArray)

    val sortedArray = bubbleSort(testArray)
    print("排序后数组: ")
    printArray(sortedArray)

    println()
    repeat(50) { print("=") }
    println()

    // 测试带步骤显示的冒泡排序
    val testArray2 = intArrayOf(64, 34, 25, 12, 22, 11, 90)
    bubbleSortWithSteps(testArray2)

    println()
    repeat(50) { print("=") }
    println()

    // 测试已经排序的数组（验证优化效果）
    val sortedTest = intArrayOf(1, 2, 3, 4, 5)
    println("\n已排序数组测试: [${sortedTest.joinToString(", ")}]")
    val result = bubbleSort(sortedTest)
    println("结果: [${result.joinToString(", ")}]")

    // 测试边界情况
    println("\n测试边界情况:")
    println("空数组排序: [${bubbleSort(intArrayOf()).joinToString(", ")}]")
    println("单元素数组排序: [${bubbleSort(intArrayOf(42)).joinToString(", ")}]")
    println("两个元素数组排序: [${bubbleSort(intArrayOf(2, 1)).joinToString(", ")}]")

    // 泛型版本的冒泡排序，支持可比较的任意类型
    fun <T : Comparable<T>> genericBubbleSort(arr: Array<T>): Array<T> {
        val sortedArr = arr.clone()
        val n = sortedArr.size

        for (i in 0 until n) {
            var swapped = false

            for (j in 0 until n - i - 1) {
                if (sortedArr[j] > sortedArr[j + 1]) {
                    val temp = sortedArr[j]
                    sortedArr[j] = sortedArr[j + 1]
                    sortedArr[j + 1] = temp
                    swapped = true
                }
            }

            if (!swapped) {
                break
            }
        }

        return sortedArr
    }

    // 测试字符串数组
    val stringArray = arrayOf("banana", "apple", "cherry", "date")
    println("\n字符串数组排序: [${genericBubbleSort(stringArray).joinToString(", ")}]")
}