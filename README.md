# GetterBot
Tweets random Getter Robo frames

# How it works
imagegen.py is used to create a large index of several hundred thousand images hosted on a remote server.
getterbot.py is then used to read this index every 30 minutes and posts one at random to Twitter.

ftpinfo.txt and twitinfo.txt must be filled out appropriately in order for these Python files to function.

# Why is it here
This code can be freely used to create imagebots of any nature, without credit.

# Alternate files
imagegen_unbiased.py and getterbot_unbiased.py are slightly more basic programs that have the same functions, but every image in every folder has an equal chance of being picked, instead of each "show" having an equal chance of being picked.

getterbot_standalone.py can be used to bypass having to create the image index with a different program, but should only be used for smaller imagebots as it is very intensive. You can also bypass having to use external files for the sensitive Twitter and FTP information to have just one file to make the bot run.

getterbot_local.py can be used by those who want to store all the images locally, instead of having them hosted on a remote server.