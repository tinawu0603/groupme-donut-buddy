import requests
import random

def grouping():
    names = ["Zack", "Cassie", "Andy", "Sharon", "Liam",
    "Sabrina", "Rajon", "Kate", "Robert", "Tina"]
    pairs = []
    while names:
        first = choose_random(names)
        second = choose_random(names)
        pair = first, second
        pairs.append(pair)
    to_send = "This week's pairings are:" + format_grouping(pairs)
    
    requests.post('https://api.groupme.com/v3/bots/post',
    data={'bot_id':'af065bcc6f08df37c5cd91d0c6', \
    "text": to_send})

def format_grouping(pairs):
    result = ""
    for first, second in pairs:
        result += "\n" + first + " <> " + second
    return result

def choose_random(names):
    # select a random element from the list of names
    idx = random.randrange(0, len(names))
    return names.pop(idx)

grouping()

# test-donut-buddies
'''
"bot": {
    "name": "Donut",
    "bot_id": "af065bcc6f08df37c5cd91d0c6",
    "group_id": "57334083",
    "group_name": "test-donut-buddies",
    "avatar_url": null,
    "callback_url": null,
    "dm_notification": false
}
'''

# Stealth 2019 Unofficial
'''
"bot": {
    "name": "Donut",
    "bot_id": "18f8f4a49bbd79c1d5a470a062",
    "group_id": "51998580",
    "group_name": "Stealth 2019 Unofficial",
    "avatar_url": null,
    "callback_url": null,
    "dm_notification": false
}
'''

# Send message
'''
POST url: https://api.groupme.com/v3/bots/post
{
  "bot_id"  : "<bot_id>",
  "text"    : "<text to send>"
}
'''

