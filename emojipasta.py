from flask import Flask, request
import requests
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import googlemaps
import os
import requests, json 
from shapely.geometry import Point, Polygon
import datetime


app = Flask(__name__)


@app.route("/sms", methods = ['GET', 'POST'])
# request = requests.get('https://maps.googleapis.com/maps/api/js?key=AIzaSyAAwuExTdfzuBbRtB1RufGzcUBzmV4YYIY&callback=initMap')


def sms_reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    currentDT = datetime.datetime.now()
   

    if body.find(":", 0, len(body)) == -1 :
        starting = "" +body[0: body.find(" to ", 0, len(body))]
        end = "" + body[body.find(" to ", 0, len(body))+4:len(body)]
    else :
        currentDT = datetime.time(int(body[body.find(":", 0, len(body))-2:body.find(":", 0, len(body))]), int(body[body.find(":", 0, len(body))+1:len(body)]), 0)
        starting = "" + body[0: body.find(" to ", 0, len(body))]
        end = "" + body[body.find(" to ", 0, len(body))+4:body.find(":", 0, len(body))-2]

        print(starting)
        print(end)
        print(currentDT)
    directions = location_finder(starting) + " to " + location_finder(end)
    print(directions)

    
    

    if "livi to buschh" in directions.lower() or "buschh to livi" in directions.lower() or "buscha to livi" in directions.lower() or "livi to buscha" in directions.lower():
        if currentDT.hour > 6 or currentDT.hour < 2 or (currentDT.hour == 2 and currentDT.minute <20):
            resp.message("Take B!")
        else :
            resp.message("No Bus Route!")
    elif "college ave to livi" in directions.lower() or "livi to college ave" in directions.lower():
        if currentDT.hour > 6 or currentDT.hour < 2 or (currentDT.hour == 2 and currentDT.minute <15) :
            resp.message("Take LX!")
        else :
            resp.message("No Bus Route!")
    elif "buscha to college ave" in directions.lower() or "college ave to buscha" in directions.lower() or "buschh to college ave" in directions.lower() or "college ave to buschh" in directions.lower():
        if currentDT.hour > 7 and currentDT.hour < 21 :
            if "buscha to college ave" in directions.lower() or "college ave to buscha" in directions.lower():
                resp.message("Take A!")
            elif "buschh to college ave" in directions.lower() or "college ave to buschh" in directions.lower():
                resp.message("Take H!")            
        elif currentDT.hour > 6 or currentDT.hour < 2 or (currentDT.hour ==2 and currentDT.minute <30) :
                resp.message("Take H")
        else :
                resp.message("No Bus Route!")
    elif "college ave to cook" in directions.lower() or "cook to college ave" in directions.lower() or "college ave to douglass" in directions.lower() or "douglass to college ave" in directions.lower():
        if currentDT.hour > 7 and currentDT.hour < 21 :
            resp.message("Take EE or F!")
        elif currentDT.hour > 6 or currentDT.hour < 2 or (currentDT.hour == 2 and currentDT.minute < 15) :
            resp.message("Take EE!")
        else :
            resp.message("No Bus Route!")
    elif "livi to cook" in directions.lower() or "cook to livi" in directions.lower() or "livi to douglass" in directions.lower() or "douglass to livi" in directions.lower():
        if currentDT.hour > 7 and currentDT.hour < 23 :
            resp.message("Take REXL!")
        elif currentDT.hour > 6 or currentDT.hour < 2 or (currentDT.hour == 2 and currentDT.minute <15):
            resp.message("Take an LX and then an EE!")
        else :
            resp.message("No Bus Route!")
    elif "buscha to cook" in directions.lower() or "cook to buscha" in directions.lower() or "cook to buschh" in directions.lower() or "buschh to cook" in directions.lower():
        if currentDT.hour > 7 and currentDT.hour < 23 :
            resp.message("Take REXB!")
        elif currentDT.hour > 6 or currentDT.hour < 2 or (currentDT.hour == 2 and currentDT.minute <15):
            resp.message("Take an H and then an EE!")
        else :
            resp.message("No Bus Route!")
    else:
        resp.message("No Bus Route!")
    return str(resp)

def location_finder(a_string) :
    # enter your api key here 
    api_key = 'AIzaSyAAwuExTdfzuBbRtB1RufGzcUBzmV4YYIY'
    query = a_string

    # url variable store url 
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

    # get method of requests module 
    # return response object 
    r = requests.get(url + 'input=' + query + '&key=' + api_key +'&inputtype=textquery' +'&fields=formatted_address,geometry,name')
               

    # json method of response object convert 
    # json format data into python format data 
    x = r.json()
    print (x)
    # now x contains list of nested dictionaries 
    # we know dictionary contain key value pair 
    # store the value of result key in variable y 
    y = x['candidates'] 
    print ('\n')
    print (y)
    print (y[0]['geometry']['location'])
    z = (y[0]['geometry']['location'])
    pt = Point(z['lat'], z['lng']) 
    
    polyca = Polygon([(40.490120, -74.441927), (40.492946, -74.452363), (40.499675, -74.463924), (40.507467, -74.452110), (40.500351, -74.443845)])
    polyli = Polygon([(40.524985, -74.448393), (40.505837, -74.440712), (40.513665, -74.425476), (40.525278, -74.427106), (40.532097, -74.442729)]) 
    polycd = Polygon([(40.490120, -74.441927), (40.467900, -74.455505), (40.457437, -74.427237), (40.474610, -74.415324), (40.491094, -74.435263)])
    polybu = Polygon([(40.510755, -74.462606), (40.522043, -74.488226), (40.531242, -74.467326), (40.526509, -74.447241), (40.516821, -74.453554)]) 
    polybuA = Polygon([(40.510755, -74.462606), (40.521020, -74.460552),(40.529854, -74.461346), (40.526509, -74.447241), (40.516821, -74.453554)])
    polybuH = Polygon([(40.510755, -74.462606), (40.522043, -74.488226), (40.531242, -74.467326), (40.529854, -74.461346), (40.521020, -74.460552)])
    if polyca.contains(pt) :
        campus = 'college ave'
    elif polyli.contains(pt) :
        campus = 'livi'
    elif polycd.contains(pt) :
        campus = 'cook'
    elif polybuA.contains(pt) :
        campus = 'buscha'
    elif polybuH.contains(pt) :
        campus = 'buschh'
    else :
        campus = 'livi'
    return campus

if __name__ == "__main__":
    app.run(debug =True)













