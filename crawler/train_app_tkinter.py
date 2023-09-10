# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 11:39:50 2023

@author: USER
"""

import tkinter as tk
from tools import init_app
from train import get_train_data
from datetime import datetime

def get_train():    
    try:
        df=get_train_data(startStation.get(),endStation.get(),rideDate.get(),
                       startTime.get(),endTime.get())    
        
        result.config(text='查詢成功!',fg='blue')
        data=df.iloc[:,[0,1,2,3,4,5,9,-1]]
        list_var.set(data.values.tolist())
        print(data)
    except Exception as e:
        print(e)
        result.config(text='查詢失敗',fg='red') 
    


font1=('標楷體',14)
font2=('標楷體',16)
font3=('標楷體',12)

app=init_app('400x600','台鐵查詢系統')

list_var=tk.StringVar()


tk.Label(app,text='起始站點名稱:',font=font1).pack()
startStation=tk.Entry(app,justify='center',font=font2,width=20)
startStation.pack(pady=5)
startStation.insert(0,'臺北')

tk.Label(app,text='終止站點名稱:',font=font1).pack()
endStation=tk.Entry(app,font=font2,width=20,justify='center')
endStation.pack(pady=5)
endStation.insert(0,'桃園')

tk.Label(app,text='乘車時間(ex:2023/7/30)',font=font1).pack()
rideDate=tk.Entry(app,font=font2,width=20,justify='center')
rideDate.pack(pady=5)
rideDate.insert(0,datetime.now().strftime('%Y/%m/%d'))

tk.Label(app,text='查詢起始時間(ex:00:00)',font=font1).pack()
startTime=tk.Entry(app,font=font2,width=20,justify='center')
startTime.pack(pady=5)
startTime.insert(0,'00:00')

tk.Label(app,text='詢終止時間(ex:23:59):',font=font1).pack()
endTime=tk.Entry(app,font=font2,width=20,justify='center')
endTime.pack(pady=5)
endTime.insert(0,'23:59')

tk.Button(app,text='查詢',font=font1,command=get_train).pack(pady=12)
result=tk.Label(app,text='查詢結果',font=font3)
result.pack(pady=5)
listbox = tk.Listbox(
    app, listvariable=list_var, font=font3, bg="aliceblue", fg="black"
    ,width=20,height=20
)
listbox.pack(fill="x")


app.mainloop()

