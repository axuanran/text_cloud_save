import httpx

# 定义要发送的数据
data = {"id": "123456", "data": "TestItem"}

# 写入
#response = httpx.get("http://127.0.0.1:8084", params=data)
#response = httpx.get("https://:8", params=data, verify=False)
#response = httpx.post("https://:8", params=data, verify=False)

# 查询
response = httpx.get("https://:8/12345", verify=False)

# 打印响应状态码和主体内容
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")