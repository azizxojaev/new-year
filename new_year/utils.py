import qrcode
from core.settings import DOMEN
from random import choice
from django.conf import settings
import os
import time


def qr_code_make(qr_hash):
    url = f"{DOMEN}/gift/{qr_hash}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    fill_color = choice(['white', 'red'])
    back_color = choice(['white', 'red'])

    if fill_color == back_color and fill_color == 'white':
        back_color = 'red'
    elif fill_color == back_color and fill_color == 'red':
        back_color = 'white'

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(f"media/{qr_hash}.png")

    return f"media/{qr_hash}.png"


def delete_qr_image(filename):
    time.sleep(1)
    for item in os.scandir('media'):
        if item.name == filename:
            os.unlink(item)
