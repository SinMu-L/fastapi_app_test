作为coolResource 的后端服务

## TODO
✅最好来个自动解析网站logo的服务,服务如下
```
curl --location 'https://host/extra_site_logo?site=http://www.baidu.com' \
'

response
{
    "code": 200,
    "msg":"",
    "data":{
        "logo": "https://www.baidu.com/logo.svg"
    }
}
```

🔄添加资源信息
```
curl --location 'https://host/resource/add' \
--header 'Content-Type: application/json' \
--data '{
    "site":"https://www.baidu.com"
}'

response
{
    "code": 200,
    "msg":"",
    "data":{
        "logo": "https://www.baidu.com/logo.svg"
    }
}
```