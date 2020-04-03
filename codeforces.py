import hashlib
import datetime
import requests

api_key = "xxx"
secret_key = "yyy"



ts = str(int(datetime.datetime.now().timestamp()))
string = '123456/contest.hacks?apiKey=' + api_key + '&contestId=1332&time=' + ts + '#' + secret_key
result = hashlib.sha512(string.encode())

hexa = result.hexdigest()

response = requests.get('https://codeforces.com/api/contest.hacks?contestId=1332&apikey=' + api_key + "&time=" + ts +
 '&apiSig=123456' + hexa)

print(response.status_code)