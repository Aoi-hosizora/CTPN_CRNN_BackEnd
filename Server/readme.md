# Server API

+ By [Aoi-hosizora](https://github.com/Aoi-hosizora)

### 修订记录
|发布日期|修改说明|
|--|--|
|2019-07-23|初步完成，CTPN待服务器部署完再修改|

### 错误返回格式
|参数名|类型|说明|
|--|--|--|
|`message`|`string`|错误信息标题|
|`detail`|`string`|错误详细信息|

+ 示例
```json
{
    "message": "Image Not Found",
    "detail": "Image \"./tmp/AI_分类.png\" not found."
}
```

### 公共错误码
|错误码|错误描述|英文解释|
|--|--|
|500|服务器错误|Internal Server Error|
|403|不允许访问|Forbidden|
|404|未找到文件*|Not Found|
|405|方法不被允许|Method Not Allowed|
|406|图片错误或未找到|Image Not Found|

### API URL
|方法|路径|功能|说明|
|--|--|--|--|
|GET|`/ocr/`|标题|无|
|POST|`/ocr/upload/`|对图片切割并识别|见请求参数体|

### 请求参数体
|请求参数|类型|描述|是否必须|备注|
|--|--|--|
|`img`|`File`|识别的图片|必须|暂未找到类型问题，中文未检测|

### 响应
+ `GET /ocr/`
```json
{
    "message": "CTPN CRNN OCR Api"
}
```
+ `POST /ocr/upload`
```json
{
    "size": {"x": 682, "y": 1024},
    "cnt": 5,
    "frames": [
        {
            "points": [
                {"x": 342, "y": 150},
                {"x": 664, "y": 115},
                {"x": 679, "y": 270},
                {"x": 358, "y": 305}
            ],
            "score": 0.9998086,
            "ocr": "Half"
        },
        {
            "points": [
                {"x": 878, "y": 653},
                {"x": 1021, "y": 653},
                {"x": 1021, "y": 672},
                {"x": 879, "y": 672}
            ],
            "score": 0.99980634,
            "ocr": "pm0336-1683hy"
        },
        // ...
    ]
}
```

