import json
import urllib

import xlwt

all_info_list = []  # 定义一个列表存储数据

try:

    for i in range(1, 100):
        # pageIndex = 2;  # 第几页 ,用i代替
        restUri = "https://sh.fang.lianjia.com/loupan/pudong-qingpu/pg" + str(i) + "/?_t=2";  # 链家-浦东-青浦地区
        PostParam = ""
        DATA = PostParam.encode('utf8')
        req = urllib.request.Request(url=restUri, data=DATA, method='GET')
        req.add_header('Content-type', 'application/x-www-form-urlencoded')
        r = urllib.request.urlopen(req).read()
        org_obj = json.loads(r.decode('utf8'))

        all_info_list.extend(org_obj['data']['list'])  # 将返回数据添加到总列表中
        print("请求完毕!" + str(i))

    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('ke_qq')
    keys = ['address', 'address_remark', 'average_price', 'avg_price_start', 'avg_price_start_unit', 'avg_unit_price',
            'min_frame_area','max_frame_area','subway_distance',
            'bizcircle_name', 'district_name', 'frame_rooms_desc', 'house_type', 'on_time', 'open_date']
    # 表头
    head = ['地址', '地标', '均价', '起步价', '单位', '单价',
            '最小面积', '最大面积','距离地铁',
            '商圈名称', '区名称', '居室类型', '房屋类型', '上线时间', '开盘时间']
    for h in range(len(head)):
        sheet.write(0, h, head[h])  # 写入表头
    i = 1
    for list_dict in all_info_list:
        j = 0
        for key in keys:
            sheet.write(i, j, list_dict[key])
            j += 1
        i += 1

    book.save('I:\spiderfile\ke.xls')
    print("---end----")
except Exception as e:
    print(e)
