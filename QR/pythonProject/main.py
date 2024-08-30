import pyqrcode

url=input("please enter url : ")
qr_code=pyqrcode.create(url)
qr_code.svg('qrcode.svg',scale=5)