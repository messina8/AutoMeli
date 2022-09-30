import pyautogui as pt
import time
import ficha_tecnica
import precio





def price():
    book_name = input('enter book name> ')
    book_price = input('enter new price> ')
    time.sleep(2)
    precio.cambiar_precio_publicacion(book_name, book_price)

def ficha():
    time.sleep(2)
    ficha_tecnica.rellenar_ficha_tecnica()


if __name__ == '__main__':
    price()
    ficha()
