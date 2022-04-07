import json
import requests as re
import datetime
import logging

countryCodes = ["AT", "AU", "BE", "BA" , "BG" , "CA" , "HR" , "CY" , "CZ" , "DK",
"EE" , "FI" , "FR" , "DE" , "GR" , "HU" , "IS" , "IE" , "IT" , "JP" , "LV",
"LT" , "LU" , "MK" , "MT" , "MD" , "ME" , "NL" , "NO" , "PL",
"PT" , "RO" , "RS" , "SK" , "SI" , "ES" , "SE" , "CH" , "UK" , "US"]
#countryCodes = ["JP", "US", "BG"] #For testing purposes (less calls)

def getData(timeGiven: datetime):

    #now = datetime.datetime.now()
    now = datetime.datetime.strftime(timeGiven, "%Y%m%d_%H%M")
    logging.basicConfig(filename='source_logs/twc_alerts_severe_source_'+ now +'.log', encoding='utf-8', level=logging.INFO)

    data = {}
    countryAlerts={"alerts": []}
    key = "<<YOUR_TWC_KEY>>"
    accountedCountries = {}

    for country in countryCodes:
        
        #initial GET call will use the mandatory params. 
        params = {'countryCode': country, 'format': 'json', 'language': 'en-US', "apiKey": key}
        next = 0
        alertCount = 0

        #looping until every page has been accounted for. 
        while (next != None):

            r = re.get("https://api.weather.com/v3/alerts/headlines?", params=params)

            if (r.status_code != 200):
                #Only set countrySum to None if this is the first time. 
                #If by some fluke it fails on a 'next' page, then it'll just return the current countrySum
                if next == 0:
                    alertCount = None
                next = None #setting next to none for while loop to exit
                continue

            data = r.json()

            for alert in data["alerts"]:
                if alert["severityCode"] < 3:
                    countryAlerts["alerts"].append(alert)
                    alertCount+=1
            
            #apply the next 'next' value for the inner loop to repeat (or not, if next == None)
            next = data["metadata"]["next"]
            params["next"] = next

        logging.info(country + ': ' + str(alertCount))

    #writing to file
    with open('source_consolidated_json/twc_alerts_severe_source_'+ now +'.json', 'w') as f:
        json.dump(countryAlerts,f, ensure_ascii=False)

