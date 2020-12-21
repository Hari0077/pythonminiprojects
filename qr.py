import pyqrcode

def qrcode():
    q=pyqrcode.create(input())
    q.png('qrcode.png',scale=6)
    print('QR code Generated')


if __name__ == "__main__":
    qrcode()