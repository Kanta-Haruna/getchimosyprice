#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:29:24 2024

@author: harunakanta
"""

import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

def plot():
    csvfile = '/Users/harunakanta/PythonTraining/csv/chimosy.csv'
    df = pd.read_csv(csvfile, encoding='shift-jis')
    
    fig, ax = plt.subplots()
    
    c1,c2,c3,c4,c5 = "blue","green","red","black", "purple"
    l1,l2,l3,l4,l5 = 'モノタロウ', 'ヨドバシ', 'チャーム', 'ココデカウ', 'ビックカメラ'
    
    x1 = df[df['place'] == l1]['Date']
    x2 = df[df['place'] == l2]['Date']
    x3 = df[df['place'] == l3]['Date']
    x4 = df[df['place'] == l4]['Date']
    x5 = df[df['place'] == l5]['Date']
    
    y1 = df[df['place'] == l1]['price(tax included)']
    y2 = df[df['place'] == l2]['price(tax included)']
    y3 = df[df['place'] == l3]['price(tax included)']
    y4 = df[df['place'] == l4]['price(tax included)']
    y5 = df[df['place'] == l5]['price(tax included)']
    
    ax.set_title('価格推移')
    ax.grid() 
    
    ax.plot(x1, y1, color=c1, label=l1, marker='o',)
    ax.plot(x2, y2, color=c2, label=l2, marker='o',)
    ax.plot(x3, y3, color=c3, label=l3, marker='o',)
    ax.plot(x4, y4, color=c4, label=l4, marker='o',)
    ax.plot(x5, y5, color=c5, label=l5, marker='o',)
    ax.legend(loc=0)    # 凡例
    fig.tight_layout()  # レイアウトの設定
    # plt.savefig('hoge.png') # 画像の保存
    plt.show()
plot()
