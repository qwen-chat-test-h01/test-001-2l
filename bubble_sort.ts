/**
 * 冒泡排序算法实现
 * @param arr - 待排序的数组
 * @returns 排序后的数组
 */
function bubbleSort<T>(arr: T[]): T[] {
    // 创建数组副本以避免修改原数组
    const sortedArr = [...arr];
    const n = sortedArr.length;

    // 遍历所有数组元素
    for (let i = 0; i < n; i++) {
        // 标记是否发生了交换，用于优化
        let swapped = false;

        // 最后i个元素已经排好序了
        for (let j = 0; j < n - i - 1; j++) {
            // 如果当前元素比下一个元素大，则交换
            if (sortedArr[j] > sortedArr[j + 1]) {
                // 交换元素
                [sortedArr[j], sortedArr[j + 1]] = [sortedArr[j + 1], sortedArr[j]];
                swapped = true;
            }
        }

        // 如果没有发生交换，说明数组已经有序
        if (!swapped) {
            break;
        }
    }

    return sortedArr;
}

/**
 * 带步骤显示的冒泡排序
 * @param arr - 待排序的数组
 * @returns 排序后的数组
 */
function bubbleSortWithSteps<T extends number | string>(arr: T[]): T[] {
    const sortedArr = [...arr];
    const n = sortedArr.length;
    
    console.log("初始数组:", sortedArr);

    for (let i = 0; i < n; i++) {
        let swapped = false;
        console.log(`\n第 ${i + 1} 轮排序:`);

        for (let j = 0; j < n - i - 1; j++) {
            if (sortedArr[j] > sortedArr[j + 1]) {
                console.log(`  交换 ${sortedArr[j]} 和 ${sortedArr[j + 1]}`);
                // 交换元素
                [sortedArr[j], sortedArr[j + 1]] = [sortedArr[j + 1], sortedArr[j]];
                swapped = true;
                console.log(`  当前数组: [${sortedArr.join(', ')}]`);
            }
        }

        if (!swapped) {
            console.log("  没有发生交换，排序完成");
            break;
        } else {
            console.log(`第 ${i + 1} 轮结束: [${sortedArr.join(', ')}]`);
        }
    }

    return sortedArr;
}

/**
 * 打印数组
 * @param arr - 要打印的数组
 */
function printArray<T>(arr: T[]): void {
    console.log(`[${arr.join(', ')}]`);
}

// 测试用例
console.log("=== TypeScript 冒泡排序测试 ===");

// 测试基本冒泡排序
const testArray: number[] = [64, 34, 25, 12, 22, 11, 90];
console.log("原始数组: ", testArray);

const sortedArray = bubbleSort(testArray);
console.log("排序后数组: ", sortedArray);

console.log("\n" + "=".repeat(50));

// 测试带步骤显示的冒泡排序
const testArray2: number[] = [64, 34, 25, 12, 22, 11, 90];
bubbleSortWithSteps(testArray2);

console.log("\n" + "=".repeat(50));

// 测试已经排序的数组（验证优化效果）
const sortedTest: number[] = [1, 2, 3, 4, 5];
console.log(`\n已排序数组测试: [${sortedTest.join(', ')}]`);
const result = bubbleSort(sortedTest);
console.log(`结果: [${result.join(', ')}]`);

// 测试边界情况
console.log("\n测试边界情况:");
console.log("空数组排序: ", bubbleSort([]));
console.log("单元素数组排序: ", bubbleSort([42]));
console.log("两个元素数组排序: ", bubbleSort([2, 1]));

// 测试字符串数组
const stringArray: string[] = ["banana", "apple", "cherry", "date"];
console.log("\n字符串数组排序: ", bubbleSort(stringArray));

// 性能测试
console.log("\n性能测试:");
const largeArray: number[] = Array.from({length: 1000}, () => Math.floor(Math.random() * 1000));
console.time("1000个元素排序时间");
bubbleSort(largeArray);
console.timeEnd("1000个元素排序时间");

// 导出函数，以便在其他模块中使用
export { bubbleSort, bubbleSortWithSteps, printArray };