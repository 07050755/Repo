[
    {
        "id": "a4403c50.3c4ea",
        "type": "tab",
        "label": "流程2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "788fbf06.31ed6",
        "type": "rpi-gpio out",
        "z": "a4403c50.3c4ea",
        "name": "Green LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 630,
        "y": 560,
        "wires": []
    },
    {
        "id": "a74b8af3.3d2278",
        "type": "debug",
        "z": "a4403c50.3c4ea",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 630,
        "y": 480,
        "wires": []
    },
    {
        "id": "4e989c97.acff14",
        "type": "rpi-gpio in",
        "z": "a4403c50.3c4ea",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": false,
        "x": 140,
        "y": 500,
        "wires": [
            [
                "a74b8af3.3d2278",
                "796cad3c.b7d314"
            ]
        ]
    },
    {
        "id": "796cad3c.b7d314",
        "type": "switch",
        "z": "a4403c50.3c4ea",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 290,
        "y": 560,
        "wires": [
            [
                "ac00f9cd.4a7108"
            ],
            [
                "bbf2fdd2.de8c"
            ]
        ]
    },
    {
        "id": "ac00f9cd.4a7108",
        "type": "change",
        "z": "a4403c50.3c4ea",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 470,
        "y": 520,
        "wires": [
            [
                "788fbf06.31ed6"
            ]
        ]
    },
    {
        "id": "bbf2fdd2.de8c",
        "type": "change",
        "z": "a4403c50.3c4ea",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 450,
        "y": 600,
        "wires": [
            [
                "788fbf06.31ed6"
            ]
        ]
    }
]
