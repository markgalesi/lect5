from twilio.rest import Client
import os

twilio_auth_token=os.environ['TWILIO_AUTH_TOKEN']
twlio_account_sid=os.environ['TWILIO_ACCOUNT_SID']
client = Client(twlio_account_sid, twilio_auth_token)

message = client.messages.create(body="waddup hoe\n-mark", from_="+14063447617",to="+19737673445")

print(message.sid)
print("OI")