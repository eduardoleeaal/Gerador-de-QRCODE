# Import QRCode from pyqrcode
import pyqrcode                                 # pyqrcode
import png                                      # pypng
from PySimpleGUI import PySimpleGUI as sg
from PIL import Image

sg.theme('Dark')

layout = [
    [sg.Text('Link: '), sg.Input(key = '_link', size = (20, 1))],
    [sg.Text('Nome do QR: '), sg.Input(key = '_nome', size = (20, 1))],
    [sg.Button('Confirmar', key='_butao')]
]
janela = sg.Window('Criador de QRCODE', layout)

while True:
    eventos, valores = janela.read()
    nome = valores['_nome']
    link = valores['_link']
    break

if 'https://' not in link:
    link = 'https://'+link

url = pyqrcode.create(link)
url.png(nome+'.png', scale = 8) 

img = Image.open(nome+'.png')
img.show()
