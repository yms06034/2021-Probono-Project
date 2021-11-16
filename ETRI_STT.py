import urllib3 
import json 
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "5b0f6b15-749b-4009-b066-95d5729d8423"
languageCode = "korean"
 

def stt(audioFilePath):
    file = open(audioFilePath, "rb")
    audioContents = base64.b64encode(file.read()).decode("utf8")
    file.close()
 
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "language_code": languageCode,
            "audio": audioContents
        }
    }
 
    http = urllib3.PoolManager()
    response = http.request(
        "POST", 
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
 
    data = json.loads(response.data.decode("utf-8", errors='ignore'))    


    return data['return_object']['recognized']

if __name__ == "__main__":
    print("it's success")
