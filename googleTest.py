# Python program to get a set of 
# places according to your search 
# query using Google Places API 

# importing required modules 
import requests, json 
from shapely.geometry import Point, Polygon
# enter your api key here 
api_key = 'AIzaSyAAwuExTdfzuBbRtB1RufGzcUBzmV4YYIY'

# url variable store url 
url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

# The text string on which to search 
query = input('Search query: ') 

# get method of requests module 
# return response object 
r = requests.get(url + 'input=' + query +
						'&key=' + api_key +
                        '&inputtype=textquery' +
                        '&fields=formatted_address,geometry,name')
                        

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
#college ave polygon
poly = Polygon([(40.490120, -74.441927), (40.492946, -74.452363), (40.499675, -74.463924), (40.507467, -74.452110), (40.500351, -74.443845)])
if poly.contains(pt) :
    campus = 'college ave'
print (campus)

"""
# keep looping upto lenght of y 
for i in range(len(y)): 
	
	# Print value corresponding to the 
	# 'name' key at the ith index of y 
	print(y[i]['name']) 
"""