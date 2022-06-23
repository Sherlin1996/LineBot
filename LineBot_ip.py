from linebot import LineBotApi
from linebot.models import TextSendMessage
import netifaces as ni

ni.ifaddresses('enp0s3')
ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']
print(ip)

CHANNEL_ACCESS_TOKEN = "Your CHANNEL_ACCESS_TOKEN"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
line_bot_api.broadcast(TextSendMessage(text = "get ip address :" + ip))

