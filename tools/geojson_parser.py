import getopt
import json
import sys


def usage():
    print(f"{sys.argv[0]} -i <input_file> [-o <output_file>] [-f <output_format>]")
    print("\t-i | --in\tInput file with geojson data")
    print("\t-o | --out\tOutput file. Default: STDOUT")


def parse_args():
    ifd = None
    ofd = sys.stdout

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["in=", "out="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--in"):
            ifd = open(arg, "r")
        elif opt in ("-o", "--out"):
            try:
                ofd = open(arg, "w")
            except (IsADirectoryError, PermissionError) as e:
                print(e)
                sys.exit(2)

    if not ifd:
        usage()
        sys.exit(2)

    return ifd, ofd


def parse_node(node):
    points = []

    tables = {
        "Point": "platform",
        "MultiLineString": "route",
        "LineString": "route"
    }

    properties = node["properties"]
    geometry = node["geometry"]

    table = tables[geometry["type"]]

    if table == "platform":
        longitude, latitude = geometry["coordinates"]
        for relation in properties["@relations"]:
            # assert table == relation["role"], f"Unknown node type {table} != {relation['role']}"
            assert relation["role"] in ("platform", "platform_exit_only"), f"Unknown node type {relation['role']}"
            # assert relation["role"], "Unknown platform type"

            points.append({
                "table": table,
                "longitude": longitude,
                "latitude": latitude,
                "name": relation["reltags"]["name"],
                "route": relation["reltags"]["ref"],
                "type": relation["role"]
            })

    elif table == "route":
        name = properties["name"]
        route = properties["ref"]

        assert geometry["type"] in ("MultiLineString", "LineString"), \
            f"Unknown geometry type {geometry['type']}"

        if geometry["type"] == "LineString":
            coordinates = geometry["coordinates"]
        else:
            coordinates = [pair
                           for segment in geometry["coordinates"]
                           for pair in segment]

        for lonlat in coordinates:
            longitude, latitude = lonlat

            chunk = {
                "model": "redit.Route",
                # "pk": rpk,
                "fields": {
                    "longitude": longitude,
                    "latitude": latitude,
                    "name": name,
                    "route": route
                }
            }

            points.append(chunk)

    return points


def main():
    global output_fd, input_fd

    try:
        input_fd, output_fd = parse_args()

        gdata = json.load(input_fd)

        parsed_data = [point
                       for node in gdata["features"]
                       for point in parse_node(node)]

        json.dump(parsed_data, output_fd)
    except json.JSONDecodeError:
        print("Error decode GeoJSON data")
    except KeyError as e:
        print(e)
    finally:
        input_fd.close()
        output_fd.close()


if __name__ == "__main__":
    main()
