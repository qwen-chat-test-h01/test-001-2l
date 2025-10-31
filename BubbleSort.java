public class BubbleSort {
    
    /**
     * 冒泡排序算法实现
     * @param arr 待排序的整数数组
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        
        // 外层循环控制排序轮数
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false; // 优化标志，用于检测是否发生交换
            
            // 内层循环进行相邻元素比较和交换
            for (int j = 0; j < n - i - 1; j++) {
                // 如果前一个元素大于后一个元素，则交换
                if (arr[j] > arr[j + 1]) {
                    // 交换 arr[j] 和 arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true; // 标记发生了交换
                }
            }
            
            // 如果这一轮没有发生任何交换，说明数组已经有序，可以提前结束
            if (!swapped) {
                break;
            }
        }
    }
    
    /**
     * 打印数组元素
     * @param arr 要打印的数组
     */
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();
    }
    
    /**
     * 主方法 - 用于测试冒泡排序
     */
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.println("排序前的数组:");
        printArray(arr);
        
        bubbleSort(arr);
        
        System.out.println("排序后的数组:");
        printArray(arr);
        
        // 测试边界情况
        System.out.println("\n测试边界情况:");
        
        // 测试空数组
        int[] emptyArr = {};
        System.out.print("空数组: ");
        printArray(emptyArr);
        bubbleSort(emptyArr);
        System.out.print("排序后: ");
        printArray(emptyArr);
        
        // 测试单个元素
        int[] singleArr = {42};
        System.out.print("单个元素: ");
        printArray(singleArr);
        bubbleSort(singleArr);
        System.out.print("排序后: ");
        printArray(singleArr);
        
        // 测试已排序数组
        int[] sortedArr = {1, 2, 3, 4, 5};
        System.out.print("已排序数组: ");
        printArray(sortedArr);
        bubbleSort(sortedArr);
        System.out.print("排序后: ");
        printArray(sortedArr);
        
        // 测试逆序数组
        int[] reverseArr = {5, 4, 3, 2, 1};
        System.out.print("逆序数组: ");
        printArray(reverseArr);
        bubbleSort(reverseArr);
        System.out.print("排序后: ");
        printArray(reverseArr);
    }
}