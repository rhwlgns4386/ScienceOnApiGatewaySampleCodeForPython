import requests
from urllib import parse

target="RESOLVER"
clientID = "Your ClientId"
accessToken = "Your AccessToken"

if __name__=='__main__':

    paperTitle = "Association of p53 Expression with Metabolic Features of Stage I Non-Small Cell Lung Cancer"
    query = parse.quote(paperTitle)

    """ 검색할 쿼리를 입력하여 링크리졸버 api에 request를 요청하고 response를 받는다. """
    target_URL = ("https://apigateway.kisti.re.kr/openapicall.do?" +
                "client_id=" +clientID+
                "&token=" +accessToken+
                "&version=1.0" +
                "&action=resolver" +
                "&target=" +target+
                "&atitle="+query)

    resonse=requests.get(target_URL)
    print(resonse.text)