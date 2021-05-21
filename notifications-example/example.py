import openfin

client = openfin.OpenFinClient()


def log_message(*args, **kwargs):
    print(args, kwargs)


def on_register(val):
    print("Registered")


client.subscribe(openfin.SubKey.from_string("notification-relay/outbox"), log_message, on_register)

payload = {
    "title": "Important Notification",
    "body": "Please open google to search for important information.",
    "category": "Signals",
    "customData": {
        "customId": "12345"
    },
    "stream": {
        "id": "5a2f6e02-5964-48cc-ae88-81df125d9314",
        "displayName": "Python Stream"
    },
    "buttons": [
        {
            "title": "Open In OpenFin",
            "onClick": {
                "task": "open-in-openfin",
                "url": "https://www.google.com",
                "handler": "agent",
                "target": "openfin"
            }
        },
        {
            "title": "Open In Default",
            "onClick": {
                "task": "open-in-default",
                "url": "https://www.google.com",
                "handler": "agent"
            }
        },
        {
            "title": "Open In Browser",
            "onClick": {
                "task": "open-in-browser",
                "url": "https://www.google.com",
                "handler": "agent",
                "target": "browser"
            }
        }
    ]
}

for index in range(0, 1):
    client.publish("notification-relay/inbox", payload)

text = input("Enter any key to exit")
