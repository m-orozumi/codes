#!/usr/bin/env python
# coding: utf-8

# In[4]:


## ライブラリインポート ##
# スクレイピング用
import requests
from bs4 import BeautifulSoup

# from time import sleep

import os

# データ保存用
import pandas as pd


## スクレイピング ##
# 対象サイトのURLを格納する
def retrieve(content):
    #url = "https://zdh.stagingbridge.net/"
    url = "https://zdh.stagingbridge.net/?s=AWS"

    # requestsを使用してhtmlを取得　→変数reqに格納
    #req = requests.get(url, params={'q': 'AWS'})
    req = requests.get(url)

    # 対象サイトへ負荷をかけないよう1sec待機
    # sleep(1)

    # 取得結果を解析してsoupに格納
    # BeautifulSoup(解析対象のHTML/XML, 利用するパーサー)
    soup = BeautifulSoup(req.content, "html.parser")

    # 本文が入っている「a」タグの「txt-link txt-nomal」*クラスを抽出
        #URLにアクセスしhtmlを取得　→取得対象のタイトル・URLが記載されているタグとクラスを確認して指定
    datas = soup.find_all("a", class_="txt-link txt-nomal")
    #datas　#動作確認用

    # 本文を抽出
    #data_list = datas.find_all("a")
    #datas[0].contents[0]
    #datas[0].attrs['href']
    #for data in datas:

    # 抽出結果をまとめる
    data_result = []

    for data in datas:
        # 抽出した本文をデータセットに格納する
        data_set = {
             'title': data.text
            ,'URL': data.attrs['href']
        }

    # 取得したデータセットをリストに格納する
    data_result.append(data_set)


## データを保存 ##
# data_resultを、データフレームに格納
df = pd.DataFrame(data_result)

# to_csv()を使って、データフレームをCSV出力する
df.to_csv("results.csv",index=None,encoding="utf-8-sig")