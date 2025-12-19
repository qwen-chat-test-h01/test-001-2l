/**
 * 冒泡排序算法实现 (JavaScript版)
 */

/**
 * 冒泡排序 - 返回新数组
 * @param {number[]} arr - 待排序的数组
 * @returns {number[]} 排序后的新数组
 */
function bubbleSort(arr) {
    // 创建数组的副本，避免修改原数组
    const sortedArr = [...arr];
    const n = sortedArr.length;
    
    // 外层循环控制排序轮数
    for (let i = 0; i < n; i++) {
        // 标记本轮是否发生交换，用于优化
        let swapped = false;
        
        // 内层循环进行相邻元素比较和交换
        // 每轮结束后最大元素会"冒泡"到末尾，所以范围逐渐缩小
        for (let j = 0; j < n - i - 1; j++) {
            // 如果前一个元素大于后一个元素，则交换
            if (sortedArr[j] > sortedArr[j + 1]) {
                [sortedArr[j], sortedArr[j + 1]] = [sortedArr[j + 1], sortedArr[j]];
                swapped = true;
            }
        }
        
        // 如果本轮没有发生交换，说明数组已经有序，可以提前结束
        if (!swapped) {
            break;
        }
    }
    
    return sortedArr;
}

/**
 * 冒泡排序 - 原地排序（修改原数组）
 * @param {number[]} arr - 待排序的数组
 * @returns {void}
 */
function bubbleSortInPlace(arr) {
    const n = arr.length;
    
    for (let i = 0; i < n; i++) {
        let swapped = false;
        
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
        }
    }
}

// 示例用法和测试
console.log("=== JavaScript 冒泡排序示例 ===");

// 测试数据
const testArray = [64, 34, 25, 12, 22, 11, 90];
console.log("原始数组:", testArray);

// 使用非原地排序
const sortedArray = bubbleSort(testArray);
console.log("排序后数组:", sortedArray);

// 使用原地排序
const testArray2 = [64, 34, 25, 12, 22, 11, 90];
console.log("\n原始数组:", testArray2);
bubbleSortInPlace(testArray2);
console.log("原地排序后:", testArray2);

// 额外测试用例
console.log("\n其他测试用例:");
console.log("空数组:", bubbleSort([]));
console.log("单个元素:", bubbleSort([1]));
console.log("已排序数组:", bubbleSort([1, 2, 3, 4, 5]));
console.log("逆序数组:", bubbleSort([5, 4, 3, 2, 1]));
console.log("有重复元素:", bubbleSort([3, 1, 4, 1, 5, 9, 2, 6, 5]));

// 性能提示信息
console.log("\n算法复杂度:");
console.log("- 时间复杂度: 最好 O(n)，平均和最坏 O(n²)");
console.log("- 空间复杂度: O(1)");
console.log("- 稳定性: 稳定");