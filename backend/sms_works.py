from flask import Flask, request
from flask_ngrok import run_with_ngrok
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import lxml
from lxml.html.clean import Cleaner
import requests, time

app = Flask(__name__)
run_with_ngrok(app)

number = "+16475593038"

cleaner = Cleaner()
cleaner.javascript = True
cleaner.style = True

with open("backend/twilio_settings.txt", "r") as file:
    account_sid, auth_token = file.read().splitlines()
client = Client(account_sid, auth_token)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    url = request.form["Body"]
    # resp = lxml.html.tostring(cleaner.clean_html(lxml.html.parse(url))).decode("utf-8")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"}
    # resp = lxml.html.tostring(cleaner.clean_html(requests.get(url, headers=headers).text)).decode("utf-8")
    resp = lxml.html.tostring(cleaner.clean_html(lxml.html.fromstring(requests.get(url, headers=headers).content))).decode("utf-8")
    # resp = """<div>Google<body><div id="mngb"> <div id="gb"><div id="gbw"><div id="gbz"><span class="gbtcb"></span><ol id="gbzc" class="gbtc"><li class="gbt"><a class="gbzt gbz0l gbp1" id="gb_1" href="https://www.google.ca/webhp?tab=ww"><span class="gbtb2"></span><span class="gbts">Search</span></a></li><li class="gbt"><a class="gbzt" id="gb_2" href="http://www.google.ca/imghp?hl=en&amp;tab=wi"><span class="gbtb2"></span><span class="gbts">Images</span></a></li><li class="gbt"><a class="gbzt" id="gb_8" href="http://maps.google.ca/maps?hl=en&amp;tab=wl"><span class="gbtb2"></span><span class="gbts">Maps</span></a></li><li class="gbt"><a class="gbzt" id="gb_78" href="https://play.google.com/?hl=en&amp;tab=w8"><span class="gbtb2"></span><span class="gbts">Play</span></a></li><li class="gbt"><a class="gbzt" id="gb_36" href="http://www.youtube.com/?gl=CA&amp;tab=w1"><span class="gbtb2"></span><span class="gbts">YouTube</span></a></li><li class="gbt"><a class="gbzt" id="gb_5" href="http://news.google.ca/nwshp?hl=en&amp;tab=wn"><span class="gbtb2"></span><span class="gbts">News</span></a></li><li class="gbt"><a class="gbzt" id="gb_23" href="https://mail.google.com/mail/?tab=wm"><span class="gbtb2"></span><span class="gbts">Gmail</span></a></li><li class="gbt"><a class="gbzt" id="gb_49" href="https://drive.google.com/?tab=wo"><span class="gbtb2"></span><span class="gbts">Drive</span></a></li><li class="gbt"><a class="gbgt" id="gbztm" href="https://www.google.ca/intl/en/about/products?tab=wh"><span class="gbtb2"></span><span id="gbztms" class="gbts gbtsa"><span id="gbztms1">More</span><span class="gbma"></span></span></a><div class="gbm" id="gbd"><div id="gbmmb" class="gbmc gbsb gbsbis"><ol id="gbmm" class="gbmcc gbsbic"><li class="gbmtc"><a class="gbmt" id="gb_24" href="https://www.google.com/calendar?tab=wc">Calendar</a></li><li class="gbmtc"><a class="gbmt" id="gb_51" href="http://translate.google.ca/?hl=en&amp;tab=wT">Translate</a></li><li class="gbmtc"><a class="gbmt" id="gb_10" href="https://books.google.ca/bkshp?hl=en&amp;tab=wp">Books</a></li><li class="gbmtc"><a class="gbmt" id="gb_6" href="https://www.google.ca/shopping?hl=en&amp;source=og&amp;tab=wf">Shopping</a></li><li class="gbmtc"><a class="gbmt" id="gb_30" href="http://www.blogger.com/?tab=wj">Blogger</a></li><li class="gbmtc"><a class="gbmt" id="gb_27" href="http://www.google.ca/finance?tab=we">Finance</a></li><li class="gbmtc"><a class="gbmt" id="gb_31" href="https://photos.google.com/?tab=wq&amp;pageId=none">Photos</a></li><li class="gbmtc"><a class="gbmt" id="gb_12" href="http://video.google.ca/?hl=en&amp;tab=wv">Videos</a></li><li class="gbmtc"><a class="gbmt" id="gb_25" href="https://docs.google.com/document/?usp=docs_alc">Docs</a></li><li class="gbmtc"><div class="gbmt gbmh"></div></li><li class="gbmtc"><a href="https://www.google.ca/intl/en/about/products?tab=wh" class="gbmt">Even more &#187;</a></li></ol><div class="gbsbt"></div><div class="gbsbb"></div></div></div></li></ol></div><div id="gbg"><h2 class="gbxx">Account Options</h2><span class="gbtcb"></span><ol class="gbtc"><li class="gbt"><a target="_top" href="https://accounts.google.com/ServiceLogin?hl=en&amp;passive=true&amp;continue=http://www.google.com/" id="gb_70" class="gbgt"><span class="gbtb2"></span><span id="gbgs4" class="gbts"><span id="gbi4s1">Sign in</span></span></a></li><li class="gbt gbtb"><span class="gbts"></span></li><li class="gbt"><a class="gbgt" id="gbg5" href="http://www.google.ca/preferences?hl=en" title="Options"><span class="gbtb2"></span><span id="gbgs5" class="gbts"><span id="gbi5"></span></span></a><div class="gbm" id="gbd5"><div class="gbmc"><ol id="gbom" class="gbmcc"><li class="gbkc gbmtc"><a class="gbmt" href="/preferences?hl=en">Search settings</a></li><li class="gbmtc"><div class="gbmt gbmh"></div></li><li class="gbkp gbmtc"><a class="gbmt" href="http://www.google.ca/history/optout?hl=en">Web History</a></li></ol></div></div></li></ol></div></div><div id="gbx3"></div><div id="gbx4"></div></div> </div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" width="272" id="hplogo"><br><br></div><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&#160;</td><td align="center" nowrap><div class="ds"></div><br><span class="ds"><span class="lsbb"></span></span><span class="ds"><span class="lsbb"></span></span></td><td class="fl sblc" align="left" nowrap width="25%"><a href="/advanced_search?hl=en-CA&amp;authuser=0">Advanced search</a></td></tr></table><div id="gac_scont"></div><div><br><div id="gws-output-pages-elements-homepage_additional_languages__als"><div id="SIvCob">Google offered in:  <a href="http://www.google.com/setprefs?sig=0_hWU8bOb1-alGuEb4URZjzdP_Azk%3D&amp;hl=fr&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjo07nM7NTnAhUHl3IEHXmYBioQ2ZgBCAU">Franis</a>  </div></div></div><span id="footer"><div><div id="fll"><a href="/intl/en/ads/">Advertising&#160;Programs</a><a href="/services/">Business Solutions</a><a href="/intl/en/about.html">About Google</a><a href="http://www.google.com/setprefdomain?prefdom=CA&amp;prev=http://www.google.ca/&amp;sig=K_ZYUC0IYSu18zbpAGv1n6X_PQm54%3D">Google.ca</a></div></div><p>&#169; 2020 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center>        </body></div>"""
    # return f"<Response><Message>{resp}</Message></Response>"

    limit = 150
    sp = [resp[i:i+limit] for i in range(0, len(resp), limit)]
    print(len(sp))
    msgs = client.messages.create(body=str(len(sp)), from_=number,to=request.form["From"])
    for i in range(len(sp)):
        s = sp[i]
        time.sleep(.4)
        msgs = client.messages.create(body=str(i)+" "+s, from_=number, to=request.form["From"])
        print(msgs.status)
    return ""

if __name__ == "__main__":
    app.run()
