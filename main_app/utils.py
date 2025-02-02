from .models import Team
from .api import fetch_team_data

def save_teams_to_db():
    try:
        api_data = fetch_team_data()
        teams = api_data.get('teams', [])

        for team in teams:
            team_obj, created = Teams.objects.update_or_create(
                api_id=team['id'],
                defaults={
                    'display_name': team['displayName'],
                    'abbreviation': team['abbreviation'],
                    'location': team['location'],
                    'color': team['color'],
                    'alternate_color': team['alternateColor'],
                    'logo': team['logo']                }
            )
            if created:
                print(f"Added new team: {team['displayName']}")
            else:
                print(f"Updated team: {team['displayName']}")

        except Exception as e:
            print(f"Error saving teams to DB: {e}")