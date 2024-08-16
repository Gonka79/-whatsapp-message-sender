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

*Python 3.x

*Google Chrome (must be installed on your system)

*ChromeDriver (compatible with your version of Chrome, included in the project)

>Required Python Libraries:<

1. pandas

2. selenium

3. Pillow

tkinter (usually included with Python installations)

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

##Customize the Message Template:

The message template is defined within the script (whatsapp_bot.py). To customize it, simply modify the mensaje_completo variable in the code:

