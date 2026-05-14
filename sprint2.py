from datetime import datetime
# ------------------------------------------------------------
#função para validar o formato do horário
def validar_horario(horario):
    try:
        datetime.strptime(horario, "%H:%M")
        return True
    except ValueError:
        return False
# ------------------------------------------------------------
# listas para armazenar o histórico das configurações
historico_cursos = []
historico_materias = []
historico_horarios = []
historico_dias = []
# ------------------------------------------------------------
# inicio do programa
while True:
    inicio = input(
        "\nVocê ainda não configurou o Modo Aula na sua câmera.\n"
        "Deseja configurar agora? (responda apenas com sim ou não): "
    ).strip().lower()
    match inicio:
        case "sim" | "s":
            print("\nIniciando configuração do Modo Aula...")
            while True:
                print("\n" + "=" * 50)
                print("CONFIGURAÇÃO DE CURSO")
                print("=" * 50)
                curso = input("Digite seu curso: ").strip()
                # ------------------------------------------------------------
                # cadastro das matérias
                materias_lista = []
                print("\nDigite suas matérias.")
                print("Digite 'FIM' para encerrar.")
                while True:
                    materia = input("Matéria: ").strip()
                    if materia.upper() == "FIM":
                        if not materias_lista:
                            print("Adicione pelo menos uma matéria!")
                            continue
                        break
                    if materia and materia not in materias_lista:
                        materias_lista.append(materia)
                        print(f"{materia} adicionada!")
                    else:
                        print("Matéria inválida ou já adicionada.")
                # ------------------------------------------------------------
                # horário de início
                while True:
                    comeco_aula = input(
                        "\nHorário de início (HH:MM): "
                    ).strip()
                    if validar_horario(comeco_aula):
                        break
                    print("Horário inválido! Use HH:MM")
                # ------------------------------------------------------------
                # horário de término
                while True:
                    fim_aula = input(
                        "Horário de término (HH:MM): "
                    ).strip()
                    if validar_horario(fim_aula):
                        break
                    print("Horário inválido! Use HH:MM")
                # ------------------------------------------------------------
                # dias da aula
                dias_validos = [
                    "Segunda",
                    "Terça",
                    "Quarta",
                    "Quinta",
                    "Sexta",
                    "Sábado",
                    "Domingo",
                ]
                dias_aula = []
                print("\nEscolha os dias da aula.")
                print("Digite 'FIM' para finalizar.")
                while True:
                    print(f"\nDias disponíveis: {', '.join(dias_validos)}")
                    entrada = input("Dia: ").strip().capitalize()
                    if entrada.upper() == "FIM":
                        if not dias_aula:
                            print("Adicione pelo menos um dia!")
                            continue
                        break
                    if entrada in dias_validos:
                        if entrada not in dias_aula:
                            dias_aula.append(entrada)
                            print(f"{entrada} adicionado!")
                        else:
                            print("Esse dia já foi adicionado.")
                    else:
                        print("Digite um dia válido.")
                # ------------------------------------------------------------
                # resumo da configuração
                materias_juntas = ", ".join(materias_lista)
                dias_juntos = ", ".join(dias_aula)
                print("\n" + "=" * 50)
                print("RESUMO DA CONFIGURAÇÃO")
                print("=" * 50)

                print(f"Curso: {curso}")
                print(f"Matérias: {materias_juntas}")
                print(f"Horário: {comeco_aula} até {fim_aula}")
                print(f"Dias: {dias_juntos}")
                # ------------------------------------------------------------
                # confirmação final
                confirmacao = input(
                    "\nAs informações estão corretas? (Sim/Não): "
                ).strip().lower()
                if confirmacao in ["sim", "s"]:
                    historico_cursos.append(curso)
                    historico_materias.append(materias_juntas)
                    historico_horarios.append(
                        f"{comeco_aula} até {fim_aula}"
                    )
                    historico_dias.append(dias_juntos)
                    print("\nConfiguração salva com sucesso!")
                else:
                    print("\nReiniciando configuração...")
                    continue
                # ------------------------------------------------------------
                # configurar outro curso?
                mais = input(
                    "\nDeseja configurar outro curso? (Sim/Não): "
                ).strip().lower()
                if mais not in ["sim", "s"]:
                    break
            # ------------------------------------------------------------
            # resumo total das configurações
            print("\n" + "=" * 60)
            print("RESUMO TOTAL DAS CONFIGURAÇÕES")
            print("=" * 60)
            if not historico_cursos:
                print("Nenhum curso configurado.")
            else:
                for c, m, h, d in zip(
                    historico_cursos,
                    historico_materias,
                    historico_horarios,
                    historico_dias,
                ):
                    print(f"\nCURSO: {c}")
                    print(f"MATÉRIAS: {m}")
                    print(f"HORÁRIO: {h}")
                    print(f"DIAS: {d}")
            # ------------------------------------------------------------
            # testar o modo aula
            quer_testar = input(
                "\nDeseja testar o Modo Aula? (Sim/Não): "
            ).strip().lower()
            if quer_testar in ["sim", "s"]:
                while True:
                    print("\n" + "=" * 40)
                    print("MENU MODO AULA")
                    print("=" * 40)

                    print("1 - Câmera")
                    print("2 - Documento")
                    print("3 - Gravar Áudio")
                    print("4 - Sair")
                    escolha = input("\nEscolha uma opção: ").strip()
                    match escolha:
                        case "1":
                            print(
                                "\nVocê está no modo câmera otimizado para aula!"
                            )
                        case "2":
                            print(
                                "\nVocê está no modo documento otimizado para aula!"
                            )
                        case "3":
                            print(
                                "\nVocê está gravando o áudio da aula!"
                            )
                        case "4":
                            print("\nSaindo do Modo Aula...")
                            break
                        case _:
                            print("\nOpção inválida!")
            print(
                "\nSeu Modo Aula foi configurado com sucesso!"
            )
            break
        # ============================================================
        case "não" | "nao" | "n":
            print("\nObrigada por acessar o Modo Aula.")
            break
        case _:
            print(
                "\nOpção inválida. Por favor, responda com Sim ou Não."
            )
                                 