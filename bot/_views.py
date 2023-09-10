from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, ImageSendMessage, LocationMessage, LocationSendMessage
import random
from crawler.main import get_lottory, get_big_lottory
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parse = WebhookParser(settings.LINE_CHANNEL_SECRET)

# Create your views here.


def index(request):
    return HttpResponse("index")


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parse.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            if isinstance(event, MessageEvent):
                text = event.message.text

                if text == "1":
                    message = TextSendMessage(text='早安')
                elif text == "2":
                    message = TextSendMessage(text='午安')
                elif "樂透" in text:
                    message = TextSendMessage(text=get_big_lottory())
                elif "捷運" in text:
                    if "台中" in text:
                        img_url = 'https://assets.piliapp.com/s3pxy/mrt_taiwan/taichung/20201112_zh.png?v=2'

                    elif '高雄' in text:
                        img_url = 'https://assets.piliapp.com/s3pxy/mrt_taiwan/kaohsiung/202210_zh.png'
                    else:
                        img_url = 'https://assets.piliapp.com/s3pxy/mrt_taiwan/taipei/20230214_zh.png'
                    message = ImageSendMessage(original_content_url=img_url,
                                               preview_image_url=img_url)
                elif '台北車站' in text:
                    message = LocationSendMessage(
                        title='台北車站', address='100台北市中正區北平西路3號1樓', latitude=25.047778, longitude=121.517222)
                else:
                    message = TextSendMessage(text="我不知道你在說什麼")

                # if event.message.text=='hello':
                line_bot_api.reply_message(
                    event.reply_token,
                    message
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
