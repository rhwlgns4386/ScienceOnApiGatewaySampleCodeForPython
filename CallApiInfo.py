import time

import requests
from urllib import parse
import xml.etree.ElementTree as ET

clientID = "Your ClientId"
accessToken = "Your AccessToken"

if __name__=='__main__':
    cn="322433"

    """ CallApiInfo의 실행을 위해 연구원상세보기 api를 호출합니다.  """
    url=("https://apigateway.kisti.re.kr/openapicall.do?" +
    "client_id=" + clientID +
    "&token=" + accessToken +
    "&version=1.0" +
    "&action=browse" +
    "&target=RESEARCHER"+
    "&cn=" + cn)

    response=requests.get(url)
    print(response.text)

    """
    xml를 파싱후 CallAPIInfo의 API-001-01를 찾고 논문 검색 API를 호출합니다.
    """

    xmlRoot=ET.fromstring(response.text)
    callApiInfo=xmlRoot.findall('recordList/record/item[@metaCode="CallAPIInfo"]')
    for i in callApiInfo:
        if i.find('item[@metaCode="ProviderAPIId"]').text=="API-001-01":
            query = parse.quote(i.find('item[@metaCode="ParameterValue"]').text)
            target_URL = ("https://apigateway.kisti.re.kr/openapicall.do?" +
                          "client_id=" + clientID +
                          "&token=" + accessToken +
                          "&version=1.0" +
                          "&action=search" +
                          "&target=ARTI"+
                          "&searchQuery=" + query)

            resonse = requests.get(target_URL)

            print(resonse.text)