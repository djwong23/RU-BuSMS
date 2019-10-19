from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if "yo angelo" in body.lower():
        resp.message("🗿")
    elif "livi to busch" in body.lower() or "busch to livi" in body.lower():
        resp.message("Take B!")
    elif "college ave to livi" in body.lower() or "livi to college ave" in body.lower():
        resp.message("Take LX!")
    elif "busch to college ave" in body.lower() or "busch to college ave" in body.lower():
        resp.message("Take A or H!")
    elif "college ave to cook" in body.lower() or "cook to college ave" in body.lower():
        resp.message("Take EE or F!")
    elif "livi to cook" in body.lower() or "cook to livi" in body.lower():
        resp.message("Take REXL!")
    elif "busch to cook" in body.lower() or "cook to busch" in body.lower():
        resp.message("Take REXB!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
