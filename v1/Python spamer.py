import pyautogui as pag
import time


def prov(c1):
    try:
        c1 = int(c1)
        return c1
    except ValueError:
        c2 = pag.prompt(text='Введите коректное число', title='Spammer by BlackAlex', default='')
        return prov(c2)


s = pag.prompt(text='Введите текст для спама \nРАБОТАЕТ ТОЛЬКО АНГЛИЙСКИЙ', title='Spammer by BlackAlex', default='')
if s != None:
    c = pag.prompt(text='Кол-во отправленных сообщений', title='Spammer by BlackAlex', default='')
    if c != None:
        c = prov(c)
        if pag.confirm(
                    text='Поставьте курсор в поле отправки сообщения и поставьте английскую раскладку \nПосле нажатия кнопки ОК через 10 секунд начнется спам',
                    title='Spammer by BlackAlex', buttons=['OK', 'Отмена']) == 'OK':
                time.sleep(10)
                for i in range(c):
                    pag.write(s)
                    pag.press('enter')
pag.alert(text='Спасибо за использования Spammer by BlackAlex', title='Spammer by BlackAlex', button='OK')
