#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语音对话性能压测脚本
用于测试语音对话系统的性能指标，包括：
- 并发连接数
- 响应时间
- 吞吐量
- 错误率
- 资源使用情况
"""

import asyncio
import aiohttp
import time
import statistics
import argparse
import json
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor
import hashlib


@dataclass
class PerformanceMetrics:
    """性能指标数据类"""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    response_times: List[float] = field(default_factory=list)
    connection_times: List[float] = field(default_factory=list)
    first_token_times: List[float] = field(default_factory=list)
    total_tokens: int = 0
    errors: Dict[str, int] = field(default_factory=dict)
    start_time: float = 0
    end_time: float = 0


class VoiceChatLoadTester:
    """语音对话压测器"""
    
    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        timeout: int = 60
    ):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.metrics = PerformanceMetrics()
        self._lock = asyncio.Lock()
        
    def _get_headers(self) -> Dict[str, str]:
        """获取请求头"""
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'VoiceChat-LoadTester/1.0'
        }
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'
        return headers
    
    async def _simulate_voice_session(
        self,
        session: aiohttp.ClientSession,
        user_id: str,
        conversation_turns: int = 3
    ) -> Dict:
        """模拟一次完整的语音对话会话"""
        result = {
            'user_id': user_id,
            'success': False,
            'total_time': 0,
            'connection_time': 0,
            'first_token_time': 0,
            'turns_completed': 0,
            'tokens_used': 0,
            'error': None
        }
        
        start_time = time.time()
        
        try:
            # 模拟语音对话的多个回合
            for turn in range(conversation_turns):
                turn_start = time.time()
                
                # 构建测试文本（模拟语音转文字后的内容）
                test_messages = [
                    "你好，我想查询一下今天的天气情况",
                    "请帮我设置一个明天早上7点的闹钟",
                    "播放一些轻松的音乐",
                    "告诉我最近的新闻",
                    "帮我计算一下1234乘以5678",
                ]
                
                payload = {
                    'user_id': user_id,
                    'message': test_messages[turn % len(test_messages)],
                    'session_id': f"session_{user_id}_{int(time.time())}",
                    'timestamp': datetime.now().isoformat(),
                    'audio_duration': 2.5 + (turn * 0.5),  # 模拟音频时长
                    'sample_rate': 16000,
                    'channels': 1
                }
                
                # 发起请求
                conn_start = time.time()
                async with session.post(
                    f'{self.base_url}/api/v1/chat',
                    json=payload,
                    headers=self._get_headers(),
                    timeout=aiohttp.ClientTimeout(total=self.timeout)
                ) as response:
                    result['connection_time'] = time.time() - conn_start
                    
                    # 记录首 token 时间（这里简化为响应开始时间）
                    if turn == 0:
                        result['first_token_time'] = time.time() - start_time
                    
                    response_data = await response.json()
                    
                    if response.status == 200:
                        result['turns_completed'] += 1
                        result['tokens_used'] += response_data.get('tokens', 50)
                    else:
                        result['error'] = f"HTTP {response.status}"
                        break
                
                # 模拟用户思考间隔
                await asyncio.sleep(0.5)
            
            result['success'] = result['turns_completed'] > 0
            result['total_time'] = time.time() - start_time
            
        except asyncio.TimeoutError:
            result['error'] = 'Request timeout'
        except aiohttp.ClientError as e:
            result['error'] = f'Client error: {str(e)}'
        except Exception as e:
            result['error'] = f'Unexpected error: {str(e)}'
        
        return result
    
    async def _worker(
        self,
        session: aiohttp.ClientSession,
        worker_id: int,
        conversations_per_worker: int,
        turns_per_conversation: int
    ):
        """工作线程，执行多个对话会话"""
        for i in range(conversations_per_worker):
            user_id = f"user_{worker_id}_{i}"
            
            async with self._lock:
                self.metrics.total_requests += 1
            
            result = await self._simulate_voice_session(
                session,
                user_id,
                turns_per_conversation
            )
            
            async with self._lock:
                if result['success']:
                    self.metrics.successful_requests += 1
                    self.metrics.response_times.append(result['total_time'])
                    self.metrics.connection_times.append(result['connection_time'])
                    self.metrics.first_token_times.append(result['first_token_time'])
                    self.metrics.total_tokens += result['tokens_used']
                else:
                    self.metrics.failed_requests += 1
                    error_msg = result['error'] or 'Unknown error'
                    self.metrics.errors[error_msg] = self.metrics.errors.get(error_msg, 0) + 1
    
    async def run_load_test(
        self,
        concurrent_users: int = 10,
        conversations_per_user: int = 5,
        turns_per_conversation: int = 3,
        duration_seconds: Optional[int] = None
    ) -> PerformanceMetrics:
        """
        执行压测
        
        Args:
            concurrent_users: 并发用户数
            conversations_per_user: 每个用户的对话次数
            turns_per_conversation: 每个对话的回合数
            duration_seconds: 压测持续时间（秒），如果指定则忽略 conversations_per_user
        """
        print(f"\n{'='*60}")
        print(f"语音对话性能压测开始")
        print(f"{'='*60}")
        print(f"目标URL: {self.base_url}")
        print(f"并发用户数: {concurrent_users}")
        print(f"每用户对话数: {conversations_per_user}")
        print(f"每对话回合数: {turns_per_conversation}")
        if duration_seconds:
            print(f"压测持续时间: {duration_seconds}秒")
        print(f"{'='*60}\n")
        
        self.metrics = PerformanceMetrics()
        self.metrics.start_time = time.time()
        
        connector = aiohttp.TCPConnector(
            limit=concurrent_users * 2,
            limit_per_host=concurrent_users * 2,
            ttl_dns_cache=300,
            use_dns_cache=True
        )
        
        async with aiohttp.ClientSession(connector=connector) as session:
            if duration_seconds:
                # 基于持续时间的压测
                end_time = time.time() + duration_seconds
                tasks = []
                worker_id = 0
                
                while time.time() < end_time:
                    task = asyncio.create_task(
                        self._worker(
                            session,
                            worker_id,
                            1,  # 每次执行1个对话
                            turns_per_conversation
                        )
                    )
                    tasks.append(task)
                    worker_id += 1
                    
                    # 控制并发
                    if len(tasks) >= concurrent_users:
                        done, pending = await asyncio.wait(
                            tasks,
                            return_when=asyncio.FIRST_COMPLETED
                        )
                        tasks = list(pending)
                
                # 等待剩余任务完成
                if tasks:
                    await asyncio.gather(*tasks, return_exceptions=True)
            else:
                # 基于固定次数的压测
                conversations_per_worker = max(1, conversations_per_user)
                
                tasks = [
                    asyncio.create_task(
                        self._worker(
                            session,
                            worker_id,
                            conversations_per_worker,
                            turns_per_conversation
                        )
                    )
                    for worker_id in range(concurrent_users)
                ]
                
                await asyncio.gather(*tasks, return_exceptions=True)
        
        self.metrics.end_time = time.time()
        return self.metrics
    
    def generate_report(self, metrics: PerformanceMetrics) -> str:
        """生成性能报告"""
        total_time = metrics.end_time - metrics.start_time
        
        report = []
        report.append("\n" + "="*60)
        report.append("性能压测报告")
        report.append("="*60)
        report.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # 基础统计
        report.append("【基础统计】")
        report.append(f"  总请求数: {metrics.total_requests}")
        report.append(f"  成功请求数: {metrics.successful_requests}")
        report.append(f"  失败请求数: {metrics.failed_requests}")
        report.append(f"  成功率: {(metrics.successful_requests/metrics.total_requests*100) if metrics.total_requests > 0 else 0:.2f}%")
        report.append(f"  总耗时: {total_time:.2f}秒")
        report.append(f"  总Token数: {metrics.total_tokens}")
        report.append("")
        
        # 响应时间统计
        if metrics.response_times:
            report.append("【响应时间统计（秒）】")
            report.append(f"  平均响应时间: {statistics.mean(metrics.response_times):.3f}")
            report.append(f"  中位数响应时间: {statistics.median(metrics.response_times):.3f}")
            report.append(f"  最小响应时间: {min(metrics.response_times):.3f}")
            report.append(f"  最大响应时间: {max(metrics.response_times):.3f}")
            report.append(f"  标准差: {statistics.stdev(metrics.response_times) if len(metrics.response_times) > 1 else 0:.3f}")
            
            # 百分位数
            sorted_times = sorted(metrics.response_times)
            p90_idx = int(len(sorted_times) * 0.9)
            p95_idx = int(len(sorted_times) * 0.95)
            p99_idx = int(len(sorted_times) * 0.99)
            report.append(f"  P90响应时间: {sorted_times[p90_idx] if p90_idx < len(sorted_times) else sorted_times[-1]:.3f}")
            report.append(f"  P95响应时间: {sorted_times[p95_idx] if p95_idx < len(sorted_times) else sorted_times[-1]:.3f}")
            report.append(f"  P99响应时间: {sorted_times[p99_idx] if p99_idx < len(sorted_times) else sorted_times[-1]:.3f}")
            report.append("")
        
        # 连接时间统计
        if metrics.connection_times:
            report.append("【连接时间统计（秒）】")
            report.append(f"  平均连接时间: {statistics.mean(metrics.connection_times):.3f}")
            report.append(f"  最小连接时间: {min(metrics.connection_times):.3f}")
            report.append(f"  最大连接时间: {max(metrics.connection_times):.3f}")
            report.append("")
        
        # 首Token时间统计
        if metrics.first_token_times:
            report.append("【首Token时间统计（秒）】")
            report.append(f"  平均首Token时间: {statistics.mean(metrics.first_token_times):.3f}")
            report.append(f"  最小首Token时间: {min(metrics.first_token_times):.3f}")
            report.append(f"  最大首Token时间: {max(metrics.first_token_times):.3f}")
            report.append("")
        
        # 吞吐量统计
        report.append("【吞吐量统计】")
        qps = metrics.total_requests / total_time if total_time > 0 else 0
        report.append(f"  QPS (Queries Per Second): {qps:.2f}")
        if metrics.total_tokens > 0:
            tokens_per_second = metrics.total_tokens / total_time
            report.append(f"  Token吞吐量: {tokens_per_second:.2f} tokens/秒")
        report.append("")
        
        # 错误统计
        if metrics.errors:
            report.append("【错误统计】")
            for error, count in sorted(metrics.errors.items(), key=lambda x: x[1], reverse=True):
                report.append(f"  {error}: {count}次 ({count/metrics.failed_requests*100:.1f}%)")
            report.append("")
        
        report.append("="*60)
        
        return "\n".join(report)
    
    def save_report(self, metrics: PerformanceMetrics, filename: str):
        """保存报告到文件"""
        report = self.generate_report(metrics)
        
        # 保存文本报告
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        # 保存JSON数据
        json_filename = filename.replace('.txt', '.json')
        json_data = {
            'timestamp': datetime.now().isoformat(),
            'total_requests': metrics.total_requests,
            'successful_requests': metrics.successful_requests,
            'failed_requests': metrics.failed_requests,
            'success_rate': (metrics.successful_requests/metrics.total_requests*100) if metrics.total_requests > 0 else 0,
            'total_time': metrics.end_time - metrics.start_time,
            'total_tokens': metrics.total_tokens,
            'response_times': {
                'mean': statistics.mean(metrics.response_times) if metrics.response_times else 0,
                'median': statistics.median(metrics.response_times) if metrics.response_times else 0,
                'min': min(metrics.response_times) if metrics.response_times else 0,
                'max': max(metrics.response_times) if metrics.response_times else 0,
                'p90': sorted(metrics.response_times)[int(len(metrics.response_times)*0.9)] if metrics.response_times else 0,
                'p95': sorted(metrics.response_times)[int(len(metrics.response_times)*0.95)] if metrics.response_times else 0,
                'p99': sorted(metrics.response_times)[int(len(metrics.response_times)*0.99)] if metrics.response_times else 0,
            },
            'qps': metrics.total_requests / (metrics.end_time - metrics.start_time) if (metrics.end_time - metrics.start_time) > 0 else 0,
            'errors': metrics.errors
        }
        
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n报告已保存到: {filename}")
        print(f"JSON数据已保存到: {json_filename}")


async def main():
    parser = argparse.ArgumentParser(
        description='语音对话性能压测工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 基本压测：10个并发用户，每个用户5次对话，每对话3个回合
  python voice_chat_load_tester.py -u http://localhost:8080 -c 10 -n 5 -t 3
  
  # 定时压测：20个并发用户，持续60秒
  python voice_chat_load_tester.py -u http://localhost:8080 -c 20 -d 60 -t 3
  
  # 带API密钥的压测
  python voice_chat_load_tester.py -u http://localhost:8080 -k your_api_key -c 10 -n 5
  
  # 保存报告到指定文件
  python voice_chat_load_tester.py -u http://localhost:8080 -c 10 -n 5 -o report.txt
        """
    )
    
    parser.add_argument(
        '-u', '--url',
        required=True,
        help='语音对话服务的基础URL'
    )
    parser.add_argument(
        '-k', '--api-key',
        help='API密钥（如果需要认证）'
    )
    parser.add_argument(
        '-c', '--concurrent',
        type=int,
        default=10,
        help='并发用户数 (默认: 10)'
    )
    parser.add_argument(
        '-n', '--conversations',
        type=int,
        default=5,
        help='每个用户的对话次数 (默认: 5)'
    )
    parser.add_argument(
        '-t', '--turns',
        type=int,
        default=3,
        help='每个对话的回合数 (默认: 3)'
    )
    parser.add_argument(
        '-d', '--duration',
        type=int,
        help='压测持续时间（秒），如果指定则忽略-n参数'
    )
    parser.add_argument(
        '-o', '--output',
        default='load_test_report.txt',
        help='报告输出文件名 (默认: load_test_report.txt)'
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=60,
        help='请求超时时间（秒）(默认: 60)'
    )
    
    args = parser.parse_args()
    
    tester = VoiceChatLoadTester(
        base_url=args.url,
        api_key=args.api_key,
        timeout=args.timeout
    )
    
    try:
        metrics = await tester.run_load_test(
            concurrent_users=args.concurrent,
            conversations_per_user=args.conversations,
            turns_per_conversation=args.turns,
            duration_seconds=args.duration
        )
        
        report = tester.generate_report(metrics)
        print(report)
        
        tester.save_report(metrics, args.output)
        
    except KeyboardInterrupt:
        print("\n\n压测被用户中断")
    except Exception as e:
        print(f"\n压测过程中发生错误: {e}")
        raise


if __name__ == '__main__':
    asyncio.run(main())
