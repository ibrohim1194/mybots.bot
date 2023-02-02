import qrcode
manzil = "https://www.instagram.com/ibrohim.11.94/?next=%2F"

qrcode.make(manzil).save("code.jpg")