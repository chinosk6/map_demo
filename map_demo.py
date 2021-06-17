import data_process as dat
import info_Request as req

def gnenrate_route(ori_city,ori_locate,dest_city,dest_locate): #路线规划
    ori_lola = dat.get_lonlat(ori_locate,ori_city)
    dest_lola = dat.get_lonlat(dest_locate,dest_city)
    path = dat.get_route(ori_lola,dest_lola,plan='driving') #driving,walking,bicycling,electrobike

    print(req.generate_img(ori_lola,dest_lola,path))

def gnenrate_where_on_bus(ori_city,ori_locate):  #上车点推荐
    lola = dat.get_lonlat(ori_locate,ori_city)

    stat = dat.where_on_bus(lola)

    print(stat)

#gnenrate_where_on_bus("北京市","故宫")
#gnenrate_route("成都市","火星","北京市","八达岭长城")