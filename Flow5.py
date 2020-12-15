[
    {
        "id": "4437de5c.36f09",
        "type": "tab",
        "label": "流程5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "4ac9c997.3fac48",
        "type": "http in",
        "z": "4437de5c.36f09",
        "name": "Set GPIO5",
        "url": "/sergpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 130,
        "y": 320,
        "wires": [
            [
                "992d4739.98d288",
                "ffc9f933.f1b1a8"
            ]
        ]
    },
    {
        "id": "ffc9f933.f1b1a8",
        "type": "function",
        "z": "4437de5c.36f09",
        "name": "Set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 480,
        "wires": [
            [
                "d6dc631.089b1a"
            ]
        ]
    },
    {
        "id": "d6dc631.089b1a",
        "type": "rpi-gpio out",
        "z": "4437de5c.36f09",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 540,
        "y": 540,
        "wires": []
    },
    {
        "id": "992d4739.98d288",
        "type": "function",
        "z": "4437de5c.36f09",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 320,
        "wires": [
            [
                "5cddfe1b.7adec",
                "1f715e42.839692"
            ]
        ]
    },
    {
        "id": "5cddfe1b.7adec",
        "type": "http response",
        "z": "4437de5c.36f09",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 620,
        "y": 380,
        "wires": []
    },
    {
        "id": "1f715e42.839692",
        "type": "debug",
        "z": "4437de5c.36f09",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 620,
        "y": 460,
        "wires": []
    },
    {
        "id": "31509f94.5a52b",
        "type": "http in",
        "z": "4437de5c.36f09",
        "name": "Clear GPIO5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 140,
        "y": 560,
        "wires": [
            [
                "e46fac70.a178f",
                "e85ce167.d58b8"
            ]
        ]
    },
    {
        "id": "e46fac70.a178f",
        "type": "function",
        "z": "4437de5c.36f09",
        "name": "Clear to 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 560,
        "wires": [
            [
                "d6dc631.089b1a"
            ]
        ]
    },
    {
        "id": "e85ce167.d58b8",
        "type": "function",
        "z": "4437de5c.36f09",
        "name": "Return Status",
        "func": "msg.payload =\"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 370,
        "y": 660,
        "wires": [
            [
                "5cddfe1b.7adec",
                "1f715e42.839692"
            ]
        ]
    }
]
