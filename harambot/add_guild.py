from yahoo_oauth import OAuth2
from config import settings
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/config/guilds.json', 'r+') as f:
    guilds = json.load(f)

    guild = input("Enter Discord Guild ID:")
    league = input("Enter Yahoo League ID :")


    oauth = OAuth2(settings.yahoo_key, settings.yahoo_secret)
    os.remove('secrets.json')

    guild_details = {
        guild:{
            "access_token": oauth.access_token,
            "guid": oauth.guid,
            "refresh_token": oauth.refresh_token,
            "token_time": oauth.token_time,
            "token_type": oauth.token_type,
            "league_id": league
        }
    }

    guilds.update(guild_details)
    f.seek(0)
    json.dump(guilds, f, indent=4)
    f.close()