import sys
import selenium
#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from seleniumwire import webdriver
from datetime import datetime
import time
import json
import pandas as pd





x = sys.argv[1]


def Number_of_Errores():
    file = open('demofile2.txt', 'r')
    Lines = file.readlines()
     
    DNS_Errore=0
    load_time = 0
    click_error =0
    # Strips the newline character
    for line in Lines:
        
        print( line.strip())
        if line.strip() == 'DNS_Error':
            DNS_Errore+=1
        if line.strip() == 'load_time_Error':
            load_time+=1
        if line.strip() == 'click_error':
            click_error+=1
    print(DNS_Errore)
    
    
    
def ss(X):
        X2=''
        for i in range (0,len(X)-1):
            
            if i<513:
                X2 += X[i]
        return X2
def find_Xpath(Address):
    print('add')
    xpathes = [
        ["google.com","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["facebook.com","/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]"],
        ["youtube.com","/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/div/span"],
        ["amazonaws.com","/html/body/div[1]/div/div[1]/div/div/div/div/button[2]"],
        ["microsoft.com","/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[2]/button[1]"],
        ["twitter.com","/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/span/span"],
        ["cloudflare.com","/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["netflix.com","/html/body/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div[1]/button"],
        ["linkedin.com","/html/body/div[1]/div/section/div/div[2]/button[1]"],
        ["yahoo.com","/html/body/div/div/div/div/form/div[2]/div[2]/button[1]"],
        ["azure.com","/html/body/div[3]/div/div[1]/div[1]/div/div[2]/button[1]"],
        ["googlevideo.com","/html/body/div/div[1]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["bing.com","/html/body/div[2]/div[1]/div/div[2]/div[2]/button[1]/a"],
        ["office.com","/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div[2]/button[1]"],
        ["reddit.com","/html/body/div[1]/div/div[2]/div[3]/div/section/div/section[2]/section[1]/form/button"],
        ["youtu.be","/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/div/span"],
        ["doubleclick.net","/html/body/div[1]/div/span[2]/a[2]"],
        ["mail.ru","/html/body/div[1]/div[1]/div[2]/span[2]/a/span"],
        ["zoom.us","/html/body/div[2]/div[3]/div/div/div[2]/div/div/button[2]"],
        ["fastly.net","/html/body/div[5]/div[3]/div/div/div[2]/div[2]/div/div[1]/button"],
        ["adobe.com","/html/body/div[6]/div[2]/div[1]/div[1]/div/div[2]/div/button[3]"],
        ["vimeo.com","/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/button[3]"],
        ["wordpress.com","/html/body/form/div[1]/div/a[2]"],
        ["goo.gl","/html/body/div[4]/div/span[2]/a[2]"],
        ["sharepoint.com","/html/body/div[1]/div/div/div/div/div/div/div[2]/button[1]"],
        ["bit.ly","/html/body/div[2]/div/div[2]/span"],
        ["tiktok.com","/html/body/tiktok-cookie-banner//div/div[2]/button[2]"],
        ["windows.net","/html/body/div[3]/div[2]/div/div/div/div/div/div/div/div[2]/button[1]"],
        ["office365.com","/html/body/div[3]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/button[1]"],
        ["google-analytics.com","/html/body/div[1]/div/span[2]/a[2]"],
        ["paypal.com","/html/body/div[1]/div/div[3]/div/div[2]/button[1]"],
        ["tumblr.com","/html/body/div/div/div[3]/div/button[2]"],
        ["canva.com","/html/body/div[1]/div/div/div/div/div[2]/button[1]/span"],
        ["comcast.net","/html/body/div[2]/div[2]/a[1]"],
        ["skype.com","/html/body/div[2]/div[1]/div/div/div/div/div/div/div[2]/button[1]"],
        ["yandex.net","/html/body/div[5]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/button"],
        ["europa.eu","/html/body/div[1]/div/div/div/div[2]/a[1]"],
        ["google.com.hk","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["fandom.com","/html/body/div[7]/div/div/div[2]/div[2]"],
        ["nytimes.com","/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div[2]/button[1]"],
        ["ebay.com","/html/body/div[5]/div[1]/div[2]/div[2]/div[2]/button[2]"],
        ["dropbox.com","/html/body/div[1]/div/div/button[2]"],
        ["flickr.com","/html/body/div[8]/div[1]/div/div[6]/a[3]"],
        ["opera.com","/html/body/div[2]/div[1]/div/div/span[1]"],
        ["ibm.com","/html/body/div[3]/div[2]/div/div[2]/div[1]/div[2]/button[1]"],
        ["gravatar.com","/html/body/form/div[1]/a[2]"],
        ["aliexpress.com","/html/body/div[7]/div/div[2]/button[2]"],
        ["salesforce.com","/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["speechmatics.com","/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]"],
        ["att.net","/html/body/div/div/div/div/form/div[2]/div[2]/button[1]"],
        ["soundcloud.com","/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/button[1]"],
        ["xhamster.com","/html/body/div[4]/div[2]/div/button[2]/span"],
        ["force.com","/html/body/div[10]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["webex.com","/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["digicert.com","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button"],
        ["cnn.com","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[1]"],
        ["forbes.com","/html/body/div[1]/div/div/div/div[2]/button[2]/span"],
        ["stackoverflow.com","/html/body/div[5]/div[1]/button[1]"],
        ["zemanta.com","/html/body/div[4]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["dnsmadeeasy.com","/html/body/div[1]/div/a"],
        ["theguardian.com","/html/body/div/div[2]/div[3]/div/div/button[1]"],
        ["cisco.com","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["bbc.com","/html/body/div[2]/div/div/div/div[3]/div[2]/button"],
        ["aliyun.com","/html/body/div[5]/div/div/div[2]/button[2]"],
        ["roblox.com","/html/body/div[4]/div/div[1]/div[2]/div/div/button[2]"],
        ["etsy.com","/html/body/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/button"],
        ["amazon.co.uk","/html/body/div[1]/span/form/div[3]/span[1]/span/input"],
        ["twitch.tv","/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[3]/button/div/div/div"],
        ["booking.com","/html/body/div[16]/div[2]/div/div[1]/div/div[2]/div/button[2]"],
        ["shopify.com","/html/body/div[3]/section/div/div/button[2]"],
        ["bbc.co.uk","/html/body/div[2]/div/div/div/div[3]/div[2]/button"],
        ["meraki.com","/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["sourceforge.net","/html/body/div[2]/div/div[2]/span[2]/a/span"],
        ["zendesk.com","/html/body/div[4]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["researchgate.net","/html/body/div[1]/div/div/div/div[2]/div/button[3]"],
        ["oracle.com","/html/body/div[8]/div[1]/div/div[3]/a[1]"],
        ["comcast.com","/html/body/div[2]/div[2]/a[1]"],
        ["slack.com","/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["freepik.com","/html/body/div[8]/div[3]/div/div[1]/div/div[2]/div/button[1]"],
        ["epicgames.com","/html/body/div[4]/div[3]/div/div/div[2]/div/button[3]"],
        ["issuu.com","/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]"],
        ["dell.com","/html/body/div[2]/div[2]/a[1]"],
        ["deepl.com","/html/body/div[7]/div/div/div[3]/button[2]"],
        ["tencent.com","/html/body/div/div[4]/div[3]/div[4]/div[1]"],
        ["google.co.in","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["weebly.com","/html/body/div[4]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["linktr.ee","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["hp.com","/html/body/div[3]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["googlesyndication.com","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["klarna.com","/html/body/div[3]/div[3]/div/div/div[2]/div/div/button[2]"],
        ["alibaba.com","/html/body/div[9]/div[2]/div/div[2]/div[1]"],
        ["opendns.com","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["washingtonpost.com","/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button[1]"],
        ["feishu.cn","/html/body/div[1]/div[2]/button[2]"],
        ["google.de","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["dailymail.co.uk","/html/body/div[4]/div/div/div/div[3]/div/button[2]"],
        ["reuters.com","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[1]"],
        ["samsung.com","/html/body/div[2]/div/div/div[2]/button[2]"],
        ["databricks.com","/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["atlassian.net","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[2]"],
        ["behance.net","/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/button[3]"],
        ["instructure.com","/html/body/div[4]/div[2]/div/div/div[2]/div/div/button"],
        ["wix.com","/html/body/div[3]/div/ul/li[1]/button"],
        ["msn.cn","/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[1]"],
        ["tinyurl.com","/html/body/div[1]/div/div/div/div[2]/div/button[2]"],
        ["bloomberg.com","/html/body/div/div[2]/div[5]/button[1]"],
        ["wsj.com","/html/body/div/div[2]/div[4]/div/div/button[2]"],
        ["huawei.com","/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["okta.com","/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["google.co.uk","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["godaddy.com","/html/body/div[2]//div/div/div[3]/div/div/button[3]"],
        ["amazonvideo.com","/html/body/div[1]/div[1]/div[2]/div/section/div/div/div[2]/span/form/button"],
        ["salesforceliveagent.com","/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["springer.com","/html/body/section/div/div[2]/button[1]/span"],
        ["ilovepdf.com","/html/body/div[5]/div/div[2]/a[2]"],
        ["stripe.com","/html/body/div[2]/div[2]/div/div/div/div/div[2]/a[1]"],
        ["criteo.com","/html/body/div[9]/div[3]/div/div/div[2]/div/button[3]"],
        ["www.gov.uk","/html/body/div[1]/div/div[2]/button[1]"],
        ["rackspace.com","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[1]"],
        ["nnip.com","/html/body/div/section/div/div/div/div[2]/button[1]"],
        ["nature.com","/html/body/section/div/div[2]/button[1]"],
        ["ig.com","/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button"],
        ["businessinsider.com","/html/body/div[2]/div[1]/div[2]/span[2]/a/span"],
        ["hubspot.com","/html/body/div[2]/div/div/div[2]/button[1]"],
        ["ring.com","/html/body/div[5]/div/button[2]"],
        ["ok.ru","/html/body/div[1]/div[1]/div[2]/span[1]/a/span"],
        ["elasticbeanstalk.com","/html/body/div[1]/div/div[1]/div/div/div/div/button[2]"],
        ["digitalocean.com","/html/body/div[8]/div[1]/div/div/div[2]/div/div/div[3]/div/button[3]"],
        ["cnbc.com","/html/body/div[5]/div[3]/div/div[1]/div/div[2]/div/button[1]"],
        ["wp.com","/html/body/form/div[1]/div/a[2]"],
        ["slideshare.net","/html/body/div[1]/div[2]/div[2]/button[2]"],
        ["unity3d.com","/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["weather.com","/html/body/div[3]/div/div/div/div/div/div[3]/button[1]"],
        ["trello.com","/html/body/div[2]/div/div[1]/div/button"],
        ["pki.goog","/html/body/div[1]/div/span[2]/a[2]"],
        ["kaspersky.com","/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]"],
        ["espn.com","/html/body/div[9]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["onlyfans.com","/html/body/div/div[1]/div/div/div[2]/button[2]"],
        ["windows.com","/html/body/div[1]/div/div[2]/button[1]"],
        ["figma.com","/html/body/div/div[1]/div[2]/div[2]/button[1]"],
        ["zoom.com","/html/body/div[2]/div[3]/div/div/div[2]/div/div/button[2]"],
        ["dailymotion.com","/html/body/div[2]/div/div/div[2]/div/div[4]/button[2]/span/span"],
        ["grammarly.com","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["fiverr.com","/html/body/div[17]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["trustpilot.com","/html/body/div[2]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["fc2.com","/html/body/div[1]/div/div/div[2]/button"],
        ["w3schools.com","/html/body/div[6]/div/div/div/div[3]/div[1]/div[1]"],
        ["eventbrite.com","/html/body/div[3]/button[2]"],
        ["swisscom.ch","/html/body/div[8]/div[1]/div/div/div[2]/div[2]/button[1]"],
        ["ampproject.org","/html/body/amp-consent/div/button[2]"],
        ["google.co.jp","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["usatoday.com","/html/body/div[2]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["xiaomi.com","/html/body/div[2]/div/div[2]/div/div[2]/button[2]"],
        ["typeform.com","/html/body/div[1]/div[1]/div/div[1]/div[2]/button[1]"],
        ["aol.com","/html/body/div/div/div/div/form/div[2]/div[2]/button[1]"],
        ["npr.org","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[1]"],
        ["cnet.com","/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["pixabay.com","/html/body/div[7]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["cpanel.net","/html/body/div[3]/div[1]/div[5]/div[2]/a[3]"],
        ["ft.com","/html/body/div/div[1]/div/div[4]/div/div/div/div/div[2]/div[1]/a"],
        ["time.com","/html/body/div[4]/div[2]/div/div/div[2]/div/div/button[1]"],
        ["surveymonkey.com","/html/body/div[2]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["udemy.com","/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["notion.so","/html/body/div/div/div/section/div/section/nav/div[2]/button"],
        ["name.com","/html/body/div[7]/div[2]/div/div[1]/div/div[2]/div/button[2]"],
        ["telegraph.co.uk","/html/body/div/div[2]/div[3]/div/div[2]/div[2]/button[1]"],
        ["scribd.com","/html/body/div[1]/div[2]/div[2]/button[2]"],
        ["hostgator.com","/html/body/div[9]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["yelp.com","/html/body/div/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["statista.com","/html/body/div[17]/div[3]/div/div/div[2]/div/div/button[2]"],
        ["webmd.com","/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[1]"],
        ["ted.com","/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]"],
        ["g.page","/html/body/section/div/div/span[2]/a[2]"],
        ["swisscom.com","/html/body/div[8]/div[1]/div/div/div[2]/div[2]/button[1]"],
        ["themeforest.net","/html/body/div[1]/div[1]/div[4]/a[2]"],
        ["adobe.io","/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/button[3]"],
        ["mi.com","/html/body/div[2]/div/div[2]/div/div[2]/button[2]"],
        ["binance.com","/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["eslgaming.com","/html/body/div[3]//div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/button[2]"],
        ["amazon.de","/html/body/div[1]/span/form/div[3]/span[1]/span/input"],
        ["wired.com","/html/body/div[4]/div[2]/div/div/div[2]/div/div/button"],
        ["casalemedia.com","/html/body/div[2]/div[2]/div/button[1]"],
        ["shutterstock.com","/html/body/div[2]/div[2]/div/div/div[2]/div/div/button[1]"],
        ["sentry.io","/html/body/div[2]/div/button[1]"],
        ["speedtest.net","/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["mailchimp.com","/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["steampowered.com","/html/body/div[3]/div/div[2]/div[1]/span"],
        ["tripadvisor.com","/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button"],
        ["pexels.com","/html/body/div[21]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["mysql.com","/html/body/div[8]/div[1]/div/div[3]/a[1]"],
        ["cloudns.net","/html/body/div[10]/button"],
        ["nvidia.com","/html/body/div[2]/div[3]/div/div/div[2]/div/div/button[2]"],
        ["bluehost.com","/html/body/div[7]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["healthline.com","/html/body/div[2]/div/div/div/div/div/div/div[2]/button/span/span"],
        ["amazon.it","/html/body/div[1]/span/form/div[3]/span[1]/span/input"],
        ["wetransfer.com","/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[1]"],
        ["squarespace.com","/html/body/div[2]/div/div/div[2]/button[1]"],
        ["roku.com","/html/body/div[2]/div/div/button[2]"],
        ["cambridge.org","/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]"],
        ["dscreens.ru","/html/body/div[1]/div/div[2]/div/div/button"],
        ["intel.com","/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["quizlet.com","/html/body/div[7]/div[2]/div/div[1]/div/div[2]/div/button[1]"],
        ["marriott.com","/html/body/div[6]/div[3]/div/div/div[2]/div[1]/div/button[2]"],
        ["independent.co.uk","/html/body/div/div[2]/div[2]/div[2]/div[5]/button[2]"],
        ["ea.com","/html/body/div[1]/div/div/div[2]/button[1]"],
        ["upwork.com","/html/body/div[7]/div[2]/div/div/div[2]/div/div/button"],
        ["vmware.com","/html/body/div[7]/div[2]/div/div[1]/div/div[2]/div/button[2]"],
        ["appsflyer.com","/html/body/div/div[2]/div/div/div[2]/div/div/button[2]"],
        ["techcrunch.com","/html/body/div/div/div/div/form/div[2]/div[2]/button[1]"],
        ["warnerbros.com","/html/body/div[3]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["zoho.com","/html/body/div[4]/div/div[1]/div/div[2]/div[2]/span"],
        ["amazon.fr","/html/body/div[1]/span/form/div[3]/span[1]/span/input"],
        ["britannica.com","/html/body/app-root/app-theme/div/div/app-notice/app-theme/div/div/app-home/div/div[2]/app-footer/div/div[2]/app-action-buttons/div/button[3]/span[1]/div/span"],
        ["playstation.com","/html/body/div[6]/button[2]"],
        ["tandfonline.com","/html/body/div[1]/div/div[3]/div/div/footer/div/div[4]/div/div/div/button"],
        ["investopedia.com","/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/button[3]"],
        ["cbsnews.com","/html/body/div[9]/div[3]/div/div/div[2]/div/div/button[1]"],
        ["yandex.com","/html/body/div[3]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/button"],
        ["avast.com","/html/body/div[1]/div[2]/div/div/div[2]/div/div/button[2]"],
        ["google.ru","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["bitly.com","/html/body/div[2]/div/div[2]/span"],
        ["uol.com.br","/html/body/div[3]/div/div[2]/button"],
        ["google.ca","/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"],
        ["huffingtonpost.com","/html/body/div[1]/div/div/div/div[2]/div/button[3]/span"],
        ["mongodb.com","/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/button[2]"],
        ["theverge.com","/html/body/div/div[2]/div/div[2]/button[1]"],
        ["wikihow.com","/html/body/div[4]/div[2]/div[1]/div[2]/div"],

        ['free.fr','/html/body/div[1]/div/div/div/div/div/div[3]/button[3]/span']

        ]


    for i in xpathes:
        if i[0]== Address:
            return i[1]
    
    return 'nothing'


def take_scrren_after(driver,site_url):
    driver.get_screenshot_as_file('C:/Users/jaber/Desktop/photoes/' + site_url +'_accept_post_consent.png')

def take_scrren_before(driver,site_url):
    driver.get_screenshot_as_file('C:/Users/jaber/Desktop/photoes/' + site_url +'_accept_pre_consent.png')

def noop_take_scrren_before(driver,site_url):
    driver.get_screenshot_as_file('C:/Users/jaber/Desktop/photoes/' + site_url +'_noop.png')
def accept2(driver,option,Address):
    JS = ""
    if option == '-u':
        xpath =  find_Xpath(Address)         
        if xpath != 'nothing':
            print(Address,xpath)
            
            
            s1= datetime.now()
            driver.get( 'https://'+Address)            
            s2=datetime.now()
            response_time = (s2-s1).total_seconds()
            take_scrren_after(driver,Address)
            #time.sleep(5)
            dictionary = '[   ]'
            person_dict = json.loads(dictionary)            
            #time.sleep(5)
            #python_button = driver.find_element('xpath',xpath)
            if (len(driver.get_cookies()) ==0):
                        if response_time<4 :
                            
                            log('load_Error',Address ,'domain does not exist')
                        else :
                            log('load_Error',Address ,'timout error')
            
            for request in driver.requests:  
                if request.response:
                    X=str(request.response.headers)
                    X=ss(X)
                    #print(  
                    #    request.url,  
                     #   request.response.status_code,  
                    #    request.response.headers['Content-Type'])                            
                                   
                    new_data ={"Address": Address,"response_time": response_time, "request_url": request.url ,"UNIX_TIME" : time.mktime(s1.timetuple()) , "headers": X}              
                    person_dict.append(new_data)

            #JS= json.dumps(person_dict)
            #print(JS)
            
            
        else :
            print('Your address not found in our database')
    return person_dict





def log(type_ , Address, message,Type):
    f = open("demofile2.txt", "a")
    f.write( '\n')
    f.write(type_)
    f.write( '\n')
    f.write(Address)
    f.write( '\n')
    f.write(message)
    f.write( '\n')
    f.write(Type)
    f.write( '\n')
    f.write( '\n')
    f.write( '\n')
    f.close()


def accept(driver,option,Address):
    
    dictionary = '[   ]'
    person_dict = json.loads(dictionary)
    person_dict2 = json.loads(dictionary)
    if option == '-u':
        xpath =  find_Xpath(Address)         
        if xpath != 'nothing':
            print(Address,xpath)
          
            s1= datetime.now()
            driver.get( 'https://'+ Address)            
            s2=datetime.now()
            response_time = (s2-s1).total_seconds()
            take_scrren_before(driver,Address)
            time.sleep(10)

            if (len(driver.get_cookies()) ==0):
                        if response_time<2 :
                            
                            log('load_Error',Address ,'domain does not exist','accept')
                        else :
                            log('load_Error',Address ,'timout error','accept')
            else:

                try:
                        print('click try')
                        python_button = driver.find_element('xpath',xpath).click()
                        log('processed',Address ,'click ','accept')
                        time.sleep(10)
                                    

                except:
                        log('load_Error',Address ,'click error','accept')
                take_scrren_after(driver,Address)
                for request in driver.requests:  
                    if request.response:
                        X=str(request.response.headers)
                        X=ss(X)
                                                             
                        new_data ={"Address": Address, "request_url": request.url ,"UNIX_TIME" : time.mktime(s1.timetuple()) , "headers": X}              
                        person_dict.append(new_data)
                        json_object = json.dumps(person_dict, indent=4)
                        with open("C:/Users/jaber/Desktop/photoes/"+Address+"_accept_headers.json", "w") as outfile:
                                outfile.write(json_object)
                Requ=[]
                Header=[]
                for request in driver.requests:  
                    if request.response:
                        
                        Requ.append((request.url,request.response.status_code))

                cockie=[]
                for cocke in driver.get_cookies():  
                       cockie.append(cocke)
              
                new_data ={"website_domain": Address,"number_of_cockie":len(driver.get_cookies()),"type":'accept',"response_time": str(response_time), "post_pageload_url":driver.current_url ,"pageload_start_ts" :str(time.mktime(s1.timetuple())) ,"pageload_end_ts" :str(time.mktime(s1.timetuple())),"requests": Requ  ,"cockie" : cockie }              
                person_dict2.append(new_data)
                json_object = json.dumps(person_dict2, indent=4)
                with open("C:/Users/jaber/Desktop/photoes/"+Address+"_accept.json", "w") as outfile:
                        outfile.write(json_object)
                return(person_dict2,person_dict)
           
        else :
          
            s1= datetime.now()
            driver.get( 'https://'+ Address)            
            s2=datetime.now()
            response_time = (s2-s1).total_seconds()
            take_scrren_after(driver,Address)
            time.sleep(10)
            if (len(driver.get_cookies()) ==0):
                        if response_time<2 :
                            
                            log('load_Error',Address ,'domain does not exist','accept')
                        else :
                            log('load_Error',Address ,'timout error','accept')
            else:
                for request in driver.requests:  
                    if request.response:
                        X=str(request.response.headers)
                        X=ss(X)
                        new_data ={"Address": Address, "request_url": request.url ,"UNIX_TIME" : time.mktime(s1.timetuple()) , "headers": X}              
                        person_dict.append(new_data)
                        json_object = json.dumps(person_dict, indent=4)
                        with open("C:/Users/jaber/Desktop/photoes/"+Address+"_accept_headers.json", "w") as outfile:
                                outfile.write(json_object)
                Requ=[]
                for request in driver.requests:  
                    if request.response:                         
                        Requ.append((request.url,request.response.status_code))
                cockie=[]
                for cocke in driver.get_cookies():  
                       cockie.append(cocke)
                new_data ={"website_domain": Address,"number_of_cockie":len(driver.get_cookies()),"type":'accept',"response_time": str(response_time), "post_pageload_url":driver.current_url ,"pageload_start_ts" :str(time.mktime(s1.timetuple())) ,"pageload_end_ts" :str(time.mktime(s1.timetuple())),"requests": Requ ,"cocke": cockie }              
                person_dict2.append(new_data)
                json_object = json.dumps(person_dict2, indent=4)
                with open("C:/Users/jaber/Desktop/photoes/"+Address+"_accept.json", "w") as outfile:
                        outfile.write(json_object)
            return(person_dict2,person_dict)
            
    return(person_dict2,person_dict)



def noop(driver,option,Address):   
    dictionary = '[   ]'
    person_dict = json.loads(dictionary)
    person_dict2 = json.loads(dictionary)
    if option == '-u':

            
          
            s1= datetime.now()
            driver.get( 'https://'+ Address)            
            s2=datetime.now()
            response_time = (s2-s1).total_seconds()
            noop_take_scrren_before(driver,Address)
            time.sleep(10)

            if (len(driver.get_cookies()) ==0):
                        if response_time<2 :
                            
                            log('load_Error',Address ,'domain does not exist','noop')
                        else :
                            log('load_Error',Address ,'timout error','noop')
            


            else:
                for request in driver.requests:  
                    if request.response:
                        X=str(request.response.headers)
                        X=ss(X)
                                                             
                        new_data ={"Address": Address, "request_url": request.url ,"UNIX_TIME" : time.mktime(s1.timetuple()) , "headers": X}              
                        person_dict.append(new_data)
                        json_object = json.dumps(person_dict, indent=4)
                        with open("C:/Users/jaber/Desktop/photoes/"+Address+"_noop_headers.json", "w") as outfile:
                                outfile.write(json_object)

                Requ=[]
                Header=[]
                for request in driver.requests:  
                    if request.response:
                        
                        Requ.append((request.url,request.response.status_code))

                cockie=[]
                for cocke in driver.get_cookies():  
                       cockie.append(cocke)
              
                new_data ={"website_domain": Address,"number_of_cockie":len(driver.get_cookies()),"type":'noop',"response_time": str(response_time), "post_pageload_url":driver.current_url ,"pageload_start_ts" :str(time.mktime(s1.timetuple())) ,"pageload_end_ts" :str(time.mktime(s1.timetuple())),"requests": Requ  ,"cockie" : cockie }              
                person_dict2.append(new_data)
                json_object = json.dumps(person_dict2, indent=4)
                with open("C:/Users/jaber/Desktop/photoes/"+Address+"_noop.json", "w") as outfile:
                        outfile.write(json_object)
                print(len(Requ))

                return(person_dict2,person_dict)

            
    return(person_dict2,person_dict)


def accept_csv(option,file):

    driver = webdriver.Firefox()
    df = pd.read_csv(file,names=[0,1], header=None)
    JS=[]
    JS_S=[]
    print(df[0][1])
    for i in range (99):
        driver = webdriver.Firefox()
        print('x',df[1][i])
        try:
            person_dict=accept(driver,'-u',df[1][i])
            if(len(person_dict)>0):
             JS.append(person_dict[0])
             JS_S.append(person_dict[1])
        except:
            log('site_error',df[1][i] ,'timout error','accept')
        driver.close()
        
        
    save_file = open("savedata2.json", "a")  
    json.dump(JS, save_file, indent = 6)  
    save_file.close()  
    save_file = open("savedata.json", "a")  
    json.dump(JS_S, save_file, indent = 6)  
    save_file.close() 

def noop_csv(option,file):

    df = pd.read_csv(file,names=[0,1], header=None)
    JS=[]
    JS_S=[]
    print(df[0][1])
    for i in range (99):
        driver = webdriver.Firefox()
        print('x',df[1][i])
        try:
            person_dict=noop(driver,'-u',df[1][i])
            if(len(person_dict)>0):
             JS.append(person_dict[0])
             JS_S.append(person_dict[1])
        except:
            log('site_error',df[1][i] ,'timout error','noop')
        driver.close()        
        
    save_file = open("savedata2.json", "a")  
    json.dump(JS, save_file, indent = 6)  
    save_file.close()  
    save_file = open("savedata.json", "a")  
    json.dump(JS_S, save_file, indent = 6)  
    save_file.close() 

if sys.argv[1] == '-u':
    if sys.argv[3] == '--accept' :
        
       accept(sys.argv[1],sys.argv[2])
    
    if sys.argv[3] == '--noop' :
        
       noop(sys.argv[1],sys.argv[2])    


if sys.argv[1] == '-i':
    if sys.argv[3] == '--accept' :
        
 
           accept_csv(sys.argv[1],sys.argv[2])
        
    
    if sys.argv[3] == '--noop' :
        
       noop_csv(sys.argv[1],sys.argv[2])  


print(x)

