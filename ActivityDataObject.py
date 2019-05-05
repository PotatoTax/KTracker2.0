import json


class ActivityData:
    def __init__(self):
        self.activity_list = []
        with open("activities.txt", 'r') as file:
            parsed = json.loads(file.read())
            for i in parsed:
                x = parsed[i]
                x['id'] = i
                self.activity_list.append(x)
                print(self.activity_list[-1])