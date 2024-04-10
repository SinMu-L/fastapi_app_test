from typing import Optional

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from datetime import datetime

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


@app.post("/is_cn_work_day")
async def is_cn_work_day(date):
    """
    判断时间是否是中国的工作日
    :param date: 2024-01-21
    :return: bool
    """
    try:
        d = datetime.strptime(date_string, date_format).date()
        holidays = [
            "2024-01-01",
            "2024-02-10",
            "2024-02-11",
            "2024-02-12",
            "2024-02-13",
            "2024-02-14",
            "2024-02-15",
            "2024-02-16",
            "2024-02-17",
            "2024-04-04",
            "2024-04-05",
            "2024-04-06",
            "2024-05-01",
            "2024-05-02",
            "2024-05-03",
            "2024-05-04",
            "2024-05-05",
            "2024-06-10",
            "2024-09-15",
            "2024-09-16",
            "2024-09-17",
            "2024-10-01",
            "2024-10-02",
            "2024-10-03",
            "2024-10-04",
            "2024-10-05",
            "2024-10-06",
            "2024-10-07",
        ]

        work_overtime_black = [
            "2024-02-04",
            "2024-02-18",
            "2024-02-04",
            "2024-02-04",
            "2024-04-07",
            "2024-04-28",
            "2024-05-11",
            "2024-09-14",
            "2024-09-29",
            "2024-10-12",
        ]
        is_cn_work_day = date in holidays or date in work_overtime_black
        if not is_cn_work_day:
            if d.weekday() == 5 or d.weekday()==6:
                return {"is_cn_work_day": True, "msg":""}
            else:
                return {"is_cn_work_day": False, "msg":""}
        return {"is_cn_work_day": is_cn_work_day, "msg": ""}
    except ValueError:
        return {"is_cn_work_day": False, "msg": "日期格式不正确"}

    




