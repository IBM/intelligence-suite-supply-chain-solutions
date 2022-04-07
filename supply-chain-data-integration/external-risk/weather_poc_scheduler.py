from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import TwcGetData
import TwcTransformData
import requests as re

def uploadData():
    now = datetime.datetime.now()
    TwcGetData.getData(now)
    TwcTransformData.transformWeatherAtTime(now)

    tenantId = "<<YOUR-TENANT-ID>>"
    header={"Content-Type":"application/x-www-form-urlencoded", "x-amz-tagging": "tenantId="+tenantId}
    body={
        "apikey":"<<YOUR-COS-APIKEY>>",
        "response_type":"cloud_iam", 
        "grant_type":"urn:ibm:params:oauth:grant-type:apikey"
        }
    r = re.post('https://iam.cloud.ibm.com/identity/token', data=body, headers=header)

    accessToken = r.json()['access_token']

    header["authorization"] = "Bearer "+str(accessToken)

    fileName = 'twc_alerts_severe_transformed_'+ str(datetime.datetime.strftime(now, "%Y%m%d_%H%M")) +'.json'
    files = {'ExternalEvent': open('output_json/'+fileName,'rb')}
    r = re.put(
        "https://s3.us.cloud-object-storage.appdomain.cloud/ih-data-ingest/SCIS/resources/tenants/"+tenantId+"/transformedData/"+fileName,
        files=files,
        headers=header
        )

    print(r.status_code)

uploadData()
# -- doesn't work --
# scheduler = BlockingScheduler()
# scheduler.add_job(uploadData(), 'interval', hours=1)
# scheduler.start()
