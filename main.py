import os

os.system("cls")

# Listas do sistema
bueiros = []
limpeza_pendente = []
historico_leituras = []

print(f'''
================================
         FLUXO SEGURO
   Monitoramento de Bueiros
================================
O sistema permite acompanhar o nível de água dos bueiros
durante e depois das chuvas, além de identificar a
necessidade de limpeza para a unidade responsável.
''')

opcao_menu = ""

while opcao_menu != "0":

    print("\n--------- MENU PRINCIPAL ---------")
    print("1 - Cadastrar bueiro")
    print("2 - Registrar nível de água")
    print("3 - Consultar histórico de leituras")
    print("0 - Encerrar o sistema")

    opcao_menu = input("\nO que deseja fazer? ")

    match opcao_menu:

        # CADASTRAR BUEIRO
        case "1":
            print("\n--------- CADASTRO DE BUEIRO ---------")
            print("Cadastre a localização do bueiro que deseja monitorar.")

            localizacao_bueiro = input("Digite o nome da rua ou ponto de referência: ").strip()

            if localizacao_bueiro == "":
                print("Informe uma localização válida.")

            else:
                bueiro_ja_cadastrado = False

                for bueiro in bueiros:
                    if bueiro.lower() == localizacao_bueiro.lower():
                        bueiro_ja_cadastrado = True

                if bueiro_ja_cadastrado:
                    print("Esse bueiro já está cadastrado.")

                else:
                    bueiros = bueiros + [localizacao_bueiro]
                    limpeza_pendente = limpeza_pendente + [False]
                    print("\nBueiro cadastrado com sucesso!")

        # REGISTRAR LEITURA
        case "2":
            if bueiros == []:
                print("\nNenhum bueiro cadastrado.")
                print("Utilize a opção 1 para cadastrar um bueiro primeiro.")

            else:
                print("\n--------- REGISTRO DE LEITURA ---------")
                print("Selecione o bueiro que deseja monitorar:")

                numero_bueiro = 1

                for bueiro in bueiros:
                    print(numero_bueiro, "-", bueiro)
                    numero_bueiro = numero_bueiro + 1

                posicao_bueiro = -1

                while posicao_bueiro == -1:
                    escolha_bueiro = input("\nDigite o número correspondente ao bueiro desejado: ")

                    numero_bueiro = 1

                    for bueiro in bueiros:
                        if escolha_bueiro == str(numero_bueiro):
                            posicao_bueiro = numero_bueiro - 1

                        numero_bueiro = numero_bueiro + 1

                    if posicao_bueiro == -1:
                        print("Número inválido. Digite o número de um dos bueiros apresentados na lista acima.")

                # ESCOLHER O PERÍODO DE MONITORAMENTO
                print("\n--------- PERÍODO DE MONITORAMENTO ---------")
                print("Escolha em qual período deseja registrar a leitura:")
                print("1 - DURANTE A CHUVA")
                print("    Acompanhar o nível de água para identificar")
                print("    riscos de alagamento e situações de perigo.")
                print("2 - APÓS A CHUVA")
                print("    Verificar se o bueiro precisa de limpeza")
                print("    devido ao acúmulo de água.")

                modo_monitoramento = input("\nDigite 1 ou 2: ")

                while modo_monitoramento != "1" and modo_monitoramento != "2":
                    modo_monitoramento = input(
                        "Opção inválida. Digite 1 para durante a chuva ou 2 para após a chuva: "
                    )

                # INFORMAR O NÍVEL DE ÁGUA
                print("\n--------- NÍVEL DE ÁGUA ---------")
                print("Informe a porcentagem de ocupação do bueiro.")
                print("Exemplo: se a água ocupa metade do espaço, digite 50.")
                print("Digite um número inteiro entre 0 e 100.")

                leitura_valida = False

                while not leitura_valida:
                    nivel_digitado = input("Nível de água: ")
                    numero_valido = True

                    if nivel_digitado == "":
                        numero_valido = False

                    else:
                        for caractere in nivel_digitado:
                            if caractere not in "0123456789":
                                numero_valido = False

                    if numero_valido:
                        nivel_agua = int(nivel_digitado)

                        if nivel_agua >= 0 and nivel_agua <= 100:
                            leitura_valida = True

                        else:
                            print("Valor inválido. Digite um número inteiro entre 0 e 100.")

                    else:
                        print("Valor inválido. Digite apenas números inteiros entre 0 e 100.")

                # ANÁLISE DURANTE A CHUVA
                if modo_monitoramento == "1":
                    periodo_leitura = "Durante a chuva"

                    # Até 80%, o pedido mantém o estado da leitura anterior
                    if nivel_agua > 80:
                        limpeza_pendente[posicao_bueiro] = True

                    if nivel_agua >= 90:
                        situacao_bueiro = "EMERGÊNCIA"

                    elif nivel_agua >= 60:
                        situacao_bueiro = "PERIGO"

                    elif nivel_agua >= 40:
                        situacao_bueiro = "ATENÇÃO"

                    else:
                        situacao_bueiro = "NORMAL"

                # ANÁLISE APÓS A CHUVA
                else:
                    periodo_leitura = "Após a chuva"

                    # Entre 20% e 24%, o pedido mantém o estado anterior
                    if nivel_agua >= 25:
                        limpeza_pendente[posicao_bueiro] = True

                    elif nivel_agua < 20:
                        limpeza_pendente[posicao_bueiro] = False

                    if limpeza_pendente[posicao_bueiro]:
                        situacao_bueiro = "LIMPEZA SOLICITADA"

                    else:
                        situacao_bueiro = "SEM PEDIDO DE LIMPEZA"

                # SALVAR E MOSTRAR RESULTADO
                registro_leitura = (
                    bueiros[posicao_bueiro] + " | " + periodo_leitura
                    + " | " + nivel_digitado + "% | " + situacao_bueiro
                )

                historico_leituras = historico_leituras + [registro_leitura]

                print("\n--------- RESULTADO DA LEITURA ---------")
                print("Localização:", bueiros[posicao_bueiro])
                print("Período:", periodo_leitura)
                print("Nível de água:", nivel_digitado + "%")
                print("Situação:", situacao_bueiro)

                if modo_monitoramento == "1" and nivel_agua > 80:
                    print("Pedido de limpeza registrado para este bueiro.")

                if modo_monitoramento == "2" and limpeza_pendente[posicao_bueiro]:
                    print("O pedido continua pendente até uma leitura após a chuva indicar menos de 20%.")

        # CONSULTAR O HISTÓRICO
        case "3":
            if historico_leituras == []:
                print("\nAinda não existem leituras registradas.")
                print("Registre uma leitura na opção 2 para consultar o histórico.")

            else:
                print("\n--------- HISTÓRICO DE LEITURAS ---------")
                print("Confira todas as leituras registradas:")

                for registro_leitura in historico_leituras:
                    print(registro_leitura)

        # ENCERRAR SISTEMA
        case "0":
            print("\nSistema encerrado.")
            print("Obrigado por usar o Fluxo Seguro!")

        case _:
            print("\nOpção inválida. Escolha uma das opções do menu.")