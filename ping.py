import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ping3 import ping
import datetime
from dotenv import load_dotenv
import os
import pyautogui as py
import time

usernamePF = 
passwordPF = 

usenameUNIFI = 
passwordUNIFI = 

def abrir_rede():
    py.press('win')

    py.write('chrome')

    time.sleep(2)
    py.press('enter')

    time.sleep(3)
    py.write('')

    py.press('enter')

    time.sleep(2)

    ir_para_site()

    time.sleep(2)

    py.write(usernamePF)
    time.sleep(2)

    py.press('tab')

    py.write(passwordPF)
    time.sleep(2)

    py.press('enter')
    
    time.sleep(2)
    
    abrir_unifi()

    time.sleep(2)

def ir_para_site():
    time.sleep(2)
    py.click(703, 625)
    
    time.sleep(2)
    py.click(722, 781)


def abrir_unifi():
    time.sleep(2)
    py.hotkey('ctrl', 't')

    time.sleep(1)

    py.write('')

    time.sleep(2)
    
    py.press('enter')

    time.sleep(2)

    py.write(usenameUNIFI)

    time.sleep(2)
    py.press('tab')
    py.write(passwordUNIFI)

    time.sleep(2)
    py.press('enter')

smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
smtp_user = ""
smtp_pass = ""
smtp_user2 = ""
hosts = ['', '', '']

def perform_ping(hosts):
    results = []
    for host in hosts:
        try:
            print(f"Pingando {host}...")  
            response = ping(host, timeout=10)
            if response is None:
                results.append(f"{host} está fora do ar, religa-los")
            else:
                results.append(f"{host} respondeu em {response*1000:.2f} ms. Todos os servidores estão ativos e funcionais.")
        except Exception as e:
            results.append(f"{host} erro ao pingar: {e}")
    return "\n".join(results)

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d")


print("Iniciando o teste de ping...")
ping_results = perform_ping(hosts)
print("Teste de ping concluído.")

msg = MIMEMultipart()
msg['From'] = smtp_user
msg['To'] = f"{smtp_user}, {smtp_user2}"
msg['Subject'] = f'Relatório de Teste de Ping - {date_str}'

body = f"Relatório de Ping:\n\n{ping_results}"
msg.attach(MIMEText(body, 'plain'))

try:
    print("Iniciando envio de e-mail...")
    with smtp.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
    print('E-mail enviado com sucesso.')
except Exception as e:
    print(f'Falha ao enviar e-mail: {e}')

abrir_rede()