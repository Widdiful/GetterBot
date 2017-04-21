import ftputil, urllib, datetime, time

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
with open('imgindex.txt', 'w') as f:
    f.write("\n" + str([ftp.path.join(path, filename)
        for path, dirs, files in ftp.walk('')
        for filename in files]))
print "[" + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + "] Image Index created"