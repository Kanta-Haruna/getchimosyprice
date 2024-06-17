# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep
from datetime import date
import glob


##chrom_path = '/Users/harunakanta/PythonTraining/chromedriver/chromedriver'
options = Options()
options.add_argument("--incognito")
##options.add_argument("--headless")
options.page_load_strategy = 'eager'

dic = {'place':[], 'price(tax included)': [], 'price*3(tax included)': [], 'shippingfee': [], 'URL': [], 'Date': []}
today = date.today()

##モノタロウのスクレイピング 関数にURLを引き渡す
def getmonotaro(url):
    mdriver = webdriver.Chrome(options=options)
    ln = []
    ##モノタロウのページを開く
    try:
        ln.append('モノタロウ')
        mdriver.get(url)
        ##モノタロウの税込金額が記載されている箇所を取得する
        monotaroPriceElement = mdriver.find_element(By.XPATH,'//*[@id="items"]/div[1]/div[3]/div[5]/span[2]').text
        ##取得した文字列をスペースで分割する
        monotaroPriceList = monotaroPriceElement.split(' ')
        ##モノタロウの販売価格を取得
        monotaroPrice = int(str(monotaroPriceList[1])[1:])
        ln.append(monotaroPrice)
        ##3個買った時の値段を取得
        monotaroPrice3 = monotaroPrice * 3
        ln.append(monotaroPrice3)
        ##送料計算
        if (monotaroPrice / 1.1) * 3 >= 3500:
            monotaroSouryo = 0
            ln.append(monotaroSouryo)
        else:
            monotaroSouryo = '550(合計金額が3500円以上なら無料)'
            ln.append(monotaroSouryo)
        ##ページを閉じる
        ln.append(url)
        ln.append(today)
        mdriver.close()
    ##リストを返す
    except:
        ln = ['モノタロウ', 0, 0, 0, 0,today]
        mdriver.close()
    return ln

def getyodobashi(url):
    ydriver = webdriver.Chrome(options=options)
    ln = []
    try:
        ln.append('ヨドバシ')
        ##ヨドバシのページを開く
        ydriver.get(url)
        ##販売価格取得
        yodobashielement = ydriver.find_element(By.XPATH,'//*[@id="js_scl_unitPrice"]').text
        yodobashiprice = int(yodobashielement[1:])
        ln.append(yodobashiprice)
        ##3個買った時の値段
        ln.append(yodobashiprice * 3)
        ##送料
        ln.append(0)
        ##URL取得、ページを閉じる
        ln.append(url)
        ln.append(today)
        ydriver.close()
    except:
        ln = ['ヨドバシ', 0, 0, 0, 0,today]
        ydriver.close()
    return ln

def getcharm(url):
    ln = []
    try:
        ln.append('チャーム')
        cdriver = webdriver.Chrome(options=options)
        ##チャームのサイトを開く
        cdriver.get(url)
        ##販売価格取得
        charmelement = cdriver.find_element(By.XPATH,'/html/body/div[1]/main/article/div[1]/div/div[2]/header/div/div/div/div[4]/div').text
        
        ##複数行取得されてしまうので、スペースで分割
        charmlist = charmelement.split(' ')
        ##分割された1つ目の値を抽出。¥マークとカンマを消去する
        charmprice3 = int(str(charmlist[0][1:]).replace(',', ''))
        ##1個当たりの値段を算出、小数点以下は切り捨て
        price = charmprice3 // 3
        ln.append(price)
        ln.append(charmprice3)
        ##送料を算出
        if charmprice3 >= 5980:
            souryo = 0
            ln.append(souryo)
        else:
            souryo = '730(合計が5980円以上で無料)'
            ln.append(souryo)
        
        ln.append(url)
        ln.append(today)
        cdriver.close()
    except:
        ln = ['チャーム', 0, 0, 0, 0,today]
        cdriver.close()
    return ln


def getkoko(url):
    ln = []
    try:
        ln.append('ココデカウ')
        kdriver = webdriver.Chrome(options=options)
        ##site open
        kdriver.get(url)
        ##get price
        kprice = kdriver.find_element(By.XPATH, '//*[@id="infobox"]/div[1]/div[3]/div[2]/span/span/div/nobr[1]/span[1]').text
        ln.append(int(kprice))
        ln.append(int(kprice) * 3)
        if int(int(kprice) * 3) >= 3300:
            souryo = 0
            ln.append(souryo)
        else:
            souryo = '499(合計が3300円以上で無料)'
            ln.append(souryo)
        ln.append(url)
        ln.append(today)
        kdriver.close()
    except:
        ln = ['ココデカウ', 0, 0, 0, 0,today]
        kdriver.close()
    return ln


def getbig(url):
    ln = []
    try:
        ln.append('ビックカメラ')
        bdriver = webdriver.Chrome(options=options)
        sleep(5)
        
        bdriver.get(url)
        
        price = bdriver.find_element(By.XPATH, '/html/body/section/form/div[1]/div[1]/table[1]/tbody/tr[2]/td/p/strong').text
        ln.append(int(price[:-1]))
        ln.append(int(price[:-1]) * 3)
        sleep(2)
        if int(price[:-1]) * 3 >= 2000:
            souryo = 0
            ln.append(souryo)
        else:
            souryo = '550(合計が2000円以上で無料)'
            ln.append(souryo)
        sleep(2)
        ln.append(url)
        ln.append(today)
        sleep(2)
        bdriver.close()
    except:
        ln = ['ビックカメラ', 0, 0, 0, 0,today]
        bdriver.close()
    return ln


def makedf():
    monotaro = getmonotaro('https://www.monotaro.com/p/6152/2276/?cq_med=pla&cq_plt=gp&utm_medium=cpc&utm_source=google&utm_campaign=246-833-4061_6466659573_shopping&utm_content=77481174716&utm_term=_380686959515_x_aud-368712506548:pla-1930216600975&utm_id=61522276&gad_source=1&gclid=CjwKCAjwyJqzBhBaEiwAWDRJVLZOwpeiP34Ha6hmrQgkvbAMfu-9jMeOfn1UjE7mD-lU1cjbmtGsIRoC2zkQAvD_BwE')  
    yodobashi = getyodobashi('https://www.yodobashi.com/product/100000001006045579/?gad1=&gad2=x&gad3=&gad4=&gad5=3653954074046849911&gad6=&gad_source=1&gclid=CjwKCAjwyJqzBhBaEiwAWDRJVLTXrC2JXHFkdJfcS1OyKngX6dWmJ3BdR4-_sR-XPp54wO02LjJnQRoCVSoQAvD_BwE&xfr=pla')
    charm = getcharm('https://www.shopping-charm.jp/product/2c2c2c2c-2c2c-2c2c-2c2c-323637363133')
    koko = getkoko('https://www.cocodecow.com/coco/gi/CD0954/')
    big = getbig('https://www.biccamera.com/bc/item/11076619/')
    n = 0
    
    for i in dic.keys():
        dic[i].append(monotaro[n])
        dic[i].append(yodobashi[n])
        dic[i].append(charm[n])
        dic[i].append(koko[n])
        dic[i].append(big[n])
        n += 1
    df = pd.DataFrame(dic)
    csvfile = '/Users/harunakanta/PythonTraining/csv/chimosy.csv'
    l = glob.glob(csvfile)
    
    if l == []:
        df.to_csv(csvfile, encoding='shift_jis', index=False)
        return df
    else:
        readcsv = pd.read_csv(csvfile, encoding='shift_jis')
        result = pd.concat([readcsv, df])
        result.to_csv(csvfile, encoding='shift_jis', index=False)
        return result



