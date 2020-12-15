[
    {
        "id": "23307cc.3e35584",
        "type": "tab",
        "label": "流程1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "f3f388ef.a44ea8",
        "type": "inject",
        "z": "23307cc.3e35584",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 150,
        "y": 300,
        "wires": [
            [
                "b9e41621.5df2f8"
            ]
        ]
    },
    {
        "id": "b9e41621.5df2f8",
        "type": "function",
        "z": "23307cc.3e35584",
        "name": "",
        "func": "msg.headers={\n    deviceKey:\"I0JzQRsPD90AHtwd\"\n};\nmsg.payload=\"Temperature,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 300,
        "y": 400,
        "wires": [
            [
                "98f37077.3fc6e"
            ]
        ]
    },
    {
        "id": "98f37077.3fc6e",
        "type": "http request",
        "z": "23307cc.3e35584",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "paytoqs": false,
        "url": "https://api.mediatek.com/mcs/v2/devices/DCi0BzeX/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 460,
        "y": 400,
        "wires": [
            [
                "1c855695.267229",
                "5c4f8afe.d1de54"
            ]
        ]
    },
    {
        "id": "1c855695.267229",
        "type": "http response",
        "z": "23307cc.3e35584",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 620,
        "y": 420,
        "wires": []
    },
    {
        "id": "5c4f8afe.d1de54",
        "type": "debug",
        "z": "23307cc.3e35584",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 630,
        "y": 460,
        "wires": []
    }
]
