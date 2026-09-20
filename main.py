# Generating Receipt of Sky Dine
from pyscript import document, display

def receipt(e):
    name = document.getElementById("customer").value

    burger = document.getElementById("burger")
    fries = document.getElementById("fries")
    shake = document.getElementById("shake")
    icecream = document.getElementById("icecream")

    burger_total = float(burger.value) * burger.checked
    fries_total = float(fries.value) * fries.checked
    shake_total = float(shake.value) * shake.checked
    icecream_total = float(icecream.value) * icecream.checked

    full_total = burger_total + fries_total + shake_total + icecream_total

    display(
        f"Order Processed! Customer: {name} Total: ${full_total:.2f}",
        target="output"
    )
