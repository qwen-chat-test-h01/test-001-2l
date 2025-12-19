// 绘制不同类型的三角形

// 1. 打印直角三角形（右下直角）
function printRightTriangle(height) {
    console.log("直角三角形（右下直角）:");
    for (let i = 1; i <= height; i++) {
        let line = '';
        for (let j = 1; j <= i; j++) {
            line += '* ';
        }
        console.log(line);
    }
}

// 2. 打印等腰三角形
function printIsoscelesTriangle(height) {
    console.log("\n等腰三角形:");
    for (let i = 1; i <= height; i++) {
        let spaces = ' '.repeat(height - i);
        let stars = '* '.repeat(i);
        console.log(spaces + stars);
    }
}

// 3. 打印空心三角形
function printHollowTriangle(height) {
    console.log("\n空心三角形:");
    for (let i = 1; i <= height; i++) {
        let line = '';
        
        if (i === 1) {
            // 第一行只有一个星号
            line = ' '.repeat(height - 1) + '*';
        } else if (i === height) {
            // 最后一行全是星号
            line = ' '.repeat(height - i) + '* '.repeat(i);
        } else {
            // 中间行只有两边有星号，中间是空格
            line = ' '.repeat(height - i) + '*' + ' '.repeat(2 * i - 3) + '*';
        }
        
        console.log(line);
    }
}

// 4. 打印数字三角形
function printNumberTriangle(height) {
    console.log("\n数字三角形:");
    for (let i = 1; i <= height; i++) {
        let spaces = ' '.repeat(height - i);
        let numbers = '';
        for (let j = 1; j <= i; j++) {
            numbers += j + ' ';
        }
        console.log(spaces + numbers);
    }
}

// 调用函数绘制各种三角形
const triangleHeight = 7;

printRightTriangle(triangleHeight);
printIsoscelesTriangle(triangleHeight);
printHollowTriangle(triangleHeight);
printNumberTriangle(triangleHeight);

// 计算三角形面积和周长的函数
console.log("\n三角形计算功能:");

function calculateTriangleArea(base, height) {
    return 0.5 * base * height;
}

function calculateTrianglePerimeter(side1, side2, side3) {
    return side1 + side2 + side3;
}

// 示例计算
const base = 6;
const height = 8;
const area = calculateTriangleArea(base, height);
console.log(`三角形面积 (底: ${base}, 高: ${height}): ${area}`);

const side1 = 3;
const side2 = 4;
const side3 = 5;
const perimeter = calculateTrianglePerimeter(side1, side2, side3);
console.log(`三角形周长 (边1: ${side1}, 边2: ${side2}, 边3: ${side3}): ${perimeter}`);