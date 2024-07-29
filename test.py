import httpx

# 定义要发送的数据
data = {"id": "1234", "data": "TestItem"}

# 使用httpx发送POST请求
#response = httpx.get("http://127.0.0.1:8084", params=data)
response = httpx.post("http://127.0.0.1:8084", params=data)
# 打印响应状态码和主体内容
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")