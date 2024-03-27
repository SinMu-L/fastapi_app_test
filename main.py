from typing import Optional

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/extra_site_logo")
def extra_site_logo(site: str):
    print("site: ",site)
    # 设置用户代理信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    # 目标网站的URL
    url = site

    # 发送GET请求获取网页内容
    response = requests.get(url, headers=headers)

    # 解析网页内容
    soup = BeautifulSoup(response.content, "html.parser")

    # 查找网站的logo或缩略图链接
    logo = soup.find("link", rel="icon")  # 查找favicon链接
    logo_url=""
    if logo:
        logo_url = logo["href"]
        print(f"Logo URL: {logo_url}")

    # 如果未找到favicon链接，可以尝试查找包含logo的img标签
    if not logo:
        logo = soup.find("img", alt="logo")  # 假设logo有一个alt属性为'logo'
        if logo:
            logo_url = logo["src"]
            print(f"Logo URL: {logo_url}")
    if len(logo_url) > 0:
        return {"code": 200, "msg": "", "data": {"logo": logo_url}}
    return {"code": 201, "msg": "未找到logo", "data": {}}


@app.post("/resource/add")
def resource_add():
    return {"message": "resource_add"}
