import requests
import json
import os

RCON_URL = os.getenv('RCON_URL')
USERNAME = os.getenv('RCON_USERNAME')
PASSWORD = os.getenv('RCON_PASSWORD')


def main():

    command = 'get_status'

    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
        # logs into rcon
        s.post(f'{RCON_URL}/login', json={'username': USERNAME, 'password': PASSWORD})

        # An authorised command request.
        r = s.get(RCON_URL + command)
        parsed_json = r.json()

        if parsed_json['failed'] is False:
            print(parsed_json)

        else:
            print('The following error was returned:' + parsed_json['error'])
if __name__ == "__main__":
    main()