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
            pt.scroll(-100)
            ficha_location = pt.locateOnScreen('ficha/ficha_incompleta.png', confidence=.9)
            ficha_completa = pt.locateOnScreen('ficha/ficha_completa.png', confidence=.9)
        if ficha_completa:
            print('La ficha ya está completa.')
        elif ficha_location:
            pt.moveTo(ficha_location)
            pt.click()
            pt.typewrite('0')
        confirmar_location = pt.locateOnScreen('confirmar.png', confidence=.9)
        while not confirmar_location:
            next_location = pt.locateAllOnScreen('ficha/completa.png', confidence=.8)
            next_yes_no = pt.locateAllOnScreen('ficha/si_no.png', confidence=.9)
            if next_location:
                for i in next_location:
                    pt.moveTo(i)
                    pt.click()
                    pt.typewrite('0')
            elif next_yes_no:
                for i in next_yes_no:
                    pt.moveTo(i)
                    pt.click()
            confirmar_location = pt.locateOnScreen('confirmar.png', confidence=.9)
            pt.scroll(-50)
            time.sleep(.5)
        time.sleep(.5)
        pt.moveTo(confirmar_location)
        pt.click()

    else:
        print('no estoy encontrando nada')
