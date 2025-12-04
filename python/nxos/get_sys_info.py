import requests
import json

SESSION = requests.Session()

# Define URL and PAYLOAD variables
URL = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"
PAYLOAD = {"aaaUser": {"attributes": {"name": "admin", "pwd": "Admin_1234!"}}}

# Obtain an authentication cookie
SESSION.post(URL, json=PAYLOAD)

# Define SYS_URL variable
SYS_URL = "https://sbx-nxos-mgmt.cisco.com/api/mo/sys.json"

# Obtain system information by making session.get call
# then convert it to JSON format then filter to system attributes
# SYS_INFO = SESSION.get(SYS_URL).json()["imdata"][0]["topSystem"]["attributes"]
SYS_INFO = SESSION.get(SYS_URL).json()

# Print hostname, serial nmber, uptime and current state information
# obtained from the NXOSv9k
# print("HOSTNAME:", SYS_INFO["name"])
# print("SERIAL NUMBER:", SYS_INFO["serial"])
# print("UPTIME:", SYS_INFO["systemUpTime"])
# print("CURRENT STATE:", SYS_INFO["state"])
print(json.dumps(SYS_INFO))
