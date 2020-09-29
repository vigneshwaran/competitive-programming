"""
    Codeforces api login
"""
import hashlib
import datetime
import requests

API_KEY = "xxx"
SECRET_KEY = "yyy"



time_stamp = str(int(datetime.datetime.now().timestamp()))
url = '123456/contest.hacks?apiKey=' + API_KEY + '&contestId=1332&time=' + \
            time_stamp + '#' + SECRET_KEY
result = hashlib.sha512(url.encode())

hexa = result.hexdigest()

response = requests.get('https://codeforces.com/api/contest.hacks?contestId=1332&apikey=' +
                        API_KEY + "&time=" + time_stamp +
                        '&apiSig=123456' + hexa
                        )
print(response.status_code)
