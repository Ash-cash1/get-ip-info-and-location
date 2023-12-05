import requests
import json
import logging 
try:
  inp = input("Please enter an ip: ")

  header = {"Accept": "application/json"}
  response = requests.get(f"http://ip-api.com/json/{inp}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
  val = response.json()
  lang = val["lat"]
  lin = val["lon"]
  print("OK: "+str(response.ok))

  print(val)
  inpfn = input("please enter a file name to make (please add .jpeg at the end of the file name): ")
  re = requests.get(f"https://maps.geoapify.com/v1/staticmap?apiKey=647699309aa547cebfee5adc9007171c&style=osm-bright&width=600&height=800&format=jpeg&center=lonlat:{lin},{lang}")
  filef = re.content
  with open(inpfn,"wb") as file:
      file.write(filef)
  print(f"made a file {inpfn}.This contains the picture")
except ValueError as e:
  logging.error(e)  
except KeyError as e:
  logging.error(e)
  print("If the error says 'lat' you most likely did not add an ip.Please try again")
