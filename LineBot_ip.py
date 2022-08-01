from linebot import LineBotApi
from linebot.models import TextSendMessage
import netifaces as ni
import subprocess


CHANNEL_ACCESS_TOKEN = "your access token"

ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']
#print(ip)

subprocess.run("ping cccc5555.ddns.net -c5 | grep rtt > ping.txt",shell=True)
# cat ping,txt

f=open("ping.txt","r")
f2=f.read()
data=f2.split("/")

if float( data[4] )<1.0:
    net="良好"
else:
    net="稍慢"
f.close()

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
line_bot_api.broadcast(TextSendMessage(text = "Sherlin的日誌已經啟動。 IP:"+ ip +",網路狀態"+net))

