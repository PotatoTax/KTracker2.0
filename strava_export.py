from stravalib.client import Client
import json

client = Client()
code = 'ac77673bd86308d2c0520f1b22a0d94b00b593c0'
client_id = 35093
client_secret = 'eae595075041697c1c1ae5120622ba098ff2242a'

start_year = 2000
end_year = 2019

access_token = client.exchange_code_for_token(client_id=client_id,
                                              client_secret=client_secret,
                                              code=code)

client = Client(access_token['access_token'])


def load_new():
    activities = {}

    for activity in client.get_activities(after='{}-01-01T00:00:00Z'.format(str(start_year)),
                                          before='{}-01-01T00:00:00Z'.format(str(end_year + 1))):
        overview = {
            'Name': activity.name,
            'Type': activity.type,
            'Date': str(activity.start_date),
            'Distance': round(activity.distance.num/1000 * 0.621371, 2),
            'Time': activity.moving_time.seconds
        }

        activities[activity.id] = overview
        username = activity.athlete.username

    for key, value in activities.items():
        print(key, value)

    f = open(r"C:\Users\Conor\PycharmProjects\KTracker2.0\activities.txt", "w+")
    f.write(json.dumps(activities))


load_new()
