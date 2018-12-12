from twilio.rest import Client

f = open("twilio.txt")
for line in f:
    if line.split(":")[0] == 'ACCOUNT SID':
        account_sid = line.split(":")[1]
    elif line.split(":")[0] == 'AUTH TOKEN':
        auth_token=line.split(":")[1]
f.close()

message = '你知道我是谁么？！'
client = Client(account_sid, auth_token)
client.messages.create(to='+8618703657865',from_='+19158000960',body=message)

