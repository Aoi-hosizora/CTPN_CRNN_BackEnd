# ctpn.py API
```python
from ctpn import ctpnParse
ctpnParse("./ctpn_repo/data/demo/006.jpg")
```

```json
{
    "size": {
        "x": 1280,
        "y": 960
    },
    "cnt": 8,
    "frames": [
        {
            "points":[
                {"x": "250", "y": "800"},
                {"x": "930", "y": "817"},
                {"x": "928", "y": "911"},
                {"x": "247", "y": "893"}
            ],
            "score": "0.9996464"
        },
        {
            "points": [
                {"x": "200", "y": "630"},
                {"x": "603", "y": "642"},
                {"x": "602", "y": "737"},
                {"x": "197", "y": "724"}
            ],
            "score": "0.99963737"
        }, 
        // ...
    ]
}
```