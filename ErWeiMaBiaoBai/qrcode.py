import qrcode
img = qrcode.make('我喜欢你\n第一行是假的\n第二行也是假的')
img.show()
#img.save('qrcode.jpg')
