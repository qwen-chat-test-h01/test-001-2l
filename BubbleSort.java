public class BubbleSort {
    
    /**
     * 冒泡排序算法实现
     * @param arr 待排序的数组
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        
        // 遍历所有数组元素
        for (int i = 0; i < n; i++) {
            // 标记是否发生了交换，用于优化
            boolean swapped = false;
            
            // 最后i个元素已经排好序了
            for (int j = 0; j < n - i - 1; j++) {
                // 如果当前元素比下一个元素大，则交换
                if (arr[j] > arr[j + 1]) {
                    // 交换 arr[j] 和 arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
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
     * @param arr 待排序的数组
     */
    public static void bubbleSortWithSteps(int[] arr) {
        int n = arr.length;
        System.out.println("初始数组: " + arrayToString(arr));
        
        for (int i = 0; i < n; i++) {
            boolean swapped = false;
            System.out.println("\n第 " + (i + 1) + " 轮排序:");
            
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    System.out.println("  交换 " + arr[j] + " 和 " + arr[j + 1]);
                    // 交换元素
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                    System.out.println("  当前数组: " + arrayToString(arr));
                }
            }
            
            if (!swapped) {
                System.out.println("  没有发生交换，排序完成");
                break;
            } else {
                System.out.println("第 " + (i + 1) + " 轮结束: " + arrayToString(arr));
            }
        }
    }
    
    /**
     * 将数组转换为字符串格式
     * @param arr 要转换的数组
     * @return 字符串格式的数组
     */
    public static String arrayToString(int[] arr) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]);
            if (i < arr.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }
    
    /**
     * 打印数组
     * @param arr 要打印的数组
     */
    public static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    // 主方法，用于测试
    public static void main(String[] args) {
        // 测试基本冒泡排序
        int[] testArray = {64, 34, 25, 12, 22, 11, 90};
        System.out.print("原始数组: ");
        printArray(testArray);
        
        bubbleSort(testArray.clone()); // 使用clone()避免修改原数组
        int[] sortedArray = testArray.clone();
        bubbleSort(sortedArray);
        
        System.out.print("排序后数组: ");
        printArray(sortedArray);
        
        System.out.println("\n" + "=".repeat(50));
        
        // 测试带步骤显示的冒泡排序
        int[] testArray2 = {64, 34, 25, 12, 22, 11, 90};
        bubbleSortWithSteps(testArray2);
        
        System.out.println("\n" + "=".repeat(50));
        
        // 测试已经排序的数组（验证优化效果）
        int[] sortedTest = {1, 2, 3, 4, 5};
        System.out.println("\n已排序数组测试: " + arrayToString(sortedTest));
        bubbleSort(sortedTest);
        System.out.println("结果: " + arrayToString(sortedTest));
    }
}