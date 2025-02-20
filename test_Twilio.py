from twilio.rest import Client

TWILIO_SID = "xxxxxxx"
TWILIO_AUTH_TOKEN = "xxxxxx"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+123456789"
RECIPIENT_WHATSAPP_NUMBER = "whatsapp:+123456789"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    from_=TWILIO_WHATSAPP_NUMBER,
    body="🔔 Test WhatsApp message from Twilio!",
    to=RECIPIENT_WHATSAPP_NUMBER
)

print(f"📩 Message sent successfully! SID: {message.sid}")
