from dotenv import load_dotenv
import os
import http.client
import json

load_dotenv()

API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

def get_api_connection_from_endpoint(endpoint):

    conn = http.client.HTTPSConnection(API_HOST)
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': API_HOST,
    }

    conn.request("GET", endpoint, headers=headers)

    response = conn.getresponse()

    if response.status != 200:
        raise Exception(f"API request failed with status {response.status}")
    
    data = response.read()
    data_decoded = data.decode('utf-8')
    
    return json.loads(data_decoded)

def fetch_player_data(api_id):

    return get_api_connection_from_endpoint(f"/nfl-player-listing/v1/data?id={api_id}")

def fetch_team_data(api_id):

    return get_api_connection_from_endpoint("/nfl-team-listing/v1/data")
