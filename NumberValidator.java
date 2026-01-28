import java.util.List;

public class NumberValidator {
    
    /**
     * 检测字符串列表中的所有元素是否都为数字
     * 
     * @param stringList 待检测的字符串列表
     * @return 如果所有元素都是数字则返回true，否则返回false
     */
    public static boolean areAllNumbers(List<String> stringList) {
        if (stringList == null || stringList.isEmpty()) {
            return false;
        }
        
        for (String str : stringList) {
            if (str == null || str.trim().isEmpty()) {
                return false;
            }
            
            try {
                // 尝试将字符串转换为数字
                Double.parseDouble(str.trim());
            } catch (NumberFormatException e) {
                return false;
            }
        }
        
        return true;
    }
    
    /**
     * 检测字符串列表中的所有元素是否都为整数
     * 
     * @param stringList 待检测的字符串列表
     * @return 如果所有元素都是整数则返回true，否则返回false
     */
    public static boolean areAllIntegers(List<String> stringList) {
        if (stringList == null || stringList.isEmpty()) {
            return false;
        }
        
        for (String str : stringList) {
            if (str == null || str.trim().isEmpty()) {
                return false;
            }
            
            try {
                // 尝试将字符串转换为整数
                Integer.parseInt(str.trim());
            } catch (NumberFormatException e) {
                return false;
            }
        }
        
        return true;
    }
    
    /**
     * 检测字符串列表中的所有元素是否都为长整数
     * 
     * @param stringList 待检测的字符串列表
     * @return 如果所有元素都是长整数则返回true，否则返回false
     */
    public static boolean areAllLongs(List<String> stringList) {
        if (stringList == null || stringList.isEmpty()) {
            return false;
        }
        
        for (String str : stringList) {
            if (str == null || str.trim().isEmpty()) {
                return false;
            }
            
            try {
                // 尝试将字符串转换为长整数
                Long.parseLong(str.trim());
            } catch (NumberFormatException e) {
                return false;
            }
        }
        
        return true;
    }
    
    // 测试方法
    public static void main(String[] args) {
        // 测试用例1：都是数字
        List<String> test1 = List.of("1", "2.5", "-3", "0", "100.99");
        System.out.println("test1 (都是数字): " + areAllNumbers(test1)); // true
        
        // 测试用例2：包含非数字
        List<String> test2 = List.of("1", "abc", "3");
        System.out.println("test2 (包含非数字): " + areAllNumbers(test2)); // false
        
        // 测试用例3：都是整数
        List<String> test3 = List.of("1", "2", "3", "-5");
        System.out.println("test3 (都是整数): " + areAllIntegers(test3)); // true
        
        // 测试用例4：包含小数（不是整数）
        List<String> test4 = List.of("1", "2.5", "3");
        System.out.println("test4 (包含小数): " + areAllIntegers(test4)); // false
        
        // 测试用例5：空列表
        List<String> test5 = List.of();
        System.out.println("test5 (空列表): " + areAllNumbers(test5)); // false
        
        // 测试用例6：包含null
        List<String> test6 = List.of("1", null, "3");
        System.out.println("test6 (包含null): " + areAllNumbers(test6)); // false
        
        // 测试用例7：包含空字符串
        List<String> test7 = List.of("1", "", "3");
        System.out.println("test7 (包含空字符串): " + areAllNumbers(test7)); // false
        
        // 测试用例8：都是长整数
        List<String> test8 = List.of("100", "200", "9999999999");
        System.out.println("test8 (都是长整数): " + areAllLongs(test8)); // true
    }
}