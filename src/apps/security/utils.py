import os
import base64


def generate_token():
    return base64.b64encode((os.urandom(48))).decode('utf-8')
