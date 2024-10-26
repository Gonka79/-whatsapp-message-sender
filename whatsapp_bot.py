import tkinter as tk
from tkinter import messagebox, PhotoImage
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
import logging
import random

# Configuración del sistema de logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def remove_non_bmp_characters(text):
    """Elimina caracteres fuera del Basic Multilingual Plane (BMP)"""
    if text:
        return ''.join(char for char in text if ord(char) <= 0xFFFF)
    return ''

def configure_chrome_options():
    """Configura las opciones de Chrome necesarias para Selenium"""
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:/Users/Gonka79/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("profile-directory=Profile 1")
    return chrome_options

def enviar_mensajes():
    """Función para enviar mensajes a contactos listados en un archivo Excel"""
    df = pd.read_excel('contactos.xlsx')
    driver = webdriver.Chrome(options=configure_chrome_options())
    driver.get("https://web.whatsapp.com")
    time.sleep(8)  # Tiempo para escanear el código QR

    for index, row in df.iterrows():
        if pd.isna(row['Telefono']) or pd.isna(row['Nombre']):
            continue  # Salta las filas que no tienen teléfono o nombre

        telefono = str(row['Telefono'])
        nombre = row['Nombre']
        mensaje_personalizado = remove_non_bmp_characters(row['Mensaje'] if pd.notna(row['Mensaje']) else '')
        mensaje_completo = (
            f"Hola {nombre},\n\n"
            f"{mensaje_personalizado}\n\n"
            f"Ya sabes, ese producto que no solo es bueno para las siestas, sino también para presumirlo con orgullo. "
            "Por cierto, si te sobra un minuto (o dos si eres de los que escriben rápido), "
            "nos harías un gran favor dejando una reseña sobre tu experiencia. ¡Tu opinión es más valiosa que encontrar wifi gratis en un aeropuerto! "
            "Nos encantaría que cuentes tu historia (y si el producto empieza a hablarte, queremos saberlo primero)."
            "\n\n➡️ https://g.page/r/CaU_e6S1DYMIEBE/review ⬅️\n\n"
            "Gracias por ser parte de nuestra familia de aventureros de sofá. ¡SALUDOS DE MERKADESCANSO!"
        )

        try:
            driver.find_element("xpath", "//div[@title='Nuevo chat']").click()
            time.sleep(random.uniform(6, 8))  # Pausa aleatoria antes de iniciar nuevo chat

            search_box = driver.find_element("xpath", "//div[@contenteditable='true' and @data-tab='3']")
            search_box.click()
            search_box.send_keys(telefono)
            time.sleep(random.uniform(6, 8))  # Pausa aleatoria para simular tiempo de búsqueda del contacto
            search_box.send_keys(Keys.ENTER)
            time.sleep(random.uniform(6, 8))  # Pausa aleatoria para abrir el chat

            # Localizar el cuadro de texto de mensaje y escribir el mensaje
            message_box = driver.find_element("xpath", "//div[@aria-placeholder='Escribe un mensaje']")
            message_box.click()
            message_box.send_keys(mensaje_completo)
            time.sleep(random.uniform(6, 8))  # Pausa antes de enviar el mensaje

            send_button = driver.find_element("xpath", "//button[@aria-label='Enviar']")
            send_button.click()
            logging.info(f"Mensaje enviado a {nombre} al número {telefono}.")
            time.sleep(random.uniform(6, 8))  # Pausa aleatoria entre envíos para evitar detección de spam

        except NoSuchElementException as e:
            logging.error(f"Error al enviar el mensaje a {nombre}: {e}")
            messagebox.showerror("Error", f"No se pudo enviar el mensaje a {nombre}. Elemento no encontrado: {str(e)}")
            continue

    driver.quit()
    logging.info("Todos los mensajes han sido enviados y el driver se ha cerrado correctamente.")
    messagebox.showinfo("Éxito", "Todos los mensajes han sido enviados exitosamente!")

# Configuración de la interfaz gráfica de usuario
root = tk.Tk()
root.title("Enviar Mensajes por WhatsApp")
root.geometry("500x400")  # Tamaño más grande de la ventana

# Cargar logo de la empresa (reemplazar 'logo.png' con la ruta correcta del logo)
try:
    logo = PhotoImage(file="logo.png")  # Asegúrate de que el logo esté en el mismo directorio o proporciona la ruta completa
    logo_label = tk.Label(root, image=logo)
    logo_label.pack(side=tk.BOTTOM, pady=10)
except Exception as e:
    logging.error(f"Error al cargar el logo: {e}")

# Botón para enviar mensajes
boton_enviar = tk.Button(root, text="Enviar Mensajes", command=enviar_mensajes, font=("Arial", 14), bg="green", fg="white")
boton_enviar.pack(pady=30)

# Etiqueta de autor en la esquina inferior
autor_label = tk.Label(root, text="Creado por Sp1d3r aka Gonka_Huelva", font=("Arial", 10))
autor_label.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
