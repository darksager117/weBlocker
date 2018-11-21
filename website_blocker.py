import time
from datetime import datetime as dt


host_temp= r"C:\Windows\System32\drivers\etc\hosts"   #In order to not be taken as a special character, add the "r" before the string
redirect= "127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "www.youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,14):
        print("Working hours....")
        with open(host_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " "+ website +"\n")

    else:
        with open(host_temp, 'r+') as file:
            content=file.readlines()  #Se toma cada linea como una lista para seleccionar lo que se va a cambiar
            file.seek(0)   #se coloca el puntero al inicio
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
            print("fun hours..")
    time.sleep(1)
