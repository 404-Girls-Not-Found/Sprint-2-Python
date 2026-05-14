historico_cursos = []
historico_materias = []
historico_horarios = []
historico_dias = []

while True:
    inicio = input(
        "\nVocê ainda não configurou o Modo Aula na sua câmera.\n"
        "Deseja configurar agora? (responda apenas com sim ou não): "
    )
    match inicio:
        case "sim" | "s" | "SIM" | "Sim" | "S":
            print("\nIniciando configuração do Modo Aula...")

            while True:
                print("===============================")
                print("CONFIGURAÇÃO DE CURSO")
                print("===============================")
                curso = input("Digite seu curso: ")

                nomes_materias = []
                horarios_materias = []
                dias_materias = []

                while True:
                    materia = input("\nMatéria: ")

                    if not materia or materia in nomes_materias:
                        print("Matéria inválida ou já adicionada.")
                        continue

                    print(f"{materia} adicionada!")

                    # Horário de início e Horário de término
                    comeco_aula = input(f"Horário de início de {materia} (HH:MM): ")
                    fim_aula = input(f"Horário de término de {materia} (HH:MM): ")

                    # Dia da semana
                    dias_validos = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado","Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
                    while True:
                        dia = input(f"Em qual dia da semana você tem {materia}? ")
                        if dia in dias_validos:
                            break
                        print("Dia inválido! Use: Segunda, Terça, Quarta, Quinta, Sexta, Sábado ou Domingo")

                    nomes_materias.append(materia)
                    horarios_materias.append(f"{comeco_aula} até {fim_aula}")
                    dias_materias.append(dia)

                    mais_materias = input("\nDeseja adicionar mais matérias? (Sim/Não): ")
                    if mais_materias not in ["sim", "s", "Sim"]:
                        break

                # Resumo do curso
                print("===============================")
                print("RESUMO DA CONFIGURAÇÃO")
                print("===============================")
                print(f"Curso: {curso}")
                for i in range(len(nomes_materias)):
                    print(f"\n  Matéria: {nomes_materias[i]}")
                    print(f"  Horário: {horarios_materias[i]}")
                    print(f"  Dia:     {dias_materias[i]}")

                confirmacao = input("\nAs informações estão corretas? (Sim/Não): ")
                if confirmacao in ["sim", "s", "Sim"]:
                    historico_cursos.append(curso)
                    historico_materias.append(nomes_materias)
                    historico_horarios.append(horarios_materias)
                    historico_dias.append(dias_materias)
                    print("\nConfiguração salva com sucesso!")
                else:
                    print("\nReiniciando configuração...")
                    continue

                mais_cursos = input("\nDeseja configurar outro curso? (Sim/Não): ")
                if mais_cursos not in ["sim", "s", "Sim"]:
                    break

            # Resumo total
            print("===============================")
            print("RESUMO TOTAL DAS CONFIGURAÇÕES")
            print("===============================")
            if not historico_cursos:
                print("Nenhum curso configurado.")
            else:
                for i in range(len(historico_cursos)):
                    print(f"\nCURSO: {historico_cursos[i]}")
                    for j in range(len(historico_materias[i])):
                        print(f"\n  Matéria: {historico_materias[i][j]}")
                        print(f"  Horário: {historico_horarios[i][j]}")
                        print(f"  Dia:     {historico_dias[i][j]}")

            quer_testar = input("\nDeseja testar o Modo Aula? (Sim/Não): ")
            if quer_testar in ["sim", "s", "Sim"]:
                while True:
                    print("==============================")
                    print("MENU MODO AULA")
                    print("==============================")
                    print("1 - Câmera")
                    print("2 - Documento")
                    print("3 - Gravar Áudio")
                    print("4 - Sair")
                    escolha = input("\nEscolha uma opção: ")
                    match escolha:
                        case "1":
                            print("\nVocê está no modo câmera otimizado para aula!")
                        case "2":
                            print("\nVocê está no modo documento otimizado para aula!")
                        case "3":
                            print("\nVocê está gravando o áudio da aula!")
                        case "4":
                            print("\nSaindo do Modo Aula...")
                            break
                        case _:
                            print("\nOpção inválida!")

            print("\nSeu Modo Aula foi configurado com sucesso!")
            break

        case "não" | "nao" | "n":
            print("\nEstamos esperando sua configuração quando desejar.")
            break
        case _:
            print("\nOpção inválida. Por favor, responda com Sim ou Não.")