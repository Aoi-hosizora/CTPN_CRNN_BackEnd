# Server API

+ By [Aoi-hosizora](https://github.com/Aoi-hosizora)

### 修订记录
|发布日期|修改说明|
|--|--|
|2019-07-23|初步完成，CTPN 待服务器部署完再修改|

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

### 公共状态码
|错误码|错误描述|英文解释|
|--|--|--|
|200|成功返回|Success|
|500|服务器错误|Internal Server Error|
|403|不允许访问|Forbidden|
|404|未找到文件 \*|Not Found|
|405|方法不被允许|Method Not Allowed|
|406|图片错误或未找到|Image Not Found|
+ \* 暂时未写清什么情况下会出现

### API URL
|方法|URL|功能|说明|
|--|--|--|--|
|GET|`/ocr/`|标题|无|
|POST|`/ocr/upload/`|对图片切割并识别|见请求参数体|

### 请求参数体
|URL|请求参数|类型|描述|是否必须|备注|
|--|--|--|--|--|--|
|`/ocr/upload/`|`img`|`File`|识别的图片|必须|暂未找到类型问题，中文未检测|

---

### 响应
+ `GET /ocr/`

|参数|类型|说明|
|--|--|--|
|`message`|`string`|API 标题|
```json
{
    "message": "CTPN CRNN OCR Api"
}
```

+ `POST /ocr/upload/`

|参数|类型|说明|
|--|--|--|
|`size`|`Point`|图片大小|
|`cnt`|`int`|文字框取结果个数|
|`frames`|`Frame[]`|每个文字框的信息|
|`points`|`Point[]`|文字框按顺时针排序的四个点的坐标|
|`score`|`double`|框取的准确程度|
|`ocr`|`string`|每个文字框的识别结果|

```json
{
    "size": {"x": 682, "y": 1024},
    "cnt": 5,
    "frames": [
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

