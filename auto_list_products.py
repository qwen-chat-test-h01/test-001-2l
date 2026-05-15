#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
商品自动上架自动化脚本
支持多种电商平台，可配置化上架商品
"""

import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('product_listing.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


@dataclass
class Product:
    """商品数据模型"""
    product_id: str
    name: str
    description: str
    price: float
    stock: int
    category: str
    images: List[str]
    sku: str
    weight: Optional[float] = None
    dimensions: Optional[Dict[str, float]] = None
    tags: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
    
    def to_dict(self) -> Dict:
        return asdict(self)


class PlatformAdapter(ABC):
    """电商平台适配器基类"""
    
    @abstractmethod
    def login(self, credentials: Dict) -> bool:
        """登录平台"""
        pass
    
    @abstractmethod
    def upload_product(self, product: Product) -> bool:
        """上架商品"""
        pass
    
    @abstractmethod
    def update_stock(self, product_id: str, stock: int) -> bool:
        """更新库存"""
        pass
    
    @abstractmethod
    def update_price(self, product_id: str, price: float) -> bool:
        """更新价格"""
        pass
    
    @abstractmethod
    def get_product_status(self, product_id: str) -> Dict:
        """获取商品状态"""
        pass


class TaobaoAdapter(PlatformAdapter):
    """淘宝平台适配器示例"""
    
    def __init__(self):
        self.session = None
        self.logged_in = False
    
    def login(self, credentials: Dict) -> bool:
        """
        淘宝登录实现
        实际使用时需要集成淘宝开放平台SDK
        """
        logger.info("正在登录淘宝平台...")
        try:
            # 模拟登录过程
            # 实际实现需要调用淘宝API
            time.sleep(1)  # 模拟网络请求
            self.logged_in = True
            logger.info("淘宝登录成功")
            return True
        except Exception as e:
            logger.error(f"淘宝登录失败: {str(e)}")
            return False
    
    def upload_product(self, product: Product) -> bool:
        """上架商品到淘宝"""
        if not self.logged_in:
            logger.error("未登录，无法上架商品")
            return False
        
        logger.info(f"正在上架商品: {product.name}")
        try:
            # 模拟商品上架
            # 实际实现需要调用淘宝API
            time.sleep(0.5)
            logger.info(f"商品 {product.name} 上架成功")
            return True
        except Exception as e:
            logger.error(f"商品上架失败: {str(e)}")
            return False
    
    def update_stock(self, product_id: str, stock: int) -> bool:
        """更新淘宝商品库存"""
        logger.info(f"更新商品 {product_id} 库存为: {stock}")
        try:
            time.sleep(0.3)
            logger.info(f"商品 {product_id} 库存更新成功")
            return True
        except Exception as e:
            logger.error(f"库存更新失败: {str(e)}")
            return False
    
    def update_price(self, product_id: str, price: float) -> bool:
        """更新淘宝商品价格"""
        logger.info(f"更新商品 {product_id} 价格为: {price}")
        try:
            time.sleep(0.3)
            logger.info(f"商品 {product_id} 价格更新成功")
            return True
        except Exception as e:
            logger.error(f"价格更新失败: {str(e)}")
            return False
    
    def get_product_status(self, product_id: str) -> Dict:
        """获取淘宝商品状态"""
        return {
            "product_id": product_id,
            "status": "active",
            "stock": 100,
            "sales": 50
        }


class JDAdapter(PlatformAdapter):
    """京东平台适配器示例"""
    
    def __init__(self):
        self.session = None
        self.logged_in = False
    
    def login(self, credentials: Dict) -> bool:
        logger.info("正在登录京东平台...")
        try:
            time.sleep(1)
            self.logged_in = True
            logger.info("京东登录成功")
            return True
        except Exception as e:
            logger.error(f"京东登录失败: {str(e)}")
            return False
    
    def upload_product(self, product: Product) -> bool:
        if not self.logged_in:
            logger.error("未登录，无法上架商品")
            return False
        
        logger.info(f"正在上架商品: {product.name}")
        try:
            time.sleep(0.5)
            logger.info(f"商品 {product.name} 上架成功")
            return True
        except Exception as e:
            logger.error(f"商品上架失败: {str(e)}")
            return False
    
    def update_stock(self, product_id: str, stock: int) -> bool:
        logger.info(f"更新商品 {product_id} 库存为: {stock}")
        try:
            time.sleep(0.3)
            logger.info(f"商品 {product_id} 库存更新成功")
            return True
        except Exception as e:
            logger.error(f"库存更新失败: {str(e)}")
            return False
    
    def update_price(self, product_id: str, price: float) -> bool:
        logger.info(f"更新商品 {product_id} 价格为: {price}")
        try:
            time.sleep(0.3)
            logger.info(f"商品 {product_id} 价格更新成功")
            return True
        except Exception as e:
            logger.error(f"价格更新失败: {str(e)}")
            return False
    
    def get_product_status(self, product_id: str) -> Dict:
        return {
            "product_id": product_id,
            "status": "active",
            "stock": 100,
            "sales": 50
        }


class ProductLister:
    """商品上架管理器"""
    
    def __init__(self):
        self.platforms: Dict[str, PlatformAdapter] = {}
        self.products: List[Product] = []
        self.results = []
    
    def register_platform(self, platform_name: str, adapter: PlatformAdapter):
        """注册电商平台"""
        self.platforms[platform_name] = adapter
        logger.info(f"已注册平台: {platform_name}")
    
    def load_products_from_json(self, file_path: str) -> List[Product]:
        """从JSON文件加载商品数据"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            products = []
            for item in data:
                product = Product(
                    product_id=item.get('product_id', ''),
                    name=item.get('name', ''),
                    description=item.get('description', ''),
                    price=float(item.get('price', 0)),
                    stock=int(item.get('stock', 0)),
                    category=item.get('category', ''),
                    images=item.get('images', []),
                    sku=item.get('sku', ''),
                    weight=item.get('weight'),
                    dimensions=item.get('dimensions'),
                    tags=item.get('tags', [])
                )
                products.append(product)
            
            self.products = products
            logger.info(f"成功加载 {len(products)} 个商品")
            return products
        except Exception as e:
            logger.error(f"加载商品数据失败: {str(e)}")
            return []
    
    def load_products_from_csv(self, file_path: str) -> List[Product]:
        """从CSV文件加载商品数据"""
        import csv
        try:
            products = []
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    product = Product(
                        product_id=row.get('product_id', ''),
                        name=row.get('name', ''),
                        description=row.get('description', ''),
                        price=float(row.get('price', 0)),
                        stock=int(row.get('stock', 0)),
                        category=row.get('category', ''),
                        images=row.get('images', '').split(';') if row.get('images') else [],
                        sku=row.get('sku', ''),
                        weight=float(row['weight']) if row.get('weight') else None,
                        tags=row.get('tags', '').split(';') if row.get('tags') else []
                    )
                    products.append(product)
            
            self.products = products
            logger.info(f"成功加载 {len(products)} 个商品")
            return products
        except Exception as e:
            logger.error(f"加载CSV商品数据失败: {str(e)}")
            return []
    
    def list_products(self, platforms: List[str] = None, delay: float = 1.0) -> Dict:
        """
        执行商品上架
        
        Args:
            platforms: 要上架的平台列表，如果为None则上架所有已注册平台
            delay: 每个商品之间的延迟时间（秒）
        
        Returns:
            上架结果统计
        """
        if not self.products:
            logger.error("没有商品可上架")
            return {"success": 0, "failed": 0}
        
        if platforms is None:
            platforms = list(self.platforms.keys())
        
        logger.info(f"开始上架 {len(self.products)} 个商品到 {len(platforms)} 个平台")
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "total_products": len(self.products),
            "platforms": platforms,
            "details": []
        }
        
        total_success = 0
        total_failed = 0
        
        for platform_name in platforms:
            if platform_name not in self.platforms:
                logger.warning(f"平台 {platform_name} 未注册，跳过")
                continue
            
            adapter = self.platforms[platform_name]
            platform_success = 0
            platform_failed = 0
            
            # 登录平台
            if not adapter.login({}):
                logger.error(f"平台 {platform_name} 登录失败，跳过该平台")
                continue
            
            # 上架每个商品
            for product in self.products:
                try:
                    success = adapter.upload_product(product)
                    
                    result_detail = {
                        "platform": platform_name,
                        "product_id": product.product_id,
                        "product_name": product.name,
                        "success": success,
                        "timestamp": datetime.now().isoformat()
                    }
                    
                    results["details"].append(result_detail)
                    
                    if success:
                        platform_success += 1
                        total_success += 1
                        logger.info(f"[{platform_name}] 商品上架成功: {product.name}")
                    else:
                        platform_failed += 1
                        total_failed += 1
                        logger.error(f"[{platform_name}] 商品上架失败: {product.name}")
                    
                    # 延迟避免请求过快
                    time.sleep(delay)
                    
                except Exception as e:
                    platform_failed += 1
                    total_failed += 1
                    logger.error(f"[{platform_name}] 商品上架异常: {product.name}, 错误: {str(e)}")
            
            logger.info(f"平台 {platform_name} 上架完成: 成功 {platform_success}, 失败 {platform_failed}")
        
        results["summary"] = {
            "total_success": total_success,
            "total_failed": total_failed,
            "success_rate": f"{(total_success / (total_success + total_failed) * 100):.2f}%" if (total_success + total_failed) > 0 else "0%"
        }
        
        self.results = results
        logger.info(f"上架任务完成: 成功 {total_success}, 失败 {total_failed}")
        
        return results
    
    def save_results(self, output_file: str = "listing_results.json"):
        """保存上架结果到文件"""
        if not self.results:
            logger.warning("没有结果可保存")
            return
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, ensure_ascii=False, indent=2)
            logger.info(f"上架结果已保存到: {output_file}")
        except Exception as e:
            logger.error(f"保存结果失败: {str(e)}")


def create_sample_products():
    """创建示例商品数据"""
    products = [
        Product(
            product_id="P001",
            name="智能手机 X1",
            description="高性能智能手机，6.7英寸屏幕，128GB存储",
            price=2999.00,
            stock=100,
            category="电子产品/手机",
            images=["image1.jpg", "image2.jpg"],
            sku="SM-X1-128",
            weight=0.2,
            tags=["手机", "智能", "5G"]
        ),
        Product(
            product_id="P002",
            name="无线蓝牙耳机",
            description="降噪无线蓝牙耳机，长续航30小时",
            price=399.00,
            stock=200,
            category="电子产品/配件",
            images=["headphone1.jpg"],
            sku="HP-BT-001",
            weight=0.05,
            tags=["耳机", "无线", "蓝牙"]
        ),
        Product(
            product_id="P003",
            name="运动手表 Pro",
            description="智能运动手表，心率监测，GPS定位",
            price=899.00,
            stock=150,
            category="电子产品/穿戴设备",
            images=["watch1.jpg", "watch2.jpg"],
            sku="SW-PRO-001",
            weight=0.08,
            tags=["手表", "运动", "智能"]
        )
    ]
    return products


def main():
    """主函数"""
    logger.info("=" * 50)
    logger.info("商品自动上架系统启动")
    logger.info("=" * 50)
    
    # 创建上架管理器
    lister = ProductLister()
    
    # 注册电商平台
    taobao_adapter = TaobaoAdapter()
    jd_adapter = JDAdapter()
    
    lister.register_platform("淘宝", taobao_adapter)
    lister.register_platform("京东", jd_adapter)
    
    # 方式1: 使用示例商品
    products = create_sample_products()
    lister.products = products
    logger.info(f"使用 {len(products)} 个示例商品")
    
    # 方式2: 从JSON文件加载商品（取消注释使用）
    # lister.load_products_from_json("products.json")
    
    # 方式3: 从CSV文件加载商品（取消注释使用）
    # lister.load_products_from_csv("products.csv")
    
    # 执行上架
    results = lister.list_products(
        platforms=["淘宝", "京东"],  # 指定平台，或设为None上架所有平台
        delay=0.5  # 商品间延迟0.5秒
    )
    
    # 保存结果
    lister.save_results("listing_results.json")
    
    # 打印摘要
    print("\n" + "=" * 50)
    print("上架任务完成摘要")
    print("=" * 50)
    print(f"总商品数: {results['total_products']}")
    print(f"成功: {results['summary']['total_success']}")
    print(f"失败: {results['summary']['total_failed']}")
    print(f"成功率: {results['summary']['success_rate']}")
    print("=" * 50)
    
    return results


if __name__ == "__main__":
    main()
