#!/usr/bin/python3
# pip3 install xmltodict
# pip3 install pyfiglet

import os, sys, xmltodict, requests, json
import pyfiglet

def logo():
    os.system("clear")

    ascii_banner = pyfiglet.figlet_format("REMF - GeoIP")
    print(ascii_banner)

def ajuda():
    print('\n Usar: ', sys.argv[0], ' IP_VÁLIDO\n')

def gIP(IP):    
    URL = "http://api.geoiplookup.net/?query=" + IP

    xdata = requests.get(URL)
    xpars = xmltodict.parse(xdata.text)
    xjson = json.dumps(xpars)
    data = json.loads(xjson)
    type(data)

    print(' ')
    print('        IP: {}' . format(data['ip']['results']['result']['ip']))
    print('      Host: {}' . format(data['ip']['results']['result']['host']))
    print('       ISP: {}' . format(data['ip']['results']['result']['isp']))
    print('    Cidade: {}' . format(data['ip']['results']['result']['city']))
    print(' País(Cod): {}' . format(data['ip']['results']['result']['countrycode']))
    print('      País: {}' . format(data['ip']['results']['result']['countryname']))
    print('  Latitude: {}' . format(data['ip']['results']['result']['latitude']))
    print(' Longitude: {}' . format(data['ip']['results']['result']['longitude']))
    print(' ')

def main():
    logo()
    if len(sys.argv) > 1:
        gIP(sys.argv[1])
    else:
        ajuda()

if __name__ == "__main__":
    main()
