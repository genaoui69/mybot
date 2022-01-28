import time
import requests 
from time import sleep
myIGs = ["ogenaoui" , "iheeb_ounissi" , "slim.harvvy" , "ramitabi69" , "rami6.969" , "rami.7694" , "fahefeb386" , 'dualivting' , "alexsandra.terner" , "zero.tow69" , "lami000123" , "stofanri30" , "serina.gomez__" , "maria.ustrulla" , "benyedeer_10" , "siskobramss_01" , "iamhero_omg"]

url="http://zux021.xyz/dezgi/dore/Add.php"


head = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" ,
    "Accept-Encoding" : "gzip, deflate" ,
    "Accept-Language" : "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7" ,
    "Cache-Control" : "max-age=0" ,
    "Connection" : "keep-alive" ,
    "Content-Length" : "48" ,
    "Content-Type" : "application/x-www-form-urlencoded" ,
    "Host" : "zux021.xyz" ,
    "Origin" : "http://zux021.xyz" ,
    "Referer" : "http://zux021.xyz/dezgi/dore/" ,
    "Upgrade-Insecure-Requests" : "1" ,
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
b = 0
while 0 < 100:
  i = 0
  while i < len(myIGs):
    print('sending to ==> ' + myIGs[i] )
    data ={
    'id': myIGs[i] ,
    'count' : '200' ,
    'lic': 'Genaoui69',
    'submit': 'Login'
}
    login = requests.post(url,headers=head,data=data).status_code
    print (login)
    print('Your Order In Progress')
    print('WAIT 20 SECEND FOR NEXT')
    time.sleep(60)
    i+=1
  b+=1