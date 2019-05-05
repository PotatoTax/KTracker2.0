from stravalib.client import Client

client_id = 35093
client = Client()
url = client.authorization_url(client_id=client_id,
                               redirect_uri='http://127.0.0.1:8000/authorization',
                               scope="activity:read")
print(url)  # Open URL, click 'Authorize', use code in url for code in strava_export.py
