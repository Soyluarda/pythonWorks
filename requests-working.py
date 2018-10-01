# -*- coding: utf-8 -*-
import requests
import json
from threading import Thread

def add_comment(id,post_id):
    ## veri almak istedigimiz url'i customer_list_url olarak tanımlıyoruz. isteklerimizi cekmek icin request kütüphanesi ile bu url'deki verileri customer_list'e atıyoruz ve json objesine ceviriyoruz.
    customer_list_url = "http://yourapi.com/api/get-customer-list"
    customer_list = requests.get(customer_list_url)
    json_customers = json.loads(customer_list.text)

    #yeni olusturdugumuz customer dictionary'e customer_listteki token ve id'leri ekliyoruz.
    customer_lists = []
    for i in json_customers:
        cust = {"token":i.get('token'), "id":i.get('id')}
        customer_lists.append(cust)

    ## benzer sekilde post_list olusturup verileri json'a cevirelim.
    post_list_url = "http://yourapi.com/api/get-post-list"
    post_list = requests.get(post_list_url)
    json_posts = json.loads(post_list.text)

    post_list_id = []
    for i in json_posts:
        post_list_id.append(i.get('id'))

    # bu kısımda url' tanımladıktan sonra göndermek istediğimizi parametreleri de params ile yolluyoruz.
    add_comment_url = "http://yourapi.com/api/add-comment"
    add_comment = requests.post(add_comment_url,params={"token":customer_lists[id].get('token'),"postId":post_list_id[post_id],"comment":"comment added","name":"Arda Soylu"})


for i in range(5):
    Thread(target=add_comment(i,3),args=(i),).start()
