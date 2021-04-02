import qrcode

input_data = 'Testiño 1 2 3.';

qr = qrcode.QRCode(			#Creating an instance of qrcode
        version=1,
        box_size=10,
        border=5)

qr.add_data(input_data)

qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save('qrcode001.png')
