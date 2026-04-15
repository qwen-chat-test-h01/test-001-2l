/**
 * 灵活的加法计算器
 * 支持任意两个整数的加法运算，默认演示 1+2=3
 */
public class FlexibleAddition {

    /**
     * 通用加法方法：计算任意两个整数的和
     * @param a 第一个加数
     * @param b 第二个加数
     * @return 两数之和
     */
    public static int add(int a, int b) {
        return a + b;
    }

    /**
     * 重载方法：支持多个整数相加
     * @param numbers 可变参数，任意数量的整数
     * @return 所有数字之和
     */
    public static int add(int... numbers) {
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        return sum;
    }

    /**
     * 格式化输出加法表达式
     * @param a 第一个加数
     * @param b 第二个加数
     */
    public static void printAddition(int a, int b) {
        int result = add(a, b);
        System.out.printf("%d + %d = %d%n", a, b, result);
    }

    public static void main(String[] args) {
        // 默认演示：1 + 2 = 3
        System.out.println("=== 基础演示 ===");
        printAddition(1, 2);

        // 灵活调用：任意数字相加
        System.out.println("\n=== 灵活调用 ===");
        printAddition(5, 7);
        printAddition(100, 250);

        // 多个数相加
        System.out.println("\n=== 多数相加 ===");
        int multiSum = add(1, 2, 3, 4, 5);
        System.out.println("1 + 2 + 3 + 4 + 5 = " + multiSum);

        // 链式调用示例
        System.out.println("\n=== 链式计算 ===");
        int result = add(add(1, 2), add(3, 4));
        System.out.println("(1 + 2) + (3 + 4) = " + result);
    }
}
