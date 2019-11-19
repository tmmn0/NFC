import datetime
import openpyxl
import nfc
import binascii

#NFC情報取得
clf = nfc.ContactlessFrontend('usb')  #カードリーダーと接続を行う。デバイスの中から見つかったものに接続
print('touch card:')
try:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
finally:
    clf.close()
card = binascii.hexlify(tag.idm)
print(card)

xlsx_file = "nfclist.xlsx"

# エクセルブック
wb = openpyxl.load_workbook(xlsx_file, data_only=True)

# エクセルシート
ws = wb["Sheet1"]
namelist = []
idmlist = []


# ヘッダーを除いて順番に読み込む
for row in ws.iter_rows(min_row=2):
    # 学籍番号
    member_number = row[0].value
    # 氏名
    member_name = row[1].value
    # idm
    member_idm = row[2].value

    namelist.append(member_name)
    idmlist.append(member_idm)

print(namelist)
print(idmlist)

print (idmlist.index(card) ) #ココがエラー出る



    #print(f"{row[1].value}")
