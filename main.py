import os
import time
import requests

def download(url: str, destination: str):
  url.replace(' ', '%20') # space URL encoding
  res = requests.get(url, stream=True)
  if url.endswith('.pdf'):
    if not os.path.exists(destination):
      os.makedirs(destination)
    with open(f"{destination}/{url.split('/')[-1].split('?')[-1]}", 'wb') as f:
      for chunk in res.iter_content(2000):
        f.write(chunk)
  else:
    try:
      data = json.loads(res.content.decode('utf-8'))
      if data['message']:
        return data['message']
      return data
    except Exception as e:
      return e

download('https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', 'out')