from datetime import datetime

def driverPath():
    return "/Usr/local/bin"

def baseUrl():
    return "http://10.4.79.56:8080/utf"

#change time to str

def getCurrentTime():
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format)

# Get time diff
def timeDiff(starttime,endtime):
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.strptime(endtime,format) - datetime.strptime(starttime,format)