/**
 * 水仙花数判断程序
 * 水仙花数是指一个n位数，其各位数字的n次方之和等于该数本身
 * 例如：153 = 1^3 + 5^3 + 3^3
 */
public class NarcissisticNumber {
    
    /**
     * 判断一个数是否为水仙花数
     * @param num 待判断的数字
     * @return 如果是水仙花数返回true，否则返回false
     */
    public static boolean isNarcissistic(int num) {
        if (num < 0) {
            return false;
        }
        
        // 计算数字的位数
        int originalNum = num;
        int digits = String.valueOf(num).length();
        
        // 计算各位数字的n次方之和
        int sum = 0;
        int temp = num;
        while (temp > 0) {
            int digit = temp % 10;
            sum += Math.pow(digit, digits);
            temp /= 10;
        }
        
        return sum == originalNum;
    }
    
    /**
     * 查找指定范围内的所有水仙花数
     * @param start 起始值
     * @param end 结束值
     */
    public static void findNarcissisticNumbers(int start, int end) {
        System.out.println("在范围 [" + start + ", " + end + "] 内的水仙花数有：");
        System.out.println("========================================");
        
        int count = 0;
        for (int i = start; i <= end; i++) {
            if (isNarcissistic(i)) {
                System.out.printf("%d ", i);
                count++;
                if (count % 10 == 0) {
                    System.out.println();
                }
            }
        }
        
        System.out.println("\n========================================");
        System.out.println("共找到 " + count + " 个水仙花数");
    }
    
    public static void main(String[] args) {
        // 示例1：判断单个数字
        int testNumber = 153;
        if (isNarcissistic(testNumber)) {
            System.out.println(testNumber + " 是水仙花数");
        } else {
            System.out.println(testNumber + " 不是水仙花数");
        }
        
        System.out.println();
        
        // 示例2：查找1-10000范围内的所有水仙花数
        findNarcissisticNumbers(1, 10000);
        
        System.out.println();
        
        // 示例3：测试几个已知的数字
        int[] testNumbers = {0, 1, 9, 10, 153, 370, 371, 407, 1634, 8208, 9474};
        System.out.println("测试已知数字：");
        System.out.println("========================================");
        for (int num : testNumbers) {
            String result = isNarcissistic(num) ? "是" : "不是";
            System.out.println(num + " " + result + " 水仙花数");
        }
    }
}
