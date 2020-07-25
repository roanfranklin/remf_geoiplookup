#!/usr/bin/python3
# pip3 install xmltodict
# pip3 install pyfiglet
# pip3 install colorama

import os, sys, xmltodict, requests, json
import pyfiglet
import colorama
from colorama import Fore, Style

def logo():
    os.system("clear")

    ascii_banner = pyfiglet.figlet_format("REMF - GeoIP")
    print(Style.BRIGHT+Fore.BLUE+ascii_banner)
    print(Fore.YELLOW+' [ '+Fore.WHITE+'REMF.COM.BR'+Fore.YELLOW+' - '+Fore.WHITE+'Geolocalização IP'+Fore.YELLOW+' ]'+Style.RESET_ALL)

def ajuda():
    print(' '+Fore.CYAN)
    print(' Use:', sys.argv[0], '[ IP_VALIDO ]')
    print(Style.RESET_ALL+' ')

def gIP(IP):    
    URL = "http://api.geoiplookup.net/?query=" + IP

    xdata = requests.get(URL)
    xpars = xmltodict.parse(xdata.text)
    xjson = json.dumps(xpars)
    data = json.loads(xjson)
    type(data)

    print(' ')
    print(Style.BRIGHT+Fore.BLUE+'        IP:'+Fore.WHITE+' {}' . format(data['ip']['results']['result']['ip']))
    print(Style.BRIGHT+Fore.BLUE+'      Host:'+Fore.WHITE+' {}' . format(data['ip']['results']['result']['host']))
    print(Style.BRIGHT+Fore.BLUE+'       ISP:'+Fore.WHITE+' {}' . format(data['ip']['results']['result']['isp']))
    print(Style.BRIGHT+Fore.BLUE+'    Cidade:'+Fore.WHITE+' {}' . format(data['ip']['results']['result']['city']))
    print(Style.BRIGHT+Fore.BLUE+' País(Cod):'+Fore.WHITE+' {}' . format(data['ip']['results']['result']['countrycode']))
    print(Style.BRIGHT+Fore.BLUE+'      País:'+Fore.WHITE+' {}' . format(data['ip']['results']['result']['countryname']))
    print(Style.BRIGHT+Fore.BLUE+'  Latitude:'+Fore.WHITE+' {}' . format(data['ip']['results']['result']['latitude']))
    print(Style.BRIGHT+Fore.BLUE+' Longitude:'+Fore.WHITE+' {}' . format(data['ip']['results']['result']['longitude']))
    print(' '+Style.RESET_ALL)

def main():
    logo()
    if len(sys.argv) > 1:
        gIP(sys.argv[1])
    else:
        ajuda()

if __name__ == "__main__":
    main()
