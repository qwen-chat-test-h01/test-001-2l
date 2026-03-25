#include <iostream>
#include <vector>
#include <algorithm>

class BubbleSort {
public:
    /**
     * 冒泡排序算法实现
     * @param arr 待排序的向量
     */
    static void bubbleSort(std::vector<int>& arr) {
        int n = arr.size();
        
        // 遍历所有数组元素
        for (int i = 0; i < n; i++) {
            // 标记是否发生了交换，用于优化
            bool swapped = false;
            
            // 最后i个元素已经排好序了
            for (int j = 0; j < n - i - 1; j++) {
                // 如果当前元素比下一个元素大，则交换
                if (arr[j] > arr[j + 1]) {
                    std::swap(arr[j], arr[j + 1]);
                    swapped = true;
                }
            }
            
            // 如果没有发生交换，说明数组已经有序
            if (!swapped) {
                break;
            }
        }
    }
    
    /**
     * 带步骤显示的冒泡排序
     * @param arr 待排序的向量
     */
    static void bubbleSortWithSteps(std::vector<int>& arr) {
        int n = arr.size();
        std::cout << "初始数组: ";
        printArray(arr);
        
        for (int i = 0; i < n; i++) {
            bool swapped = false;
            std::cout << "\n第 " << (i + 1) << " 轮排序:" << std::endl;
            
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    std::cout << "  交换 " << arr[j] << " 和 " << arr[j + 1] << std::endl;
                    std::swap(arr[j], arr[j + 1]);
                    swapped = true;
                    std::cout << "  当前数组: ";
                    printArray(arr);
                }
            }
            
            if (!swapped) {
                std::cout << "  没有发生交换，排序完成" << std::endl;
                break;
            } else {
                std::cout << "第 " << (i + 1) << " 轮结束: ";
                printArray(arr);
            }
        }
    }
    
    /**
     * 打印数组
     * @param arr 要打印的向量
     */
    static void printArray(const std::vector<int>& arr) {
        std::cout << "[";
        for (size_t i = 0; i < arr.size(); i++) {
            std::cout << arr[i];
            if (i < arr.size() - 1) {
                std::cout << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }
};

// 主函数，用于测试
int main() {
    // 测试基本冒泡排序
    std::vector<int> testArray = {64, 34, 25, 12, 22, 11, 90};
    std::cout << "原始数组: ";
    BubbleSort::printArray(testArray);
    
    std::vector<int> sortedArray = testArray;
    BubbleSort::bubbleSort(sortedArray);
    
    std::cout << "排序后数组: ";
    BubbleSort::printArray(sortedArray);
    
    std::cout << std::endl;
    for (int i = 0; i < 50; i++) std::cout << "=";
    std::cout << std::endl;
    
    // 测试带步骤显示的冒泡排序
    std::vector<int> testArray2 = {64, 34, 25, 12, 22, 11, 90};
    BubbleSort::bubbleSortWithSteps(testArray2);
    
    std::cout << std::endl;
    for (int i = 0; i < 50; i++) std::cout << "=";
    std::cout << std::endl;
    
    // 测试已经排序的数组（验证优化效果）
    std::vector<int> sortedTest = {1, 2, 3, 4, 5};
    std::cout << "\n已排序数组测试: ";
    BubbleSort::printArray(sortedTest);
    BubbleSort::bubbleSort(sortedTest);
    std::cout << "结果: ";
    BubbleSort::printArray(sortedTest);
    
    return 0;
}