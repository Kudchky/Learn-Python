import time
from selenium import webdriver # Permite usar herramienta webdriver para controlar navegador
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options  # Opciones especiales para abrir navegador
from selenium.webdriver.chrome.service import Service # Usa ayudante Service para arrancar navegador
from selenium.webdriver.common.by import By


def create_options(browser):
    options_fun = Options()  # Creando opciones, reglas para ver como abrir el navegador
    options_fun.binary_location = browser  # Le indicamos que usaremos Brave
    return options_fun


def create_manager(options_par):
    service = Service() # Creamos ayudante que se encargue de iniciar el navegador
    return webdriver.Chrome(service=service, options=options_par)  # Abre navegador usando ayudante y las
    # reglas que escribimos, control remoto para manejar el navegador


def open_page(driver_fun):
    url = "https://www.pccomponentes.com/sony-playstation-5-digital-slim"
    # url = "https://www.pccomponentes.com/asus-geforce-gtx-1050-tis-4gb-gddr5"
    driver_fun.get(url) # Usa el navegador para abrir esta página web como si lo buscara yo mismo,
    while True:
        try:
            button = driver_fun.find_element(By.ID, "pdp-add-to-cart")
            time.sleep(5)
            if button.is_enabled():
                print("Button found, ready to click ")
                break
        except NoSuchElementException:
            print("The button was not found... ")

        time.sleep(5)
        driver_fun.refresh()


def main():
    options = create_options("/usr/bin/brave-browser")
    driver = create_manager(options)
    open_page(driver)


if __name__ == "__main__":
    main()
