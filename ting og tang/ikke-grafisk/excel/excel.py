import xlwings as xw
import time

wb = xw.Book('XO.xlsx')
sht1 = wb.sheets['Sheet']

sht1.range('A1').value = 1
sht1.range('B1').value = 2
sht1.range('C1').value = 3
sht1.range('A2').value = 4
sht1.range('B2').value = 5
sht1.range('C2').value = 6
sht1.range('A3').value = 7
sht1.range('B3').value = 8
sht1.range('C3').value = 9
sht1.range('B5').value = ""

vinning = False

while True:
    if sht1.range('A1').value == sht1.range('A2').value and sht1.range('A2').value == sht1.range('A3').value:
        vinning = True
        vinner = sht1.range('A1').value
    if sht1.range('B1').value == sht1.range('B2').value and sht1.range('B2').value == sht1.range('B3').value:
        vinning = True
        vinner = sht1.range('B1').value
    if sht1.range('C1').value == sht1.range('C2').value and sht1.range('C2').value == sht1.range('C3').value:
        vinning = True
        vinner = sht1.range('C1').value
    if sht1.range('A1').value == sht1.range('B1').value and sht1.range('B1').value == sht1.range('C1').value:
        vinning = True
        vinner = sht1.range('A1').value
    if sht1.range('A2').value == sht1.range('B2').value and sht1.range('B2').value == sht1.range('C2').value:
        vinning = True
        vinner = sht1.range('A2').value
    if sht1.range('A3').value == sht1.range('B3').value and sht1.range('B3').value == sht1.range('C3').value:
        vinning = True
        vinner = sht1.range('A3').value
    if sht1.range('A1').value == sht1.range('B2').value and sht1.range('B2').value == sht1.range('C3').value:
        vinning = True
        vinner = sht1.range('A1').value
    if sht1.range('A3').value == sht1.range('B2').value and sht1.range('B2').value == sht1.range('C1').value:
        vinning = True
        vinner = sht1.range('A3').value
    
    if vinning == True:
        sht1.range('B5').value = f"{vinner} vant!"

    time.sleep(0.5)