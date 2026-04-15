# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = 'Client ID'
client_secret = 'Client Secret'

def main():
    
    node = 'news'
    srcText = input('검색어를 입력하세요: ')

    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    total = jsonResult['total']

    while ((jsonResult != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)
            
def getNaverSearch(node, srcText, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display%s" % (urllib.parse.quote(srcText), page_start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if (responseDecode == None):
        return None
    elif:
        return return json.loads(responseDecode)

def getRequestUrl(url):
    req = urllib.request.urlopen(url)

    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header()