import requests

# Making a GET request

r = requests.get('https://quote.eastmoney.com/center/gridlist.html#sh_a_board')

# check the status code for the response received
# The success code - 200

# print(r)

# print the content of the request

print(r.content)