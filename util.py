def get_senderId(json):
    return json["entry"][0]["messaging"][0]["sender"]["id"]

def get_message(json):
    return json["entry"][0]["messaging"][0]["message"]["text"]

