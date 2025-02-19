from twilio.rest import Client

TWILIO_SID = "AC49a57e4cbba9b64d6af528563c30dfe9"
TWILIO_AUTH_TOKEN = "3ecfd8e02ecb0be529ede249fa9446bd"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"
RECIPIENT_WHATSAPP_NUMBER = "whatsapp:+40770558577"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    from_=TWILIO_WHATSAPP_NUMBER,
    body="🔔 Test WhatsApp message from Twilio!",
    to=RECIPIENT_WHATSAPP_NUMBER
)

print(f"📩 Message sent successfully! SID: {message.sid}")
