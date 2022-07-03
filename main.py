import time


db = [
    {
        'name': 'Jack',
        'text': 'Hello',
        'time': time.time()
    },
    {
        'name': 'Mary',
        'text': 'Jack',
        'time': time.time()
    },
]


def send_message(name, text):
    db.append({
        'name': name,
        'text': text,
        'time': time.time()
    })


def get_messages(after):
    filtered_messages = []

    for message in db:
        if message['time'] > after:
            filtered_messages.append(message)

    return filtered_messages[:50]



print(db)

send_message('Jack', 'Hi, Mary!')
send_message('Mary', 'What\'s up')

print(db)

print(get_messages(0))
