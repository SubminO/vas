import json


data = [
    {
        "model": "route.PlatformType",
        "pk": 1,
        "fields": {
            "name": "platform",
            "description": "Остановка"
        }
    },
    {
        "model": "route.PlatformType",
        "pk": 2,
        "fields": {
            "name": "platform_exit_only",
            "description": "Остановка по требованию"
        }
    },
    {
        "model": "route.PlatformType",
        "pk": 3,
        "fields": {
            "name": "platform_endpoint",
            "description": "Конечная"
        }
    },
]

file_name = "out.json"

with open(file_name, "w") as fp:
    json.dump(data, fp)


