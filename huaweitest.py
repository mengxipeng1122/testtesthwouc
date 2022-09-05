#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import requests
import xml.etree.ElementTree as ET

headers = {
    'content-type' : 'application/json; charset=UTF-8',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
    'Accept-Encoding': 'identity',
}

def getRequest(URL, PARAMS={}):
    r = requests.get(url = URL, params = PARAMS)
    data = r.text
    print(data)

def postRequest(URL, data={}, PARAMS={}):
    r = requests.post(url = URL, data=data, headers=headers)
    data = r.text
    print(data)

def getRequestConfig():
    URL='https://configserver.hicloud.com/servicesupport/updateserver/getConfig'
    data = {
        "configureID":"RomUpdate",
        "isStrictMatch":False,
        "condParaList":[
            {"key":"DeviceName","value":"KNT-UL10"},
            {"key":"FirmWare","value":"KNT-UL10 8.0.0.535(C00)"},
            {"key":"IMEI","value":"862989032015118"},
            {"key":"Language","value":"zh-cn"},
            {"key":"PackageType","value": "increment",},
            {"key":"OS","value": "Android 8.0.0",},
        ] }
    postRequest(URL,data=json.dumps(data))


def main():
    getRequestConfig();

if __name__ == '__main__':
    main()

