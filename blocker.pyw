import time
from datetime import datetime as dt

#host_path = "C:\Windows\System32\drivers\etc"
host_path = "hosts" #Always pass absolute path if you wish to use this script in task scheduler

redirect = "127.0.0.1"
website_to_blk = ["www.youtube.com", "www.facebook.com"]


while True:
    #Setting lower thershold and upper threshold datetime object
    lt_dt = dt(dt.now().year, dt.now().month, dt.now().day, 10)
    ut_dt = dt(dt.now().year, dt.now().month, dt.now().day, 20)
    if lt_dt < dt.now() < ut_dt:
        print("working hours")
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_to_blk:
                if website in content:
                    #Already added
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
                #print(content)
    else :
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for lines in content:
                if not any(web in lines for web in website_to_blk):
                    file.write(lines)
                else:
                    print("else")
            file.truncate()
        print("Sleeping")
    time.sleep(5)


# To run python scripts on background we use pythonw.exe
# rename the file to .pyw
#