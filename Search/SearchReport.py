from urllib import parse
import requests



target="REPORT"
clientID = "Your ClientId"
accessToken = "Your AccessToken"

if __name__=='__main__':

    """
    검색어를 인코딩 합니다.
    검색어 필드에 관한것은 ScienceOn Api GateWay를 참고 해주세요.
    """
    query = parse.quote("{\"BI\":\"코로나\"}")

    target_URL = ("https://apigateway.kisti.re.kr/openapicall.do?"+
    "client_id=" +clientID+
    "&token="+accessToken+
    "&version=1.0"+
    "&action=search"+
    "&target="+target+
    "&searchQuery="+query)


    """ 검색할 쿼리를 입력하여 보고서 검색 api에 request를 요청하고 response를 받는다. """
    resonse=requests.get(target_URL)
    print(resonse.text)