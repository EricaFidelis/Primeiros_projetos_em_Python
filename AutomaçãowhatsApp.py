import pywhatkit as kit
import pyautogui
import time

# 1. Sua lista de contatos (Nome e Número)
# Importante: O número deve ter +55, DDD e ser apenas números.
clientes = [
    {"nome": "João", "numero": "+551194594999"},
    {"nome": "Mariana", "numero": "+55119344546"},
    {"nome": "Lívia", "numero": "+5511958565656"}
]

print(f" iniciando...")

for cliente in clientes:
    nome_cliente = cliente["nome"]
    telefone = cliente["numero"]

    # 2. Sua mensagem personalizada
    mensagem = f"""Sr(a) {nome_cliente}, 

Me chamo Erica Fidelis e estou testando um novo projeto!.

Estou entrando em contato para verificar se necessitam de serviços de manutenção preventiva, reformas ou peças. E também para marcarmos uma visita na sua empresa, para conversarmos sobre projetos futuros e demais demandas para prensas. 

Aguardo retorno!"""

    print(f"📧 Preparando mensagem para: {nome_cliente} ({telefone})")

    # 3. O processo de envio
    # wait_time=25 para garantir que o WhatsApp Web carregue a conversa
    kit.sendwhatmsg_instantly(telefone, mensagem, wait_time=25, tab_close=False)
    
    # Espera o cursor focar e aperta o "Enter" mágico
    time.sleep(5)
    pyautogui.press('enter')
    
    # Fecha a aba para não virar bagunça (Ctrl + W)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    
    print(f"✅ Mensagem enviada para {nome_cliente}!")
    
    # INTERVALO DE SEGURANÇA (Para o WhatsApp não achar que você é um spammer)
    print("⏳ Aguardando 15 segundos para o próximo envio...")
    time.sleep(15) 

print("\n🎯 Missão cumprida,todos os clientes foram avisados.")