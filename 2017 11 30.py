#!/usr/bin/env python
# -*- coding :utf-8 -*-
import time
from multiprocessing.dummy import pool as Threadpool
import sys
import requests
from lxml  import etree
import json
import pymongo


def get_response(url)
    html = requests.get(url,hearders = headers)
    selector = etree.HTML(html.text)
    product_list = selector.xpath('//*[@id="J_goodslist"]/ul/li')
    for product in product_list:
        try:
            sku_id = product.xpath('@data-sku')[0]
            product_url = 'https://item.jd.com/{}.html.format(str(sku_id))'
            get_data(product_url)
        except Exception as e:
            print e





def get_data(product_url):


    product_dict = {}
    html = requests.get(product_url,headers=headers)
    selector = etree.HTML(html.text)
    product_infos = selector.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[3]')
    for product in product_infos:
        product_number = product.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[3]/li[2]')[0]
        product_prict = get_product_price.xpath(product_number)

        product_dict['商品名称 '] = product.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[3]/li[1]')[0]
        product_dict['商品id'] = product_number
        product_dict['商品产地'] = product.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[3]/li[4]')[0]

    print product_dict
    save(product_dict)


def get_product_price(sku):




    price_url = 'https://p.3.cn/prices/mgets?&skuIds=J_{}'.format(str(sku))
    reponse = requests.get(price_url,headers=headers).content
    respose_json = json.loads(response)
    for info in response_json:
        return info.get('p')
    pass

def save(list):

    client = pymongo.MongoClient('localhost')
    db = client['product_dict']
    content = db['jd']
    content.insert(product_list)





if __name__ == '__main__':
    headers ={
    'User-Agent':'Morilla/5.0 (Window NT 6.1:Win64; x64) Applewekit/537.36(KHTML,Like Gecko)chorm/59.0.3071.115 safari/537.36 '

}
    url = ['https://list.jd.com/list.html?cat=9987,653,655']
    pool = Threadpool(2)
    start_time = time.time()
    pool.map(get_response,urls)
    pool. close()
    pool.join()
    end_time = time.time()
    print u'用时{}秒'.format(str(end_time-start_time))



