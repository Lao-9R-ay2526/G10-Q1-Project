# Generating SKU
from pyscript import display, document

# Angelic Burger
def burger(e):
    user = document.getElementById('name').value
    sku = 'SK-BRGR'

    display(f'Thank you {user}!', target="total1")
    display(f'Your Angelic Burger Is In the Process of Going Sky High', target="total2")
    display(f'Order SKU: {sku}', target="total3")

# Golden Fries
def fries(e):
    user = document.getElementById('name').value
    sku = 'SK-FS'

    display(f'Thank You {user}!', target="total1")
    display(f'The Golden Gates are on the way to a savory delight!', target="total2")
    display(f'Order SKU: {sku}', target="total3")

# Heavenly Shake
def shake(e):
    user = document.getElementById('name').value
    sku  = 'SK-SE'

    display(f'Thank You {user}!', target="total1")
    display(f'Your Heavenly Shake Is Made with Blessing!', target="total2")
    display(f'Order SKU: {sku}', target="total3")

def icecream(e):
    user = document.getElementById('name').value
    sku = 'SK-ATMFR'

    display(f'Thank you {user}!', target="total1")
    display(f'Your Atmospheric Flavor Ice Cream is Sent Through Ya!', target="total2")
    display(f'Order SKU: {sku}', target="total3")