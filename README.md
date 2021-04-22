# Cisco Learning

This is just a repo for programatic learning of Cisco devices. It will over time evolve and grow.

## Requirements

1. Clone repo

   ```bash
   git clone git@github.com:mrlesmithjr/Cisco_Learning.git --recursive
   ```

1. Install Python requirements

   ```bash
   pip install -r requirements.txt
   ```

## Environments

### Nexus9000v Always On

```text
Host: sbx-nxos-mgmt.cisco.com
SSH Port: 8181
NETCONF Port: 10000
RESTCONF Ports: 9443 (HTTPS)
Username: admin
Password: Admin_1234!
```

### CSR1000V Always On

```text
Host: ios-xe-mgmt.cisco.com
SSH Port: 8181
NETCONF Port: 10000
RESTCONF Ports: 9443 (HTTPS)
Username: developer
Password: C1sco12345
```

### ACI Always On

```text
Username: admin
Password: ciscopsdt
URL: https://sandboxapicdc.cisco.com
```

### Cisco DNA Center Always On

1. Go to https://sandboxdnac.cisco.com
1. Accept the self-signed certificate
1. Allow for showing of Browser Notifications
1. Login with credentials [devnetuser/Cisco123!]

### Cisco Meraki Always On

```text
URL: https://n149.meraki.com/
Username: devnetmeraki@cisco.com
Password: ilovemeraki
You can also use this API key for the Dashboard API: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0
```
