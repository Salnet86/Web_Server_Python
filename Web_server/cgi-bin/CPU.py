#!/usr/bin/env python3
#dos2unix /home/utente/Scrivania/brezza/cgi-bin/temp.py
# -*- coding: utf-8 -*-

'''
import random as rd

def CPU():
    print("Content-type: text/html\r\n")
    
    print("""
    <html>
    <head>
        <meta charset='UTF-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Temperature and Humidity</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #e0f7fa; /* Blu chiaro */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            header {
                background: rgba(129, 199, 132, 0.8); /* Lime con trasparenza */
                color: #fff;
                padding: 10px 20px;
                width: 100%;
                text-align: center;
            }
            nav {
                margin: 20px 0;
            }
            nav a {
                margin: 0 15px;
                color: #fff;
                text-decoration: none;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 1.2em;
                text-align: center;
            }
            button {
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 1em;
                background-color: #4caf50; /* Verde */
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049; /* Verde scuro */
            }
            @media (max-width: 600px) {
                p {
                    font-size: 1em;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>CPU Virtuale</h1>
            <nav>
                <a href="http://localhost:8010/">Index</a>
                <a href="http://localhost:8010/documenti/manuale.pdf">Manuale</a>
                <a href="http://localhost:8010/cgi-bin/Tempe.py">Temp epoca</a>
            </nav>
        </header>
    """)

    # Genera una temperatura casuale per la CPU
    Temperatura_Cpu = rd.randint(30, 90) 
    temp_threshold = 70
    
    if Temperatura_Cpu > temp_threshold:
        print(f'<p style="color:red;">La temperatura CPU ha superato i: {Temperatura_Cpu}°C</p>')
    else:
        print(f'<p style="color:green;">Valore temperatura CPU: {Temperatura_Cpu}°C</p>')

    print("""
        <button onclick="location.reload();">Ricarica</button>
    </body>
    </html>
    """)

CPU()


'''
import random as rd

def CPU():
    print("Content-type: text/html\r\n")
    
    print("""
    <html>
    <head>
        <meta charset='UTF-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Temperature and Humidity</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #e0f7fa; /* Blu chiaro */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            header {
                background: rgba(129, 199, 132, 0.8); /* Lime con trasparenza */
                color: #fff;
                padding: 10px 20px;
                width: 100%;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 1.2em;
                text-align: center;
            }
            button {
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 1em;
                background-color: #4caf50; /* Verde */
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049; /* Verde scuro */
            }
            .chart {
                width: 100px; /* Larghezza del grafico */
                height: 100px; /* Altezza del grafico */
                border-radius: 50%; /* Forma rotonda */
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
                margin: 20px 0;
            }
            @media (max-width: 600px) {
                p {
                    font-size: 1em;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>CPU Virtuale</h1>
        </header>
    """)

import random as rd
import matplotlib.pyplot as plt
import io
import base64

def generate_chart(temperature):
    # Crea un grafico
    plt.figure(figsize=(5, 3))
    plt.bar(['CPU Temperature'], [temperature], color='red' if temperature > 70 else 'lime')
    plt.ylim(0, 100)
    plt.ylabel('Temperature (°C)')
    plt.title('CPU Temperature')
    
    # Salva il grafico in un buffer di memoria
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    
    # Converte l'immagine in base64
    return base64.b64encode(buf.read()).decode('utf-8')

def CPU():
    print("Content-type: text/html\r\n")
    
    print("""
    <html>
    <head>
        <meta charset='UTF-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Temperature and Humidity</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #e0f7fa; /* Blu chiaro */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            header {
                background: rgba(129, 199, 132, 0.8); /* Lime con trasparenza */
                color: #fff;
                padding: 10px 20px;
                width: 100%;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 1.2em;
                text-align: center;
            }
            button {
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 1em;
                background-color: #4caf50; /* Verde */
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049; /* Verde scuro */
            }
            .chart {
                margin: 20px 0;
            }
            @media (max-width: 600px) {
                p {
                    font-size: 1em;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>CPU Virtuale</h1>
        </header>
    """)

    # Genera una temperatura casuale per la CPU
    Temperatura_Cpu = rd.randint(30, 90)
    
    # Genera il grafico
    chart_data = generate_chart(Temperatura_Cpu)

    # Imposta il messaggio in base alla temperatura
    if Temperatura_Cpu > 70:
        message_color = "red"
        message = f"La temperatura ha superato i 70 gradi. Contattare l'amministratore o il tecnico."
    else:
        message_color = "green"
        message = f"Valore temperatura CPU: {Temperatura_Cpu}°C"

    print(f'<p style="color:{message_color};">{message}</p>')
    print(f'<div class="chart"><img src="data:image/png;base64,{chart_data}" alt="CPU Temperature Chart"></div>')

    print("""
        <button onclick="location.href='http://localhost:8010/';">Torna alla pagina Index</button>
        <button onclick="location.reload();">Ricarica</button>
    </body>
    </html>
    """)

CPU()
