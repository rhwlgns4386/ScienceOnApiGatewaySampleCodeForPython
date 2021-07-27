import requests
from urllib import parse

target="RECOMMEND"
clientID = "Your ClientId"
accessToken = "Your AccessToken"

if __name__=='__main__':

    recomType = "merge"
    cn = "NART95824392"
    uid = "cchh7549"

    """ 추천을 할려는 유형,cn,uid를 입력 받아 콘텐츠 추천 api에 request를 요청하고 response를 받는다. """
    target_URL = ("https://apigateway.kisti.re.kr/openapicall.do?" +
                "client_id=" +clientID+
                "&token="+accessToken+"" +
                "&version=1.0" +
                "&action=browse" +
                "&target=" +target+
                "&recomType="+recomType+
                "&cn="+cn+
                "&uid="+uid)

    resonse=requests.get(target_URL)
    print(resonse.text)