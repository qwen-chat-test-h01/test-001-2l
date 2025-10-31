public class BubbleSortWithValidation {
    
    /**
     * 验证字符串数组中的所有元素是否为数字
     * @param arr 待验证的字符串数组
     * @return 如果所有元素都是数字则返回true，否则返回false
     */
    public static boolean areAllElementsNumbers(String[] arr) {
        if (arr == null) {
            return false;
        }
        
        for (String element : arr) {
            if (!isNumber(element)) {
                return false;
            }
        }
        return true;
    }
    
    /**
     * 检查单个字符串是否表示一个数字
     * @param str 待检查的字符串
     * @return 如果是数字则返回true，否则返回false
     */
    public static boolean isNumber(String str) {
        if (str == null || str.trim().isEmpty()) {
            return false;
        }
        
        try {
            Double.parseDouble(str.trim());
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    
    /**
     * 对数字字符串数组进行冒泡排序
     * @param arr 包含数字字符串的数组
     * @return 排序成功返回true，如果数组包含非数字元素则返回false
     */
    public static boolean bubbleSort(String[] arr) {
        // 首先验证数组中的所有元素是否为数字
        if (!areAllElementsNumbers(arr)) {
            System.out.println("错误：数组中包含非数字元素");
            return false;
        }
        
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                // 将字符串转换为数字进行比较
                double num1 = Double.parseDouble(arr[j]);
                double num2 = Double.parseDouble(arr[j + 1]);
                
                if (num1 > num2) {
                    // 交换元素
                    String temp = arr[j];
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
        return true;
    }
    
    /**
     * 打印数组元素
     * @param arr 要打印的数组
     */
    public static void printArray(String[] arr) {
        if (arr == null || arr.length == 0) {
            System.out.println("[]");
            return;
        }
        
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    /**
     * 主方法 - 测试函数
     */
    public static void main(String[] args) {
        // 测试用例1：有效的数字数组
        System.out.println("测试用例1：有效数字数组");
        String[] arr1 = {"64", "34", "25", "12", "22", "11", "90"};
        System.out.print("排序前: ");
        printArray(arr1);
        if (bubbleSort(arr1)) {
            System.out.print("排序后: ");
            printArray(arr1);
        }
        System.out.println();
        
        // 测试用例2：包含非数字元素的数组
        System.out.println("测试用例2：包含非数字元素的数组");
        String[] arr2 = {"64", "34", "abc", "12", "22"};
        System.out.print("原数组: ");
        printArray(arr2);
        boolean result2 = bubbleSort(arr2);
        System.out.println("排序结果: " + result2);
        System.out.println();
        
        // 测试用例3：包含小数的数组
        System.out.println("测试用例3：包含小数的数组");
        String[] arr3 = {"3.14", "2.71", "1.41", "4.67", "2.23"};
        System.out.print("排序前: ");
        printArray(arr3);
        if (bubbleSort(arr3)) {
            System.out.print("排序后: ");
            printArray(arr3);
        }
        System.out.println();
        
        // 测试用例4：包含负数的数组
        System.out.println("测试用例4：包含负数的数组");
        String[] arr4 = {"-5", "3", "-1", "8", "0", "-10"};
        System.out.print("排序前: ");
        printArray(arr4);
        if (bubbleSort(arr4)) {
            System.out.print("排序后: ");
            printArray(arr4);
        }
        System.out.println();
        
        // 测试用例5：空数组
        System.out.println("测试用例5：空数组");
        String[] arr5 = {};
        System.out.print("原数组: ");
        printArray(arr5);
        boolean result5 = bubbleSort(arr5);
        System.out.println("排序结果: " + result5);
        System.out.println();
        
        // 测试用例6：单个元素
        System.out.println("测试用例6：单个元素");
        String[] arr6 = {"42"};
        System.out.print("排序前: ");
        printArray(arr6);
        if (bubbleSort(arr6)) {
            System.out.print("排序后: ");
            printArray(arr6);
        }
    }
}