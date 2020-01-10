import requests
from urllib.parse import quote

lua = '''
function main(splash, args)
  splash:go("https://www.geekdigging.com/")
    return {
      url = splash:url(),
      jpeg = splash:jpeg(),
      har = splash:har(),
      cookies = splash:get_cookies()
    }
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)