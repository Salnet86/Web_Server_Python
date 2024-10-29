#!/usr/bin/python3
#dos2unix /home/utente/Scrivania/brezza/cgi-bin/temp.py
'''
import datetime
import matplotlib.pyplot as plt
import base64
import psutil
import io
import time

def get_cpu_temperature():
    try:
        temp = psutil.sensors_temperatures()
        return temp['coretemp'][0].current if 'coretemp' in temp else None
    except Exception:
        return None

def TemperatureCpu():
    cpu_data = []
    for _ in range(10):
        now = datetime.datetime.now()
        ts = datetime.datetime.timestamp(now)
        temp = get_cpu_temperature()
        if temp is not None:
            cpu_data.append((ts, temp))
        time.sleep(0.5)  # Intervallo di raccolta dati
    return cpu_data

def get_disk_usage():
    usage = psutil.disk_usage('/')
    return usage.total, usage.used, usage.free

def create_plot(data, title, xlabel, ylabel):
    buffer = io.BytesIO()
    plt.figure(figsize=(12, 6))
    plt.plot([x[0] for x in data], [x[1] for x in data], marker='o', label=title, color='blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

def create_pie_chart(data, labels, title):
    buffer = io.BytesIO()
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
    plt.title(title, fontsize=16)
    plt.axis('equal')
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

def display_system_info():
    print("Content-type: text/html; charset=utf-8\r\n")
    print("<html><head><title>Informazioni di Sistema</title></head><body>")
    print("<h1>Monitoraggio della Temperatura CPU e Utilizzo Disco</h1>")

    # Grafico temperatura CPU
    cpu_data = TemperatureCpu()
    img_base64_real_temp = create_plot(cpu_data, 'Temperatura CPU (Reale)', 'Tempo', 'Temperatura (°C)')
    print("<h2>Grafico della Temperatura CPU (Reale)</h2>")
    print(f'<img src="data:image/png;base64,{img_base64_real_temp}">')

    # Informazioni e grafico dell'utilizzo disco
    disk_total, disk_used, disk_free = get_disk_usage()
    img_base64_disk_pie = create_pie_chart([disk_used, disk_free], ['Usato', 'Libero'], 'Utilizzo Disco')

    print("<h2>Utilizzo Disco</h2>")
    print(f'<img src="data:image/png;base64,{img_base64_disk_pie}">')
    print("""
        <table border="1" cellpadding="10" cellspacing="0">
            <tr>
                <th>Spazio Totale (GB)</th>
                <th>Spazio Usato (GB)</th>
                <th>Spazio Libero (GB)</th>
            </tr>
            <tr>
                <td>{:.2f}</td>
                <td>{:.2f}</td>
                <td>{:.2f}</td>
            </tr>
        </table>
    """.format(disk_total / (1024 ** 3), disk_used / (1024 ** 3), disk_free / (1024 ** 3)))

    print("</body></html>")

if __name__ == "__main__":
    display_system_info()



'''

import datetime
import random
import matplotlib.pyplot as plt
import base64
import psutil
import io
import time

def get_cpu_temperature():
    try:
        temp = psutil.sensors_temperatures()
        return temp['coretemp'][0].current if 'coretemp' in temp else None
    except Exception:
        return None

def TemperatureCpu():
    cpu_data = []
    for _ in range(10):
        now = datetime.datetime.now()
        ts = datetime.datetime.timestamp(now)
        temp = get_cpu_temperature()
        if temp is not None:
            cpu_data.append((ts, temp))
        time.sleep(0.5)
    return cpu_data

def get_disk_usage():
    usage = psutil.disk_usage('/')
    return usage.total, usage.used, usage.free

def TemperatureUmidita():
    data = []  
    for _ in range(10):  
        now = datetime.datetime.now()
        ts = datetime.datetime.timestamp(now)
        temperatura = random.randint(20, 100)
        umidita = random.randint(20, 100)
        data.append((ts, temperatura, umidita))  
        time.sleep(0.05)
    return data  

def create_plot(data, title, xlabel, ylabel):
    buffer = io.BytesIO()
    plt.figure(figsize=(12, 6))
    plt.plot([x[0] for x in data], [x[1] for x in data], marker='o', label=title, color='blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

def create_pie_chart(data, labels, title):
    buffer = io.BytesIO()
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
    plt.title(title, fontsize=16)
    plt.axis('equal')
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

def display_system_info():
    print("Content-type: text/html; charset=utf-8\r\n")
    print("<html><head><title>Informazioni di Sistema</title>")
    print("""
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: lime;  /* Colore di sfondo lime */
            color: #333;
        }
        h1, h2 {
            text-align: center;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: auto;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        .card {
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            margin: 10px;
            padding: 20px;
            flex: 1 1 300px;
            min-width: 300px;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: center;
        }
        img {
            display: block;
            margin: auto;
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }
    </style>
    """)
    print("</head><body>")
    print("<h1>Monitoraggio della Temperatura CPU e Utilizzo Disco</h1>")

    # Grafico temperatura CPU
    cpu_data = TemperatureCpu()
    img_base64_real_temp = create_plot(cpu_data, 'Temperatura CPU (Reale)', 'Tempo', 'Temperatura (°C)')
    print("<h2>Grafico della Temperatura CPU (Reale)</h2>")
    print(f'<img src="data:image/png;base64,{img_base64_real_temp}">')

    # Informazioni e grafico dell'utilizzo disco
    disk_total, disk_used, disk_free = get_disk_usage()
    img_base64_disk_pie = create_pie_chart([disk_used, disk_free], ['Usato', 'Libero'], 'Utilizzo Disco')

    print("<h2>Utilizzo Disco</h2>")
    print(f'<img src="data:image/png;base64,{img_base64_disk_pie}">')
    print("""
        <table border="1" cellpadding="10" cellspacing="0">
            <tr>
                <th>Spazio Totale (GB)</th>
                <th>Spazio Usato (GB)</th>
                <th>Spazio Libero (GB)</th>
            </tr>
            <tr>
                <td>{:.2f}</td>
                <td>{:.2f}</td>
                <td>{:.2f}</td>
            </tr>
        </table>
    """.format(disk_total / (1024 ** 3), disk_used / (1024 ** 3), disk_free / (1024 ** 3)))

    # Sezione Valori Random
    print("<h1>Valori Random</h1>")
    print('<div id="random-data-section">')
    random_data = TemperatureUmidita()
    temperatures = [temp for _, temp, _ in random_data]

    # Grafico e Tabella per i Valori Random di Temperatura
    img_base64_random_temp = create_plot([(i, temp) for i, temp in enumerate(temperatures)], 
                                         'Temperatura (Dati Random)', 'Tempo', 'Temperatura (°C)')
    print("<h2>Grafico Temperatura (Valori Random)</h2>")
    print(f'<img src="data:image/png;base64,{img_base64_random_temp}">')

    # Tabella per Valori Random
    print("<h2>Tabella dei Valori Random</h2>")
    print("<table border='1' cellpadding='10' cellspacing='0'>")
    print("<tr><th>Epoca</th><th>Temperatura (°C)</th><th>Umidità (%)</th></tr>")
    for timestamp, temp, hum in random_data:
        print(f"<tr><td>{timestamp}</td><td>{temp}</td><td>{hum}</td></tr>")
    print("</table>")
    print('</div>')

    print("</body></html>")

if __name__ == "__main__":
    display_system_info()
