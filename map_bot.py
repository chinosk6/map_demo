import data_process as dat
import info_Request as req
import sys

def gnenrate_route(ori_city,ori_locate,dest_city,dest_locate): #路线规划 "1"
    ori_lola = dat.get_lonlat(ori_locate,ori_city)
    dest_lola = dat.get_lonlat(dest_locate,dest_city)
    path = dat.get_route(ori_lola,dest_lola,plan='walking') #driving,walking,bicycling,electrobike

    print(req.generate_img(ori_lola,dest_lola,path))

def gnenrate_where_on_bus(ori_city,ori_locate):  #上车点推荐 "2"
    lola = dat.get_lonlat(ori_locate,ori_city)

    stat = dat.where_on_bus(lola)

    print(stat)

#gnenrate_route("成都市","火星","成都市","地球")
#sys.exit()

msg = sys.argv #文件名 项目 参数1 参数2...
func = msg[1]

if(func != "1" and func != "2"):
    print("参数不正确")
    sys.exit()

if(len(msg) == 4): #4 - 2 个参数
    if(func == "1"):
        gnenrate_route("",msg[2],"",msg[3])
        sys.exit()
    elif(func == "2"):
        gnenrate_where_on_bus(msg[2],msg[3])
        sys.exit()

    else:
        print("处理异常")
        sys.exit()

if(len(msg) == 5): #5 - 2 = 3 个参数 
    if(func == "1"):
        gnenrate_route(msg[2],msg[3],msg[2],msg[4])
        sys.exit()

if(len(msg) == 6): #6 - 2 = 4 个参数 
    if(func == "1"):
        gnenrate_route(msg[2],msg[3],msg[4],msg[5])
        sys.exit()

if(len(msg) == 7): #7 - 2 = 5 个参数
    if(func == "1"):
        gnenrate_route(msg[3],msg[4],msg[5],msg[6],msg[2])
        sys.exit()

print("unexpected parameters")
#gnenrate_where_on_bus("成都市","xx路xx号")
#gnenrate_route("成都市","火星","成都市","地球")