import requests


def get_items(url):
    resp = requests.get(url,
                        headers={"user-agent": "Fake user-agent"},
                        timeout=3)
    return resp.text


print(get_items('https://blog.betrybe.com/'))
