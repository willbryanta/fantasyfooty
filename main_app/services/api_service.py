import http.client
import json

API_HOST="nfl-api-data.p.rapidapi.com"
API_KEY="8fc35cf562mshe19dd7988877635p1e3666jsn91cdc8a086f2"

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