from importlib import import_module
from random import randint
import datetime
st = datetime.datetime.now()
que = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
num = randint(0,2)
print(que[num])

ans = input("回答を入力：")
if num == 0:
    if ans == "ますお" or "マスオ":
        print("正解")
    else:
        print("不正解")
if num == 1:
    if ans == "わかめ" or "ワカメ":
        print("正解")
    else:
        print("不正解")
if num == 2:
    if ans == "甥" or "おい" or "甥っ子" or "おいっこ":
        print("正解")
    else:
        print("不正解")
ed = datetime.datetime.now()
print((ed-st).seconds)