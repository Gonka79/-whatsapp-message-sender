import tkinter as tk
from tkinter import messagebox, PhotoImage
import pandas as pd
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
import logging
import os

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
    time.sleep(6)

    for index, row in df.iterrows():
        if pd.isna(row['Telefono']) or pd.isna(row['Nombre']):
            continue

        telefono = str(row['Telefono'])
        nombre = row['Nombre']
        mensaje_personalizado = remove_non_bmp_characters(row['Mensaje'] if pd.notna(row['Mensaje']) else '')
        mensaje_completo = (
            f"Estimad@ {nombre},\n\n"
            f"{mensaje_personalizado}\n\n"
            "Esperamos que estés disfrutando de tu nuevo producto y que esté siendo el compañero perfecto para todas tus aventuras (¡o siestas!). "
            "Tenemos una pequeña misión para ti, que no involucra salir en una búsqueda épica ni nada por el estilo. "
            "Solo necesitamos tus súper habilidades de escritura para dejarnos una reseña en Google. ¡Prometemos que no te llevará más tiempo que el que tardas en decir 'sofá cama con apertura italiana'!\n\n"
            "Deja que el mundo sepa qué tal te fue con nosotros y si te ha sacado alguna sonrisa (o varias). Tu opinión es muy valiosa y nos ayuda a seguir mejorando y creciendo. "
            "¡Gracias por ser parte de nuestra familia y esperamos leerte pronto!\n\n"
            "Puedes dejar tu reseña pinchando en este enlace mágico:\n\n"
            "➡️ https://g.page/r/CaU_e6S1DYMIEBE/review ⬅️\n\n"
            "Saludos cordiales, MERKADESCANSO HUELVA\n\n"
            "P.D.: Si tu PRODUCTO ADQUIRIDO EN NUESTRA TIENDA comienza a hablarte, prométenos que será la primera cosa que mencionarás en la reseña. "
        )

        try:
            driver.find_element("xpath", "//div[@title='Nuevo chat']").click()
            time.sleep(2)
            search_box = driver.find_element("xpath", "//div[@contenteditable='true' and @data-tab='3']")
            search_box.click()
            search_box.send_keys(telefono)
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)
            time.sleep(2)

            message_box = driver.find_element("xpath", "//div[@aria-placeholder='Escribe un mensaje']")
            message_box.click()
            message_box.send_keys(mensaje_completo)
            time.sleep(1)

            send_button = driver.find_element("xpath", "//button[@aria-label='Enviar']")
            send_button.click()
            logging.info(f"Mensaje enviado a {nombre} al número {telefono}.")
            time.sleep(2)
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
root.geometry("600x750")  # Ampliar la altura de la ventana para asegurar que el texto del creador sea visible

# Establecer el icono de la ventana (asegúrate de que icono.ico esté en el directorio correcto)
root.iconbitmap("C:/Users/Gonka79/Downloads/Programa msj whasapp/icono.ico")

# Establecer el color de fondo
root.configure(bg='#3d7590')

# Cargar y mostrar la imagen de portada
portada_path = "portada.png"
if os.path.exists(portada_path):
    try:
        portada = Image.open(portada_path)
        portada = portada.resize((500, 500), Image.Resampling.LANCZOS)  # Mantener la proporción cuadrada de la imagen
        portada_img = ImageTk.PhotoImage(portada)
        portada_label = tk.Label(root, image=portada_img, bg='#3d7590')
        portada_label.pack(pady=5)
    except Exception as e:
        logging.error(f"Error al cargar la imagen de portada: {e}")
else:
    logging.error(f"Imagen de portada no encontrada: {portada_path}")

# Botón para enviar mensajes
boton_enviar = tk.Button(root, text="Enviar Mensajes", command=enviar_mensajes, font=("Arial", 14), bg="#51a8c7", fg="white")
boton_enviar.pack(pady=10)

# Cargar logo de la empresa
logo_path = "logo.png"
if os.path.exists(logo_path):
    try:
        logo = PhotoImage(file=logo_path)  # Asegúrate de que el logo esté en el mismo directorio o proporciona la ruta completa
        logo_label = tk.Label(root, image=logo, bg='#3d7590')
        logo_label.pack(pady=10)
    except Exception as e:
        logging.error(f"Error al cargar el logo: {e}")
else:
    logging.error(f"Logo no encontrado: {logo_path}")

# Etiqueta de autor en la parte inferior
autor_label = tk.Label(root, text="Creado por Sp1d3r aka Gonka_Huelva", font=("Arial", 10, "bold"), fg="white", bg="#3d7590")
autor_label.pack(pady=15)

root.mainloop()
