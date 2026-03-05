// 添加到购物车功能
document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartCountElement = document.createElement('span');
    let cartCount = 0;

    // 添加购物车按钮点击事件
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const fruitCard = e.target.closest('.fruit-card');
            const fruitName = fruitCard.querySelector('h3').textContent;
            
            // 更新购物车计数
            cartCount++;
            
            // 显示添加成功提示
            alert(`${fruitName} 已添加到购物车！`);
            
            // 按钮文字变化效果
            const originalText = e.target.textContent;
            e.target.textContent = '已添加 ✓';
            e.target.style.backgroundColor = '#45a049';
            
            setTimeout(() => {
                e.target.textContent = originalText;
                e.target.style.backgroundColor = '';
            }, 1500);
        });
    });

    // 导航栏平滑滚动
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            window.scrollTo({
                top: targetSection.offsetTop - 70,
                behavior: 'smooth'
            });
        });
    });

    // 表单提交处理
    const contactForm = document.querySelector('.contact-form');
    if(contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 获取表单数据
            const name = this.querySelector('input[type="text"]').value;
            const email = this.querySelector('input[type="email"]').value;
            const message = this.querySelector('textarea').value;
            
            // 简单验证
            if(name && email && message) {
                alert('感谢您的留言！我们会尽快回复您。');
                this.reset();
            } else {
                alert('请填写完整的信息！');
            }
        });
    }

    // 滚动时导航栏背景变化
    window.addEventListener('scroll', function() {
        const header = document.querySelector('header');
        if(window.scrollY > 50) {
            header.style.backgroundColor = '#45a049';
        } else {
            header.style.backgroundColor = '#4CAF50';
        }
    });
});