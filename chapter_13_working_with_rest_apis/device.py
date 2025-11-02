import requests
from requests.auth import HTTPBasicAuth


class Device:
    def __init__(self, hostname: str, username: str, password: str):
        self.base_url = f"https://{hostname}/restconf/data"
        self.username = username
        self.password = password
        self.headers = {
            "Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json",
            }

    def get_interfaces_json(self):
        response = requests.get(
            url=f"{self.base_url}/Cisco-IOS-XE-native:native/interface",
            headers=self.headers,
            auth=HTTPBasicAuth(username=self.username, password=self.password),
            verify=False
            )
        return response.json()


def main():
    device = Device("10.10.99.1", "script", "cisco123")
    print(device.get_interfaces_json())

if __name__ == "__main__":
    main()
