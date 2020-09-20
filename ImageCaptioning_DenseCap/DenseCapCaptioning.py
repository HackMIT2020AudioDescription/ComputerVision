import requests

def get_captions():
    r = requests.post(
        "https://api.deepai.org/api/densecap",
        files={
            'image': open('/path/to/your/file.jpg', 'rb'),
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'})

print(r.json())