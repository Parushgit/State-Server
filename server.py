# Below code is linted using pylint
import json
from flask import Flask, request


app = Flask(__name__)
states = []


@app.before_first_request
def _load_json():
    """
        Private method: Loads the json from the file present in the root directory. Only once!
    """
    file_name = 'states.json'
    with open(file_name, 'r') as f:
        for line in f:
            states.append(json.loads(line))


@app.route("/", methods=['POST'])
def start():
    """
        Returns the required output
    """
    return get_state()


def _point_lies_in_state(long, lat, boundaries):
    """
        Private method: Tells if a point lies in the given state or not
        :param long: longitude
        :param lat: latitude
        :param boundaries: boundaries of the state
    """
    j = len(boundaries) - 1
    i = 0
    point_lies = 0
    while i < len(boundaries):
        long1 = boundaries[i][0]
        long2 = boundaries[j][0]
        lat1 = boundaries[i][1]
        lat2 = boundaries[j][1]

        base_condition = (lat1 < lat <= lat2) or (lat2 < lat <= lat1)
        lying_point = base_condition and (long < long1 + (long2 - long1) * (lat - lat1) / (lat2 - lat1))

        if lying_point:
            point_lies = 1 - point_lies
        j = i
        i = i + 1
    return point_lies


def get_state():
    """
        Returns the valid output
    """
    long = request.values.get('longitude')
    lat = request.values.get('latitude')
    if lat is None or long is None:
        return "Input is not correct. Please curl it again!\n"
    else:
        for state in states:
            if _point_lies_in_state(float(long), float(lat), state['border']):
                return '["' + state['state'] + '"]' + '\n'
        return "Given coordinates are outside of United States. Try again!\n"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
