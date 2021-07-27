import requests


target="VOLUME"
clientID = "Your ClientId"
accessToken = "Your AccessToken"

if __name__=='__main__':

    cn = "NJOU00023797"
    volno = "3"

    """ cn과 volno를 입력받아 kisti의 권호정보를 반환 받습니다. """
    target_URL = ("https://apigateway.kisti.re.kr/openapicall.do?" +
                "client_id=" +clientID+
                "&token="+accessToken+
                "&version=1.0" +
                "&action=toc" +
                "&target=" +target+
                "&cn="+cn+
                "&volno="+volno)

    resonse=requests.get(target_URL)
    print(resonse.text)