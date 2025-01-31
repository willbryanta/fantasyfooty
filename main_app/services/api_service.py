from dotenv import load_dotenv
import os
import http.client
import json

load_dotenv()

API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")


def fetch_player_data(api_id):

    conn = http.client.HTTPSConnection(API_HOST)
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': API_HOST,
    }
    endpoint = f"/nfl-player-listing/v1/data?id={api_id}"
    conn.request("GET", endpoint, headers=headers)

    response = conn.getresponse()

    if response.status != 200:
        raise Exception(f"API request failed with status {response.status}")
    
    data = response.read()
    player_data = data.decode('utf-8')
    
    return json.loads(player_data)

def fetch_team_data(api_id):

    conn = http.client.HTTPSConnection(API_HOST)

    headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': API_HOST
    }

    endpoint = "/nfl-team-listing/v1/data"

    conn.request("GET", endpoint, headers=headers)

    response = conn.getresponse()
    data = response.read()
    team_data = data.decode("utf-8")

    return json.loads(team_data)
