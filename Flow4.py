[
    {
        "id": "58651465.27ba5c",
        "type": "tab",
        "label": "流程4",
        "disabled": false,
        "info": ""
    },
    {
        "id": "8018d1c1.40eb3",
        "type": "http response",
        "z": "58651465.27ba5c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 550,
        "y": 560,
        "wires": []
    },
    {
        "id": "88a14e05.d2caa",
        "type": "debug",
        "z": "58651465.27ba5c",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 550,
        "y": 640,
        "wires": []
    },
    {
        "id": "de5d3228.6954a",
        "type": "http in",
        "z": "58651465.27ba5c",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 120,
        "y": 540,
        "wires": [
            [
                "f5b2b90b.203e28"
            ]
        ]
    },
    {
        "id": "7e1e6cf0.a6d214",
        "type": "rpi-gpio in",
        "z": "58651465.27ba5c",
        "name": "GPIO4",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": false,
        "x": 110,
        "y": 640,
        "wires": [
            [
                "375e1371.17aacc"
            ]
        ]
    },
    {
        "id": "375e1371.17aacc",
        "type": "function",
        "z": "58651465.27ba5c",
        "name": "Set GPIO",
        "func": "global.set(\"GPIO\",msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 280,
        "y": 600,
        "wires": [
            [
                "88a14e05.d2caa"
            ]
        ]
    },
    {
        "id": "f5b2b90b.203e28",
        "type": "function",
        "z": "58651465.27ba5c",
        "name": "Get GPIO",
        "func": "msg.payload = global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 300,
        "y": 540,
        "wires": [
            [
                "8018d1c1.40eb3",
                "88a14e05.d2caa"
            ]
        ]
    }
]
