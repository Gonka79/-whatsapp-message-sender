# -whatsapp-message-sender
Este programa automatiza el envío de mensajes personalizados a través de WhatsApp Web. Utilizando datos de un archivo Excel, el programa envía mensajes a múltiples contactos de manera eficiente.
This project automates the process of sending personalized messages to clients via WhatsApp Web using Python, Selenium, and other essential libraries. The program reads client data from an Excel file and sends customized messages based on a pre-defined template.

# Features

Automated WhatsApp Messaging: Sends personalized messages to multiple clients using WhatsApp Web.

Customizable Message Template: Easily modify the message template to fit your needs.

Excel Integration: Reads client data (name, phone number, and optional custom message) from an Excel file (contactos.xlsx).

Graphical User Interface (GUI): Simple and intuitive interface built with Tkinter.


Logging: Tracks message sending activities in a log file (app.log) for easy debugging and monitoring.

# Requirements

**Python 3.x**

**Google Chrome (must be installed on your system)**

**ChromeDriver (compatible with your version of Chrome, included in the project)**

## >Required Python Libraries:<

1. pandas

2. selenium

3. Pillow

tkinter (usually included with Python installations)

## 
*****INSTALL*****

You can install all necessary libraries using pip:

$ `pip install pandas selenium pillow` (terminal & Console)

or

$ `pip install -r requirements.txt`

$ `git clone https://github.com/Gonka79/-whatsapp-message-sender.git`

cd whatsapp-message-sender

# **Run the Program:**

You can execute the program using Python:

$ `python whatsapp_bot.py`

# **Usage**

## Prepare Your Data:

Ensure you have an Excel file named contactos.xlsx in the same directory as the script.

The Excel file should have the following columns:

Telefono: The client's phone number (e.g., +1234567890).

Nombre: The client's name.

Mensaje: (Optional) A personalized message for the client. If left blank, the standard message template will be used.

## Customize the Message Template:

The message template is defined within the script (whatsapp_bot.py). To customize it, simply modify the mensaje_completo variable in the code:

`mensaje_completo = (
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
    "P.D.: Si tu PRODUCTO ADQUIRIDO EN NUESTRA TIENDA comienza a hablarte, prométenos que será la primera cosa que mencionarás en la reseña. 😄"
)`

## Run the Program:

Launch the program and click on "Enviar Mensajes". The program will automatically send the messages to all clients listed in the Excel file.

## View Logs:

## Customization

Message Template: Edit the mensaje_completo variable within the enviar_mensajes() function in whatsapp_bot.py to modify the message template.

Icon and Branding: Replace icono.ico, portada.png, and logo.png with your own images to customize the branding of the GUI.

## Troubleshooting

Message Not Sending: Ensure that ChromeDriver is correctly installed and compatible with your Chrome version.

Blank Fields in Excel: Ensure that each client has a phone number and name. The message is optional but can be customized for each client.

Error Logs: Check app.log for any errors or warnings during the message-sending process.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.

Check the app.log file in the project directory for detailed logs of the message-sending process.
