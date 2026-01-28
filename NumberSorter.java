import java.util.ArrayList;
import java.util.List;

/**
 * 数字字符串排序器
 */
public class NumberSorter {
    
    /**
     * 判断字符串列表是否都为数字（支持整数和小数）
     * 
     * @param list 待检测的字符串列表
     * @return 如果都为数字返回true，否则返回false
     */
    public static boolean areAllNumbers(List<String> list) {
        if (list == null || list.isEmpty()) {
            return false;
        }
        
        for (String str : list) {
            if (str == null || str.trim().isEmpty()) {
                return false;
            }
            String trimmed = str.trim();
            try {
                // 尝试转换为double，支持整数和小数
                Double.parseDouble(trimmed);
            } catch (NumberFormatException e) {
                return false;
            }
        }
        return true;
    }
    
    /**
     * 对字符串列表进行冒泡排序（按数字大小排序）
     * 
     * @param list 待排序的字符串列表
     * @return 排序后的字符串列表
     * @throws IllegalArgumentException 如果列表包含非数字字符串
     */
    public static List<String> bubbleSortNumbers(List<String> list) {
        if (list == null || list.isEmpty()) {
            return new ArrayList<>();
        }
        
        // 先验证是否都为数字
        if (!areAllNumbers(list)) {
            throw new IllegalArgumentException("列表中包含非数字字符串，无法进行排序");
        }
        
        // 创建副本进行排序，避免修改原列表
        List<String> result = new ArrayList<>(list);
        int n = result.size();
        
        // 冒泡排序
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                // 比较两个数字的大小
                double num1 = Double.parseDouble(result.get(j).trim());
                double num2 = Double.parseDouble(result.get(j + 1).trim());
                
                if (num1 > num2) {
                    // 交换
                    String temp = result.get(j);
                    result.set(j, result.get(j + 1));
                    result.set(j + 1, temp);
                    swapped = true;
                }
            }
            // 如果没有发生交换，说明已经有序
            if (!swapped) {
                break;
            }
        }
        
        return result;
    }
    
    /**
     * 测试方法
     */
    public static void main(String[] args) {
        // 测试用例1：正常数字列表
        List<String> test1 = List.of("3.5", "1", "2.8", "10", "0.5");
        System.out.println("测试1 - 原始列表: " + test1);
        System.out.println("是否都为数字: " + areAllNumbers(test1));
        System.out.println("排序后: " + bubbleSortNumbers(test1));
        System.out.println();
        
        // 测试用例2：包含非数字
        List<String> test2 = List.of("1", "2", "abc", "4");
        System.out.println("测试2 - 原始列表: " + test2);
        System.out.println("是否都为数字: " + areAllNumbers(test2));
        try {
            bubbleSortNumbers(test2);
        } catch (IllegalArgumentException e) {
            System.out.println("排序失败: " + e.getMessage());
        }
        System.out.println();
        
        // 测试用例3：包含空格的数字
        List<String> test3 = List.of("  5  ", "  2  ", "  8  ");
        System.out.println("测试3 - 原始列表: " + test3);
        System.out.println("是否都为数字: " + areAllNumbers(test3));
        System.out.println("排序后: " + bubbleSortNumbers(test3));
        System.out.println();
        
        // 测试用例4：负数
        List<String> test4 = List.of("-5", "3", "-10", "0", "7");
        System.out.println("测试4 - 原始列表: " + test4);
        System.out.println("是否都为数字: " + areAllNumbers(test4));
        System.out.println("排序后: " + bubbleSortNumbers(test4));
    }
}