import requests

url = "https://www.businessforsale.com/login.html"

payload = "{\"username\": \"random1k11@yandex.ru\", \"password\": \"dima1994\", \"login\": \"Login\", \"usertype\": \"1\", \"controller\": \"login\", \"user_id\": \"\", \"mod\": \"mod_index\", \"previousUrl\": \"https://poland.businessforsale.com/\"}\n"
headers = {
    'https': "//www.businessforsale.com/login.html",
    'cache-control': "no-cache",
    'postman-token': "d7d3eb64-dcc2-99f6-701e-4d5a20f441bb"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
