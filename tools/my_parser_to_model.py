import json
# import logging

# from pprint import pprint
from route.models import Route, RoutePoint, RoutePlatform, PlatformType

"""
  "features": [
    {
      "type": "Feature",
      "properties": {
        "@id": "node/889450313",
        "bus": "yes",
        "highway": "bus_stop",
        "name": "10 микрорайон",
        "public_transport": "platform",
        "trolleybus": "yes"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          47.83179,
          52.0186393
        ]
      },
"""

with open('../tools/balakovo_bus_stop.geojson', 'r') as json_file:
    exist_routes = Route.objects.all()
    exist_platforms = RoutePlatform.objects.all()
    types = PlatformType.objects.all()
    json_data = json.loads(json_file.read())
    prepared_data = []
    for feature in json_data['features']:
        properties = feature.get('properties')
        geometry = feature.get('geometry')
        lon, lat = geometry.get('coordinates')
        name = properties.get('name')
        if name:
            if name not in [p.name for p in exist_platforms]:
                if name not in [p.name for p in prepared_data]:
                    new_platform = RoutePlatform(name=name, latitude=lat, longitude=lon)
                    prepared_data.append(new_platform)
                    new_platform.save()
                    # print(name)
print([p.name for p in prepared_data])
