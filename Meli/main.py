import pyautogui as pt
import time


def open_search_page(title, price):
    tab = pt.locateOnScreen('publi_tab.png', confidence=.8)
    tab2 = pt.locateOnScreen('publi_tab2.png', confidence=.8)
    if tab:
        pt.moveTo(tab)
    elif tab2:
        pt.moveTo(tab2)
    else:
        exit()
    pt.click()
    time.sleep(1)
    # search_book(title, price)

def modificar_precio(precio):
    location_p = pt.locateCenterOnScreen('modificar_precio.png', confidence=.8)
    if location_p:
        pt.moveTo(location_p)
        pt.middleClick()
        time.sleep(3)
        location2 = pt.locateOnScreen('meli_modificar.png')
        pt.moveTo(location2)
        pt.click()
        time.sleep(1)
        location3 = pt.locateOnScreen('signo_pesos.png', confidence=.8)
        pt.moveTo(location3[0] + 10, location3[1] + 5)
        pt.doubleClick()
        pt.typewrite(precio)
        time.sleep(1)
        location4 = pt.locateOnScreen('confirmar.png', confidence=.8)
        pt.moveTo(location4)
        pt.click()
        time.sleep(3)
        location_confirmar2 = pt.locateOnScreen('confirmar2.png', confidence=.8)
        if location_confirmar2:
            pt.moveTo(location_confirmar2)
            pt.click()


def search_book(title, price):
    location = pt.locateCenterOnScreen('busqueda.png', confidence=.8)
    if location:
        pt.moveTo(location)
        pt.click()
        pt.typewrite(title, interval=0.1)
        pt.typewrite('\n')
        time.sleep(4)
        modificar_precio(price)
    else:
        print('no se encontró el buscador vacío, buscando la cruz...')
        location = pt.locateOnScreen('cruz_filtro.png', confidence=.8)
        if location:
            pt.moveTo(location[0] - 50, location[1] + 5)
            pt.tripleClick()
            pt.typewrite(title, interval=0.05)
            pt.typewrite('\n')
            modificar_precio(price)
        else:
            print('no se encontró el buscador.')


def main():
    book_name = input('enter book name> ')
    book_price = input('enter new price> ')
    time.sleep(3)
    open_search_page(book_name, book_price)


if __name__ == '__main__':
    main()
