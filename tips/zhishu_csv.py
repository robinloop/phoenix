# -*- coding: UTF-8 -*-
import csv
import requests
import sys
import getopt

URL_INDICE_FUNDAMENTAL = "https://open.lixinger.com/api/a/indice/fundamental"

stockNames = ["上证指数", "创业板指", "中证全指", "上证50", "沪深300", "中证500", "证券公司PB", "证券公司PE"]
stockCodes = ["1000004", "399006", "1000002", "000016", "000300", "000905", "399975"]
# date = "2019-03-19"


def get_data(date):
    request_data = {
      "token": "8ec3e830-0fe7-4734-844c-e23d6ea119e2",
      "stockCodes": stockCodes,
      "metrics": ["pb.median", "pe_ttm.median"],
      "date": date
    }
    result = requests.post(URL_INDICE_FUNDAMENTAL, json=request_data)
    result = result.json()
    if result['msg'] == 'success':
            fun_data = []
            last_pe = None
            for data in result['data']:
                fun_data.append(data['pb']['median'])
                last_pe = data['pe_ttm']['median']
            fun_data.append(last_pe)
            with open(date + ".csv", "w", newline="") as datacsv:
                # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
                csvwriter = csv.writer(datacsv, dialect=("excel"))
                # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
                csvwriter.writerow(stockNames)
                csvwriter.writerow(fun_data)


if __name__ == '__main__':
    args = sys.argv[1:]
    name = 'No Name'
    word = 'Hello'
    print( '数据获取中，请稍后......')

    if len(args) > 0:
        get_data(args[0])
    print('数据获取完毕，请在同目录下查看')
    sys.exit(0)

