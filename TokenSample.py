import xml.etree.ElementTree as ET
from urllib import parse
import requests
import traceback
import AES256Util
import datetime
import re
import json


################################################### 사용자 정보 입력 #####################################################
# 맥주소 입력하세요.
MAC_address = "Your Mac Address"
# 발급받은 client_id를 입력하세요.
clientID = "Your clientId"
# 발급받은 인증키를 입력해주세요.
key = "Your key"
#######################################################################################################################
refreshToken = "Your RefreshToken"
accessToken = "Your AccessToken"




# Access Token 및 Refresh Token 발급
def createToken():
    time = ''.join(re.findall("\d", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    plain_txt = json.dumps({"datetime": time, "mac_address": MAC_address}).replace(" ", "")

    encryption = AES256Util.AESTestClass(plain_txt, key)
    encrypted_txt = encryption.encrypt()
    target_URL = "https://apigateway.kisti.re.kr/tokenrequest.do?client_id=" + clientID + "&accounts=" + encrypted_txt

    try:
        response = requests.get(target_URL)
        # API 호출 결과값 출력
        print(response.text)

        # 발급된 토큰(Refresh Token, Access Token) global 변수 입력
        json_object = json.loads(response.text)
        global refreshToken, accessToken
        refreshToken = json_object['refresh_token']
        accessToken = json_object['access_token']
        print(refreshToken)
        print(accessToken)
        return response
    except Exception:
        traceback.print_exc()


# Access Token 재발급
def getAccessToken():
    target_URL = "https://apigateway.kisti.re.kr/tokenrequest.do?refreshToken=" + refreshToken + "&client_id=" + clientID

    try:
        response = requests.get(target_URL)
        # API 호출 결과값 출력
        if 'errorCode' in response:
            # 발급된 토큰(Access Token) 변수 입력
            json_object = json.loads(response.text)
            global accessToken
            accessToken = json_object['access_token']
        return response.text
    except Exception:
        traceback.print_exc()


if __name__=="__main__":
    """
    최초 token요청을 합니다.
    RefreshToken과 AccessToken을 발급 받습니다.
    """
    tokenResponse=createToken()
    print(tokenResponse)

    """
    데이터를 요청하고 그에 맞는 데이터를 받습니다.
    하단의 코드는 예제코드이며 자세한 내용은 ScienceOn ApiGateWay를 참조해주세요.
    """
    query=parse.quote("{\"BI\":\"코로나\"}")
    target_URL = ("https://apigateway.kisti.re.kr/openapicall.do?"+
    "client_id=" +clientID+
    "&token="+accessToken+
    "&version=1.0"+
    "&action=search"+
    "&target=ARTI"+
    "&searchQuery="+query)

    response=requests.get(target_URL)
    print(response.text)

    """
    AccessToken만료시 AccessToken를 재발급합니다.
    AccessToken요청시 E4106번이 떨어지면 RefreshToken 만료된 것 입니다.
    """

    tokenXml=ET.fromstring(response.text)
    statusCode=tokenXml.find('resultSummary/statusCode').text
    if(int(statusCode)!=200):
        if(tokenXml.find('errorDetail/errorCode').text=='E4103'):
            print("AccessToken이 만료 되었습니다.")
            accessTokenResponse=getAccessToken()
            if 'errorCode' in accessTokenResponse:
                print("RefreshToken이 만료 되었습니다.")
                createToken()
