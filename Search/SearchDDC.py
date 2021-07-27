from urllib import parse
import requests


target="DDC"
clientID = "Your ClientId"
accessToken = "Your AccessToken"

if __name__=='__main__':

    query = "science"

    target_URL = ("https://apigateway.kisti.re.kr/openapicall.do?"+
    "client_id=" +clientID+
    "&token="+accessToken+
    "&version=1.0"+
    "&action=search"+
    "&target="+target+
    "&subject="+query)

    """ 검색할 주제어를 입력하여 주제분류 api에 request를 요청하고 response를 받는다. """
    resonse=requests.get(target_URL)
    print(resonse.text)