import ftputil, random, urllib, twitter, datetime, time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

#connect to twitter api
print "[" + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + "] CHAAAAAAAAAAAAAAAANGE GETTEEEEEEEEEEEEEEEEEEER OOOOOOOOOOOOOOOOOOOOONE"
with open('twitinfo.txt', 'a+') as f:
    twitinfo = f.readlines()
    twitinfo = [line.strip('\r\n') for line in twitinfo]
conKey = twitinfo[0]
conSec = twitinfo[1]
accKey = twitinfo[2]
accSec = twitinfo[3]
api = twitter.Api(consumer_key=conKey,
                  consumer_secret=conSec,
                  access_token_key=accKey,
                  access_token_secret=accSec)

#login to ftp
print "[" + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + "] Initialising..."
with open('ftpinfo.txt', 'a+') as f:
    ftpinfo = f.readlines()
    ftpinfo = [line.strip('\r\n') for line in ftpinfo]
ipadr = ftpinfo[0]
user = ftpinfo[1]
passw = ftpinfo[2]
ftp = ftputil.FTPHost(ipadr, user, passw)

#walk files in directory
fileinfo = []
for x in range(1, 8):
    fileinfo.append("\n" + str([ftp.path.join(path, filename)
        for path, dirs, files in ftp.walk(str(x))
        for filename in files]))
    print "[" + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + "] Done step " + str(x) + "/7"
print "[" + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + "] Image Index created"

#pick random file, generate tweet info
while True:
    now = datetime.datetime.now()
    if str(now.second) == '0':
        if int(now.minute)%30 == 0:
            showno = random.randint(1, 2)
            if int(showno) <= 3:
                type = "Episode "
            else:
                type = "Chapter "
            if int(showno) == 1:
                show = "Getter Robo Armageddon"
            elif int(showno) == 2:
                show = "Shin Getter Robo vs Neo Getter Robo"
            elif int(showno) == 3:
                show = "New Getter Robo"
            elif int(showno) == 4:
                show = "Getter Robo"
            elif int(showno) == 5:
                show = "Getter Robo G"
            elif int(showno) == 6:
                show = "Getter Robo Go"
            elif int(showno) == 7:
                show = "Shin Getter Robo"
            result = random.choice(fileinfo[showno - 1])
            resultName = result.split("/")[0] + " " + result.split("/")[1] + " " + result.split("/")[2]
            episode = resultName.split(" ")[1]
            frame = resultName.split(" ")[2]
            message = "From " + type + episode + " of " + show

            #tweet
            tweeted = api.PostMedia(message, 'http://www.widdiful.co.uk/GetterBot/' + result)
            print "[" + str(now.hour) + ":" + str(now.minute) + "] Tweeted image from " + type + episode + " of " + show + " (frame " + frame + ")"