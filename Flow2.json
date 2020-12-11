[
    {
        "id": "7c137fe8.978f1",
        "type": "tab",
        "label": "流程3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "998ae043.dcde1",
        "type": "inject",
        "z": "7c137fe8.978f1",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 90,
        "y": 280,
        "wires": [
            [
                "d9cad2e1.950a7"
            ]
        ]
    },
    {
        "id": "d9cad2e1.950a7",
        "type": "function",
        "z": "7c137fe8.978f1",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey:\"I0JzQRsPD90AHtwd\"\n};\n\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 280,
        "y": 340,
        "wires": [
            [
                "446285cb.30503c"
            ]
        ]
    },
    {
        "id": "446285cb.30503c",
        "type": "http request",
        "z": "7c137fe8.978f1",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": false,
        "url": "http://api.mediatek.com/mcs/v2/devices/DCi0BzeX/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 480,
        "y": 360,
        "wires": [
            [
                "793de525.67c2dc",
                "6127b06c.63a8"
            ]
        ]
    },
    {
        "id": "793de525.67c2dc",
        "type": "http response",
        "z": "7c137fe8.978f1",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 630,
        "y": 360,
        "wires": []
    },
    {
        "id": "6127b06c.63a8",
        "type": "debug",
        "z": "7c137fe8.978f1",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 640,
        "y": 440,
        "wires": []
    }
]
