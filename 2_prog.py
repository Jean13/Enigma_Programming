# Library for requests and regular expression operations
import requests, re

# The URL to send stuff to
target ='http://challenges.enigmagroup.org/programming/2/index.php'

# Cookies
cookies = {'PHPSESSID': 'sessidgoeshere'}

# Verifying we can connect
req = requests.get(target, cookies=cookies)
if req.status_code != requests.codes.ok:
        raise ValueError('Poof! Unable to connect to target t(X_X)t')
else:
        print('+++ Connected to target. Starting operation...\n')

html_code = req.text

match = re.search('You have . second to multiply this random number (.*) by (.) and submit it', html_code)
solution = int(match.group(1)) * int(match.group(2))
values = {'answer': solution}

match = re.search('<input type="hidden" name="E\[number]" value="(.*)" />', html_code)
E_Number = match.group(1)
values.update({"E[number]": E_Number})

match = re.search('<input type="hidden" name="E\[time]" value="(.*)" />', html_code)
E_Time = match.group(1)
values.update({"E[time]": E_Time})

match = re.search('<input type="hidden" name="hash" value="(.*)" />', html_code)
hash_value = match.group(1)
values.update({"hash": hash_value, "submit": "Submit Answer"})

data = values

# Sending our cookies and data
req = requests.post(target, cookies=cookies, data=data)

print('+++ Successfully sent information.\n')


