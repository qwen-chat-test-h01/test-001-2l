<?php
/**
 * 冒泡排序算法实现
 * @param array $arr 待排序的数组
 * @return array 排序后的数组
 */
function bubbleSort($arr) {
    $n = count($arr);

    // 遍历所有数组元素
    for ($i = 0; $i < $n; $i++) {
        // 标记是否发生了交换，用于优化
        $swapped = false;

        // 最后i个元素已经排好序了
        for ($j = 0; $j < $n - $i - 1; $j++) {
            // 如果当前元素比下一个元素大，则交换
            if ($arr[$j] > $arr[$j + 1]) {
                // 交换元素
                $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $temp;
                $swapped = true;
            }
        }

        // 如果没有发生交换，说明数组已经有序
        if (!$swapped) {
            break;
        }
    }

    return $arr;
}

/**
 * 带步骤显示的冒泡排序
 * @param array $arr 待排序的数组
 * @return array 排序后的数组
 */
function bubbleSortWithSteps($arr) {
    $n = count($arr);
    echo "初始数组: [" . implode(", ", $arr) . "]\n";

    for ($i = 0; $i < $n; $i++) {
        $swapped = false;
        echo "\n第 " . ($i + 1) . " 轮排序:\n";

        for ($j = 0; $j < $n - $i - 1; $j++) {
            if ($arr[$j] > $arr[$j + 1]) {
                echo "  交换 {$arr[$j]} 和 {$arr[$j + 1]}\n";
                // 交换元素
                $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $temp;
                $swapped = true;
                echo "  当前数组: [" . implode(", ", $arr) . "]\n";
            }
        }

        if (!$swapped) {
            echo "  没有发生交换，排序完成\n";
            break;
        } else {
            echo "第 " . ($i + 1) . " 轮结束: [" . implode(", ", $arr) . "]\n";
        }
    }

    return $arr;
}

/**
 * 打印数组
 * @param array $arr 要打印的数组
 */
function printArray($arr) {
    echo "[" . implode(", ", $arr) . "]\n";
}

// 测试用例
echo "=== PHP冒泡排序测试 ===\n";

// 测试基本冒泡排序
$testArray = [64, 34, 25, 12, 22, 11, 90];
echo "原始数组: ";
printArray($testArray);

$sortedArray = bubbleSort($testArray);
echo "排序后数组: ";
printArray($sortedArray);

echo "\n" . str_repeat("=", 50) . "\n";

// 测试带步骤显示的冒泡排序
$testArray2 = [64, 34, 25, 12, 22, 11, 90];
bubbleSortWithSteps($testArray2);

echo "\n" . str_repeat("=", 50) . "\n";

// 测试已经排序的数组（验证优化效果）
$sortedTest = [1, 2, 3, 4, 5];
echo "\n已排序数组测试: [" . implode(", ", $sortedTest) . "]\n";
$result = bubbleSort($sortedTest);
echo "结果: [" . implode(", ", $result) . "]\n";

// 测试边界情况
echo "\n测试边界情况:\n";
echo "空数组排序: ";
printArray(bubbleSort([]));
echo "单元素数组排序: ";
printArray(bubbleSort([42]));
echo "两个元素数组排序: ";
printArray(bubbleSort([2, 1]));

// 测试字符串数组
echo "\n字符串数组排序: ";
$stringArray = ["banana", "apple", "cherry", "date"];
printArray(bubbleSort($stringArray));
?>