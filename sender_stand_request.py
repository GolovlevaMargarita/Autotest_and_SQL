import requests
import configuration
import data

def post_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, headers=data.headers, json=data.create_order);
    return response.json()['track'];

def get_order_by_track(track_id):
    q = {};
    q["t"] = track_id;

    return requests.get(configuration.URL_SERVICE+configuration.TRACK_ORDER_PATH, params=q, headers=data.headers);