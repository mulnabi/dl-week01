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

    jsonResult = getNaverSearch(node, srcText, 1, 100)
    total = jsonResult['total']

    while ((jsonResult != None) and (jsonResp))