import json
import datetime
import unicodedata

def transformWeatherAtTime(timeGiven: datetime):
  print("Time transformed: ", timeGiven)
  time = datetime.datetime.strftime(timeGiven, "%Y%m%d_%H%M")
  #set time to whatever you want to generate items for.
  now = datetime.datetime.now()
  with open('source_consolidated_json/twc_alerts_severe_source_' + time + '.json') as f:
    data = json.load(f)

  with open('output_json/twc_alerts_severe_transformed_'+ time +'.json', 'w', encoding='utf-8') as f:
    for i in range(len(data["alerts"])):
      
      temp = {}    
      upsertObject = {"eventCode": "objectUpsertEvent", "eventDetails": {"businessObject":temp}}

      alert = data["alerts"][i]
      temp["type"] = "ExternalEvent"
      temp["globalIdentifiers"] = [{"name": "sterlingSupplyChain.globalId", "value": "twc." + alert["detailKey"] + "." + alert["phenomena"]}]
      #temp["category"] = alert["categories"][0]["category"]
      temp["subject"] = alert["eventDescription"]
      temp["description"] = str(alert["headlineText"]) +" - " + str(alert["areaName"]) + ", " + str(alert["adminDistrict"]) + ", " + str(alert["countryName"])
      temp["extrnalEventSubtype"] = alert["phenomena"]
      if alert["adminDistrict"] != None:
        temp["stateProvince"] = alert["adminDistrict"] 

      temp["areaCounty"] = alert["areaName"]
      temp["country"] = alert["countryName"]
      temp["severity"] = alert["severity"]

      #time logic
      onsetTimeLocal = datetime.datetime.strptime(alert["onsetTimeLocal"], '%Y-%m-%dT%H:%M:%S%z') if alert["onsetTimeLocal"] != None else None
      expireTimeLocal = datetime.datetime.strptime(alert["expireTimeLocal"], '%Y-%m-%dT%H:%M:%S%z') if alert["expireTimeLocal"] != None else None
      if (now > expireTimeLocal.utcfromtimestamp(expireTimeLocal.timestamp())):
        temp["status"] = "Past"
      else:
        if onsetTimeLocal == None or (now > onsetTimeLocal.utcfromtimestamp(onsetTimeLocal.timestamp())):
          temp["status"] = "Active"
        else:
          temp["status"] = "Future"

      temp["dateRaised"] = alert["issueTimeLocal"]
      temp["start"] = alert["onsetTimeLocal"]

      temp["forecastedEnd"] = alert["expireTimeLocal"]
      temp["locationCoordinates"] = str(alert["latitude"]) + ", " + str(alert["longitude"])
      temp["radius"] = float(10.0) #hardcoded for now
      temp["eventSource"] = "TWC"

      sourceInfo = [alert["officeName"], alert["officeAdminDistrictCode"], alert["officeCountryCode"], alert["source"], alert["disclaimer"]]
      sourceInfo = filter(None, sourceInfo)
      temp["attribution"] = "Issued by " + ", ".join(sourceInfo) + "."


      if now > expireTimeLocal.utcfromtimestamp(expireTimeLocal.timestamp()):
        temp["actualEnd"] = str(datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S%z')) 

      f.write(json.dumps(upsertObject, ensure_ascii=False) + "\n")

