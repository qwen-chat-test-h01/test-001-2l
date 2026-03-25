fn bubble_sort(mut arr: Vec<i32>) -> Vec<i32> {
    let n = arr.len();

    // 遍历所有数组元素
    for i in 0..n {
        // 标记是否发生了交换，用于优化
        let mut swapped = false;

        // 最后i个元素已经排好序了
        for j in 0..n-i-1 {
            // 如果当前元素比下一个元素大，则交换
            if arr[j] > arr[j + 1] {
                // 交换元素
                arr.swap(j, j + 1);
                swapped = true;
            }
        }

        // 如果没有发生交换，说明数组已经有序
        if !swapped {
            break;
        }
    }

    arr
}

fn bubble_sort_with_steps(mut arr: Vec<i32>) -> Vec<i32> {
    let n = arr.len();
    println!("初始数组: {:?}", arr);

    for i in 0..n {
        let mut swapped = false;
        println!("\n第 {} 轮排序:", i + 1);

        for j in 0..n-i-1 {
            if arr[j] > arr[j + 1] {
                println!("  交换 {} 和 {}", arr[j], arr[j + 1]);
                arr.swap(j, j + 1);
                swapped = true;
                println!("  当前数组: {:?}", arr);
            }
        }

        if !swapped {
            println!("  没有发生交换，排序完成");
            break;
        } else {
            println!("第 {} 轮结束: {:?}", i + 1, arr);
        }
    }

    arr
}

fn print_array(arr: &Vec<i32>) {
    print!("[");
    for (i, val) in arr.iter().enumerate() {
        print!("{}", val);
        if i < arr.len() - 1 {
            print!(", ");
        }
    }
    println!("]");
}

fn main() {
    println!("=== Rust冒泡排序测试 ===");

    // 测试基本冒泡排序
    let test_array = vec![64, 34, 25, 12, 22, 11, 90];
    print!("原始数组: ");
    print_array(&test_array);

    let sorted_array = bubble_sort(test_array.clone());
    print!("排序后数组: ");
    print_array(&sorted_array);

    println!();
    for _ in 0..50 {
        print!("=");
    }
    println!();

    // 测试带步骤显示的冒泡排序
    let test_array2 = vec![64, 34, 25, 12, 22, 11, 90];
    bubble_sort_with_steps(test_array2);

    println!();
    for _ in 0..50 {
        print!("=");
    }
    println!();

    // 测试已经排序的数组（验证优化效果）
    let sorted_test = vec![1, 2, 3, 4, 5];
    println!("\n已排序数组测试: {:?}", sorted_test);
    let result = bubble_sort(sorted_test.clone());
    println!("结果: {:?}", result);

    // 测试边界情况
    println!("\n测试边界情况:");
    println!("空数组排序: {:?}", bubble_sort(vec![]));
    println!("单元素数组排序: {:?}", bubble_sort(vec![42]));
    println!("两个元素数组排序: {:?}", bubble_sort(vec![2, 1]));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_empty_array() {
        assert_eq!(bubble_sort(vec![]), vec![]);
    }

    #[test]
    fn test_single_element() {
        assert_eq!(bubble_sort(vec![42]), vec![42]);
    }

    #[test]
    fn test_sorted_array() {
        assert_eq!(bubble_sort(vec![1, 2, 3, 4, 5]), vec![1, 2, 3, 4, 5]);
    }

    #[test]
    fn test_reverse_sorted_array() {
        assert_eq!(bubble_sort(vec![5, 4, 3, 2, 1]), vec![1, 2, 3, 4, 5]);
    }

    #[test]
    fn test_random_array() {
        assert_eq!(bubble_sort(vec![64, 34, 25, 12, 22, 11, 90]), vec![11, 12, 22, 25, 34, 64, 90]);
    }

    #[test]
    fn test_duplicates() {
        assert_eq!(bubble_sort(vec![3, 1, 4, 1, 5, 9, 2, 6, 5]), vec![1, 1, 2, 3, 4, 5, 5, 6, 9]);
    }
}