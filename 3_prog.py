# Library for requests
import requests
# PIL adds image processing capabilities
from PIL import Image
# StringIO allows to read and write strings as files
from StringIO import StringIO

# The URL to send stuff to
target ='http://challenges.enigmagroup.org/programming/3/image.php'

# Cookies 
cookieName1 = 'PHPSESSID'
cookieValue1 = 'sessidgoeshere'
cookies = {cookieName1: cookieValue1}

# Referer
referer = 'http://challenges.enigmagroup.org/programming/3/image.php'

# Headers
headers = {'Referer': referer}
 
# Verifying we can connect
req = requests.post(target, cookies=cookies)
if req.status_code != requests.codes.ok:
        raise ValueError('Poof! Unable to connect to target t(X_X)t')
else:
        print('+++ Connected to target. Starting operation...\n')

# Get image and RGB
theImage = Image.open(StringIO(req.content))
rColor, gColor, bColor = theImage.getpixel((1, 1))
answerColor = str(rColor) + ';' + str(gColor) + ';' + str(bColor)
data = {'color': answerColor, 'submit': '1'}

# Sending our cookies, data and headers (referer required for mission)
req = requests.post(target, cookies=cookies, data=data, headers=headers)

print('+++ Successfully sent information.\n') 
print(req.content)

