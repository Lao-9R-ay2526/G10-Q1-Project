# Generating A Receipt of Sky Dine
from pyscript import display, document

def receipt(e):
    name = document.getElementById("customer").checked

    has_burger = document.getElementById("burger").checked
    has_fries = document.getElementById("fries").checked
    has_shake = document.getElementById("shake").checked
    has_icecream = document.getElementById("icecream").checked

    burger_total = {has_burger} * 7.99
    fries_total = {has_fries} * 5.99
    shake_total = {has_shake} * 3.99
    icecream_total = {has_icecream} * 0.99

    full_total = {burger_total} + {fries_total} + {shake_total} + {icecream_total}


    display(f'Order Processed!', target="process")
    display(f'{full_total}', target="output")