import requests
import hashlib
import urllib
import sys

class k:
    gaode_key = ""
    tx_key = ""
    tx_sk = ""
    baidu_ak = ""

def url_sort(url):
    a = urllib.parse.parse_qs(url)
    r_url = ""
    for i in sorted (a) : 
        r_url = r_url + "&" +  i + "=" + a[i][0]
    return("?" + r_url[1:])

def tx_sig(url:str):
    u = url.split("https://apis.map.qq.com")[1]
    sr = u.split("?")
    url_sorted = url_sort(sr[1])

    url = sr[0] + url_sorted + k.tx_sk
    url = url.replace("markers2qwq","markers")
    url_sorted = url_sorted.replace("markers2qwq","markers")

    #print("怪耶",url)

    ret = hashlib.md5(url.encode('utf-8')).hexdigest()
    returl = "https://apis.map.qq.com" + sr[0] + url_sorted
    return(ret,returl)

def search_locate(lname,lcity):
    
    url = "https://restapi.amap.com/v5/place/text?key=" + k.gaode_key + "&keywords="+ lname +"&output=json&region=" + lcity

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.text)


def route_planning(ori,dest,plan='driving'):  #高德路径规划
    url = "https://restapi.amap.com/v5/direction/" + plan + "?key=" + k.gaode_key + "&origin=" + ori +"&destination=" + dest +"&AlternativeRoute=0&output=json&show_fields=polyline"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.text)

def generate_img_tx(ori,dest,path): #废案

    #url = "https://apis.map.qq.com/ws/staticmap/v2?size=300*300&zoom=12&scale=2&maptype=roadmap&key=" + k.tx_key + "&path=" + path + "&markers=size:mid|color:blue|label:A|" + ori + "&markers2qwq=size:mid|color:red|label:B|" + dest
    url = "https://apis.map.qq.com/ws/staticmap/v2?size=300*300&zoom=12&scale=2&maptype=roadmap&key=" + k.tx_key + "&path=" + path 

    tmp = tx_sig(url)

    sig = tmp[0]
    url = tmp[1]
    url = url + "&sig=" + sig
    #url = url.replace("markers2qwq","markers")
    #print(url)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    #print(response.text)
    with open ('nb', 'wb') as f:
        f.write(response.content)

def generate_img(ori,dest,path):  #高德,路径规划,图片生成

    url = "https://restapi.amap.com/v3/staticmap?size=1024*1024&paths=4,0x0000FF,1,,:" + path + "&key=" + k.gaode_key + "&traffic=1&scale=2&markers=large,0xFF0000,起:" + ori +"|large,0xFF0000,终:" + dest

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if(response.status_code != 200):
        return(response.text)

    with open ('.\\temp\\nb.png', 'wb') as f:
        f.write(response.content)
    return(sys.path[0] + '\\temp\\nb.png')

def where_on_bus(lola):

    url = "http://api.map.baidu.com/parking/search?location=" + lola + "&coordtype=wgs84ll&ak=" + k.baidu_ak
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.text)

def where_on_bus_generate(markers,labels):

    url = "https://restapi.amap.com/v3/staticmap?size=512*512&key=" + k.gaode_key + "&traffic=0&scale=2&markers=" + markers + "&labels=" + labels

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if(response.status_code != 200):
        return(response.text)

    with open ('.\\temp\\bus.png', 'wb') as f:
        f.write(response.content)
    return(sys.path[0] + "\\temp\\bus.png")


def city_code(address): #地理编码

    url = "https://restapi.amap.com/v3/geocode/geo?key=" + k.gaode_key + "&address=" + address

    payload={}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    return(response.text)

