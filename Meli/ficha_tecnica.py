import pyautogui as pt
import time


def rellenar_ficha_tecnica():
    location = pt.locateOnScreen('meli_modificar.png', confidence=.9)
    if location:
        pt.moveTo(location)
        pt.click()
        time.sleep(.5)
        pt.moveTo(700, 700)
        pt.scroll(+2000)

        ficha_location = pt.locateOnScreen('ficha/ficha_incompleta.png', confidence=.9)
        ficha_completa = pt.locateOnScreen('ficha/ficha_completa.png', confidence=.9)
        while not ficha_location and not ficha_completa:
            pt.scroll(-300)
            ficha_location = pt.locateOnScreen('ficha/ficha_incompleta.png', confidence=.9)
            ficha_completa = pt.locateOnScreen('ficha/ficha_completa.png', confidence=.9)
        if ficha_completa:
            print('La ficha ya está completa.')
            exit()
        elif ficha_location:
            pt.moveTo(ficha_location)
            pt.click()
            pt.typewrite('0')
        confirm_location = pt.locateOnScreen('confirmar.png', confidence=.9)
        while not confirm_location:
            next_location = pt.locateAllOnScreen('ficha/completa.png', confidence=.8)
            next_yes_no = pt.locateAllOnScreen('ficha/si_no.png', confidence=.9)
            tapa_location = pt.locateOnScreen('ficha/tapa_libro.png', confidence=.7)
            if tapa_location:
                pt.moveTo(tapa_location)
                pt.click()
                pt.moveRel(0, 100)
                pt.click()
            for i in next_location:
                pt.moveTo(i)
                pt.click()
                pt.typewrite('0')
            for i in next_yes_no:
                pt.moveTo(i)
                pt.click()
            pt.scroll(-500)
            confirm_location = pt.locateOnScreen('confirmar.png', confidence=.9)
            time.sleep(.5)
        time.sleep(.5)
        pt.moveTo(confirm_location)
        pt.click()

    else:
        print('no estoy encontrando nada')
