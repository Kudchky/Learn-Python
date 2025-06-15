from time import sleep
from requests_html import HTMLSession
import sys

url = "https://www.pccomponentes.com/asus-geforce-gtx-1050-tis-4gb-gddr5"

session = HTMLSession()


def check_stock():
    try:
        r = session.get(url)
        r.html.render(
            timeout=20
        )  # Renderiza JavaScript (necesario para páginas dinámicas)

        # Dos posibles selectores para detectar disponibilidad
        buy_button = r.html.find(".buy-button", first=True) or r.html.find(
            "#btnsWishAddBuy", first=True
        )

        if buy_button:
            print("¡HAY STOCK! 🎉")
            # Aquí podrías añadir una notificación más visible
            # como un sonido, email, etc.
            return True
        else:
            print("Sigue sin haber stock 😞")
            return False

    except Exception as e:
        print(f"Error al verificar stock: {str(e)}")
        return False


while True:
    if check_stock():
        # Si hay stock, puedes decidir terminar el script o continuar
        break  # Termina el script cuando encuentra stock
    sleep(30)  # Espera 30 segundos antes de volver a comprobar
