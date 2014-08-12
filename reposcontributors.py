import requests
import json
import sys

mytoken = 'get this from profile'
url = 'https://api.github.com/repos/docker/docker/contributors'
headers = { 'Authorization' : 'token ' + mytoken }
csv='"{login}","{avatar_url}","{html_url}","{contributions}"'

#-------- MAIN ----------
print csv

while True:

  # Get a list of all the contributors
  resp=requests.get(url, headers=headers)

  for r in resp.json():
      print csv.format(
          login=r['login'],
          avatar_url=r['avatar_url'],
          html_url=r['html_url'],
          contributions=r['contributions']
          )


  if ("next" in resp.links and "url" in resp.links["next"] and len(resp.links["next"]["url"])):
      url=resp.links['next']['url']
  else:
      break

