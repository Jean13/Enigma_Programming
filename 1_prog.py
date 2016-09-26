# Library for POST requests
import requests

# The URL to send stuff to
target ='http://challenges.enigmagroup.org/programming/1/'

# Verifying we can connect
req = requests.get(target)
if req.status_code != requests.codes.ok:
        raise ValueError('Poof! Unable to connect to target t(X_X)t')
else:
        print('+++ Connected to target. Starting operation...\n')

# IP address and Username
data = {'ip': 'ipgoeshere', 'username': 'usergoeshere'}

# Cookies
cookies = {'mission': 'yes', 'PHPSESSID': 'sessidgoeshere'}
# Sending our cookies, IP and username
req = requests.post(target, cookies=cookies, data=data)

print('+++ Successfully sent information.\n')
print(req.content)

