import urllib3 #URL(Uniform Resource Locator)을 가져오기 위한 파이썬 모듈
import json #노드의 현재 프로젝트에 대한 정보 저장
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "5b0f6b15-749b-4009-b066-95d5729d8423"
# audioFilePath = "C:\\Temp\\sbs.mp3"
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
        "POST", #임의의 데이터를 자신의 응용 프로그램으로 전송
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
 
    #print("[responseCode] " + str(response.status))
    #print("[responBody]")
    data = json.loads(response.data.decode("utf-8", errors='ignore'))    
    #print(data['return_object']['recognized'])

    return data['return_object']['recognized']

if __name__ == "__main__":
    print("it's success")
