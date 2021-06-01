import json
import info_Request as Req
import sys

def get_lonlat_pt(lname,lcity):  #获取经纬度，带交互
    jsondata = Req.search_locate(lname,lcity)
    j = json.loads(jsondata)
    poi = j['pois']
    num = 0
    l_lola = {}
    for p in poi:
        print(str(num) + '.' + p['pname'] + ' ' + p['cityname'] + ' ' + p['adname'] + ' ' + p['address'] + p['name'])
        l_lola[str(num)] = p['location']
        num = num +1

    print("输入目标序号:")
    num = sys.stdin.readline()[:-1]

    return(l_lola[str(num)])

def get_lonlat(lname,lcity):  #获取经纬度，无交互，默认第一个
    jsondata = Req.search_locate(lname,lcity)
    j = json.loads(jsondata)
    poi = j['pois']
    num = 0
    l_lola = {}
    for p in poi:
        #print(str(num) + '.' + p['pname'] + ' ' + p['cityname'] + ' ' + p['adname'] + ' ' + p['address'] + p['name'])
        l_lola[str(num)] = p['location']
        num = num +1
    #print(l_lola['0'])
    return(l_lola['0'])



def get_route(ori,dest,is_list:bool = False,plan='driving'):  #True直接返回python列表，False返回高德静态图path
    getjson = Req.route_planning(ori,dest,plan=plan)
    get_obj = json.loads(getjson)
    steps = get_obj['route']['paths'][0]['steps']

    lolas = []
    gnum = 0
    for step in steps:
        polyline = step['polyline']
        tmp = polyline.split(';')
        lolas.append(tmp)
        gnum = gnum + len(tmp)

    while(gnum > 1536):
            n = 0
            m = 0
            for tmp in lolas:
                if(len(tmp) > 2):
                    lolas[n].pop(int(len(tmp)/2))
                    m = m + 1
                n = n + 1
            gnum = gnum - m
    ret = []
    for ret_tmp in lolas:
        ret = ret + ret_tmp

    if(is_list == True):
        return(ret)  #直接返回列表
    else:
        rettext = ''
        for r in ret:
            rettext = rettext + ";" + r
        #print(rettext[1:])
        return(rettext[1:])

def where_on_bus(lola):
    markers = ''
    labels = ''
    jsondata = Req.where_on_bus(lola)
    j = json.loads(jsondata)

    for l_list in j['recommendStops']:
        l_name = l_list['name']
        l_locate = str(l_list['gcj02ll_x']) + ',' + str(l_list['gcj02ll_y'])

        l_name = l_name.replace('·','•')[0:15]

        markers = markers + ';' + l_locate
        labels = labels + "|" + l_name + ",,,13,,:" + l_locate

    markers = "large,0x00CC00,起:" + lola + "|mid,0xFF0000,:" + markers[1:]
    labels = labels[1:]

    stat = Req.where_on_bus_generate(markers,labels)
    return(stat)

def get_citycode(address):
    jsondata = Req.get_citycode(address)
    j = json.loads(jsondata)

    citycode = j['geocodes'][0]['citycode']

    return(citycode)

#print(get_route("102.416172,30.688095","101.846094,30.700282"))
