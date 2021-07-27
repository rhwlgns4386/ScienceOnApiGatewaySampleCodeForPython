import requests

target="ATT"
clientID = "Your ClientId"
accessToken = "Your AccessToken"

if __name__=='__main__':

    cn = "GTB2020005723"

    target_URL = ("https://apigateway.kisti.re.kr/openapicall.do?" +
    "client_id=" + clientID +
    "&token=" + accessToken +
    "&version=1.0" +
    "&action=browse" +
    "&target=" + target +
    "&cn=" + cn)

    """ cn을 입력하여 동향 상세보기 api에 request를 요청하고 response를 받는다. """
    resonse=requests.get(target_URL)
    print(resonse.text)