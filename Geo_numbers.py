#!/usr/bin/env python
#Author: Hacker NoDo
# Porfavor no borres el author#
import phonenumbers
from phonenumbers import carrier, geocoder
from colorama import init, Fore, Back, Style
print(Fore.GREEN+'''
 ## ##   ### ###   ## ##
##   ##   ##  ##  ##   ##
##        ##      ##   ##
##  ###   ## ##   ##   ##
##   ##   ##      ##   ##
##   ##   ##  ##  ##   ##
 ## ##   ### ###   ## ##

\n''')
print(
'''88b 88 88   88 8b    d8 88""Yb 888888 88""Yb .dP"Y8
88Yb88 88   88 88b  d88 88__dP 88__   88__dP `Ybo."
88 Y88 Y8   8P 88YbdP88 88""Yb 88""   88"Yb  o.`Y8b
88  Y8 `YbodP' 88 YY 88 88oodP 888888 88  Yb 8bodP'
\n''')
print("\t Visita mi Canal: https://youtube.com/@hackerNoDo \n")
def numChecker(phoneNumber):
    info = []
    phone = phonenumbers.parse(phoneNumber)
    info.append(geocoder.description_for_number(phone,"es"))
    info.append(carrier.name_for_number(phone,"es"))
    return info
print(Fore.RED+"Ejemplo: +569xxxxxxxx <=•\n")
phoneNumber = input(Fore.YELLOW+"Ingrese un numero de telefono:=>  ")
print(numChecker(phoneNumber))
print("Gracias por usar mi scrip.....✓")
