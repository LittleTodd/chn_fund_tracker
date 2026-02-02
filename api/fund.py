"""
Vercel Serverless Function for fund data API
"""
from http.server import BaseHTTPRequestHandler
import urllib.request
import urllib.error
import json
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置CORS头
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        try:
            # 从查询参数中获取基金代码
            path = self.path
            fund_code = None
            
            if '?' in path:
                query_string = path.split('?')[1]
                params = query_string.split('&')
                for param in params:
                    if '=' in param:
                        key, value = param.split('=', 1)
                        if key == 'code':
                            fund_code = value
                            break
            
            if not fund_code:
                self.wfile.write(json.dumps({
                    'success': False,
                    'error': '请提供基金代码参数 ?code=XXXXXX'
                }).encode())
                return
            
            # 请求天天基金接口
            url = f"http://fundgz.1234567.com.cn/js/{fund_code}.js"
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8')
                
                # 解析 jsonpgz() 格式
                match = re.search(r'jsonpgz\((.*)\)', data)
                if match:
                    fund_data = json.loads(match.group(1))
                    result = {
                        'success': True,
                        'data': fund_data
                    }
                else:
                    result = {
                        'success': False,
                        'error': '数据格式错误'
                    }
                
                self.wfile.write(json.dumps(result, ensure_ascii=False).encode('utf-8'))
                
        except urllib.error.HTTPError as e:
            error_response = {
                'success': False,
                'error': f'基金代码不存在或网络错误: {e.code}'
            }
            self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode('utf-8'))
            
        except urllib.error.URLError as e:
            error_response = {
                'success': False,
                'error': f'网络连接失败'
            }
            self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            error_response = {
                'success': False,
                'error': f'服务器错误: {str(e)}'
            }
            self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode('utf-8'))
    
    def do_OPTIONS(self):
        # 处理CORS预检
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
