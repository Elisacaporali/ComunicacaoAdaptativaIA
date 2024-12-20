import random
import time
from datetime import datetime, timedelta

class AssistenteIA:
    def __init__(self):
        self.nome_usuario = ""
        self.respostas = {}
        self.tarefas = []
        self.perfil_neurodivergente = None
        self.tempo_foco = 0
        self.contatos_emergencia = {}
        self.medicacoes = []
        self.lembretes = []
        self.registros_medicacao = []
        self.medicacoes_comuns = {
            "TDAH": ["Metilfenidato", "Atomoxetina", "Lisdexanfetamina"],
            "TEA": ["Risperidona", "Aripiprazol", "Fluoxetina"],
            "Outros": ["Sertralina", "Escitalopram", "Quetiapina", "Lamotrigina", "Valproato de Sódio", "Bupropiona"]
        }
        self.respostas_emocionais = {
            "cansado": ("Entendo que você está cansado. Que tal tirar um momento para relaxar?", 
                        "Sugestão: Que tal fazer uma pausa de 10 minutos? Respire fundo e tome um copo d'água."),
            "triste": ("Sinto muito que você esteja triste. Lembre-se que seus sentimentos são válidos.", 
                       "Sugestão: Às vezes, expressar nossos sentimentos pode ajudar. Que tal escrever sobre o que está sentindo?"),
            "feliz": ("Fico muito feliz em saber que você está feliz! Seu sorriso ilumina o dia.", 
                      "Sugestão: Que tal compartilhar essa felicidade? Você poderia fazer algo legal para alguém."),
            "ansioso": ("A ansiedade pode ser desafiadora. Vamos tentar um exercício de respiração?", 
                        "Sugestão: Inspire profundamente por 4 segundos, segure por 4 e expire por 4. Repita 5 vezes."),
            "estressado": ("O estresse pode ser difícil. Vamos pensar em atividades relaxantes?", 
                           "Sugestão: Que tal ouvir uma música tranquila ou fazer um desenho?")
        }

    def iniciar_dia(self):
        print("Assistente: Bom dia! Vamos começar nosso dia juntos.")
        self.nome_usuario = input("Assistente: Qual é o seu nome? ")
        print(f"Assistente: Olá, {self.nome_usuario}! É um prazer conhecer você.")
        self.verificar_estado_inicial()
        self.definir_perfil_neurodivergente()
        self.configurar_contatos_emergencia()
        self.configurar_medicacoes()
        self.criar_lembretes_medicacao()

    def verificar_estado_inicial(self):
        estado = input("Assistente: Como você está se sentindo agora? ").lower()
        if estado in self.respostas_emocionais:
            resposta, sugestao = self.respostas_emocionais[estado]
            print(f"Assistente: {resposta}")
            print(f"Assistente: {sugestao}")
        else:
            print(f"Assistente: Entendo que você está se sentindo {estado}. Cada sentimento é único e importante.")
            print("Assistente: Lembre-se de que estou aqui para te apoiar no que precisar.")

    def definir_perfil_neurodivergente(self):
        print("Assistente: Para melhor atendê-lo, preciso saber um pouco mais sobre você.")
        print("1. TDAH")
        print("2. TEA")
        print("3. Outro")
        escolha = input("Por favor, escolha uma opção (1-3): ")
        if escolha == '1':
            self.perfil_neurodivergente = "TDAH"
            self.tempo_foco = 15  # 15 minutos de foco para TDAH
        elif escolha == '2':
            self.perfil_neurodivergente = "TEA"
            self.tempo_foco = 30  # 30 minutos de foco para TEA
        else:
            self.perfil_neurodivergente = "Outro"
            self.tempo_foco = 20  # 20 minutos de foco para outros perfis
            print("Assistente: Aqui está uma lista de medicações comuns para diversos transtornos neuropsiquiátricos:")
            for categoria, meds in self.medicacoes_comuns.items():
                print(f"{categoria}: {', '.join(meds)}")

    def configurar_contatos_emergencia(self):
        print("Assistente: Vamos configurar seus contatos de emergência.")
        familiar_nome = input("Por favor, digite o nome de um familiar: ")
        familiar_numero = input(f"Digite o número de telefone de {familiar_nome}: ")
        medico_nome = input("Agora, digite o nome do seu médico: ")
        medico_numero = input(f"Digite o número de telefone do Dr. {medico_nome}: ")
        self.contatos_emergencia['familiar'] = (familiar_nome, familiar_numero)
        self.contatos_emergencia['medico'] = (medico_nome, medico_numero)

    def configurar_medicacoes(self):
        print("Assistente: Vamos configurar suas medicações.")
        while True:
            medicacao = input("Assistente: Qual medicação você precisa tomar? (ou digite 'fim' para terminar) ")
            if medicacao.lower() == 'fim':
                break
            if medicacao.lower() == 'não sei' or medicacao.lower() == 'nao sei':
                print("Assistente: Entendo que você não tem certeza sobre suas medicações. Vamos pular esta parte por enquanto.")
                print("Assistente: Recomendo que você consulte seu médico para obter informações precisas sobre suas medicações.")
                break
            horario = input(f"Assistente: A que horas você precisa tomar {medicacao}? ")
            dosagem = input(f"Assistente: Qual a dosagem de {medicacao}? ")
            frequencia = input(f"Assistente: Com que frequência você toma {medicacao}? (ex: diariamente, 2x ao dia, semanalmente) ")
            self.medicacoes.append({
                "nome": medicacao,
                "horario": horario,
                "dosagem": dosagem,
                "frequencia": frequencia
            })
        if self.medicacoes:
            print("Assistente: Obrigado. Vou lembrá-lo de tomar suas medicações nos horários corretos.")
        else:
            print("Assistente: Não há problema se você não configurou medicações agora. Podemos fazer isso mais tarde se necessário.")

    def criar_lembretes_medicacao(self):
        for med in self.medicacoes:
            self.lembretes.append({
                "mensagem": f"Tomar {med['nome']} - {med['dosagem']}",
                "horario": med['horario']
            })
        if self.lembretes:
            print("Assistente: Lembretes de medicação configurados.")

    def fazer_pergunta(self, pergunta):
        resposta = input(f"Assistente: {pergunta} ")
        self.respostas[pergunta] = resposta
        return resposta

    def sugerir_atividade(self, atividade):
        print(f"Assistente: Que tal {atividade} agora?")
        resposta = input("Você (responda 'ok' quando terminar ou 'pular' para outra atividade): ")
        while resposta.lower() not in ['ok', 'pular']:
            resposta = input("Você (responda 'ok' quando terminar ou 'pular' para outra atividade): ")
        return resposta.lower() == 'ok'

    def verificar_estado(self):
        estado = self.fazer_pergunta("Como você está se sentindo agora?").lower()
        if estado in self.respostas_emocionais:
            resposta, sugestao = self.respostas_emocionais[estado]
            print(f"Assistente: {resposta}")
            print(f"Assistente: {sugestao}")
        else:
            print(f"Assistente: Entendo que você está se sentindo {estado}. Saiba que estou aqui para te apoiar no que precisar.")
        
        self.verificar_pulso()
        if self.perfil_neurodivergente == "TDAH":
            self.fazer_pergunta("Você está tendo dificuldade em se concentrar hoje?")
        elif self.perfil_neurodivergente == "TEA":
            self.fazer_pergunta("Houve alguma mudança na sua rotina que o deixou desconfortável?")

    def verificar_pulso(self):
        pulso = int(self.fazer_pergunta("Qual é sua leitura de pulso atual?"))
        if pulso < 60:
            print("Assistente: Sua frequência cardíaca está baixa. Recomendo que você descanse um pouco e beba água.")
        elif pulso > 100:
            print("Assistente: Sua frequência cardíaca está alta.")
            medicacao = self.fazer_pergunta("Você já tomou sua medicação hoje?")
            if medicacao.lower() == 'não':
                print("Assistente: Por favor, tome sua medicação conforme prescrito pelo médico.")
            aviso = self.fazer_pergunta("Gostaria que eu enviasse um aviso para seu familiar ou médico? (sim/não)")
            if aviso.lower() == 'sim':
                self.enviar_aviso("Frequência cardíaca alta detectada.")
        else:
            print("Assistente: Sua frequência cardíaca está normal. Ótimo!")

    def enviar_aviso(self, mensagem):
        print("Assistente: Enviando aviso...")
        for contato, info in self.contatos_emergencia.items():
            nome, numero = info
            print(f"Aviso enviado para {nome} ({numero}): {mensagem}")
        print("Assistente: Avisos enviados com sucesso.")

    def gerenciar_medicacoes(self):
        print("Assistente: Vamos revisar suas medicações.")
        
        if not self.medicacoes:
            print("Assistente: Parece que ainda não temos uma lista de suas medicações. Vamos criar uma agora.")
            self.configurar_medicacoes()
        
        if self.medicacoes:
            print("Assistente: Aqui está a lista de suas medicações:")
            for i, med in enumerate(self.medicacoes, 1):
                print(f"{i}. {med['nome']} - {med['dosagem']} às {med['horario']} ({med['frequencia']})")
        
            agora = datetime.now().strftime("%H:%M")
            print(f"Assistente: Agora são {agora}.")
        
            medicacoes_para_tomar = [med for med in self.medicacoes if med['horario'] <= agora]
            if medicacoes_para_tomar:
                print("Assistente: Você precisa tomar as seguintes medicações agora:")
                for med in medicacoes_para_tomar:
                    print(f"- {med['nome']} - {med['dosagem']}")
                confirmacao = self.fazer_pergunta("Você tomou essas medicações? (sim/não)")
                if confirmacao.lower() == 'sim':
                    print("Assistente: Ótimo! Lembre-se de tomar água.")
                    self.registrar_medicacao(medicacoes_para_tomar)
                else:
                    print("Assistente: Por favor, tome suas medicações agora. É importante para sua saúde.")
                    self.definir_lembrete("Tomar medicações", 15)  # Lembrete em 15 minutos
            else:
                print("Assistente: Você não tem medicações para tomar neste momento.")
        
            self.mostrar_proxima_medicacao()
        else:
            print("Assistente: Você ainda não configurou nenhuma medicação. Se precisar, podemos fazer isso agora.")

    def registrar_medicacao(self, medicacoes):
        for med in medicacoes:
            self.registros_medicacao.append({
                "nome": med['nome'],
                "dosagem": med['dosagem'],
                "horario": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
        print("Assistente: Registro de medicação atualizado.")

    def mostrar_proxima_medicacao(self):
        if self.medicacoes:
            proxima_medicacao = min(self.medicacoes, key=lambda x: x['horario'])
            print(f"Assistente: Sua próxima medicação é {proxima_medicacao['nome']} - {proxima_medicacao['dosagem']} às {proxima_medicacao['horario']}.")
            tempo_ate = self.calcular_tempo_ate(proxima_medicacao['horario'])
            print(f"Assistente: Faltam aproximadamente {tempo_ate} minutos para a próxima dose.")
            self.definir_lembrete(f"Tomar {proxima_medicacao['nome']}", tempo_ate)

    def definir_lembrete(self, mensagem, minutos):
        print(f"Assistente: Defini um lembrete para '{mensagem}' em {minutos} minutos.")
        self.lembretes.append({
            "mensagem": mensagem,
            "horario": (datetime.now() + timedelta(minutes=minutos)).strftime("%H:%M")
        })

    def verificar_lembretes(self):
        agora = datetime.now().strftime("%H:%M")
        lembretes_ativos = [l for l in self.lembretes if l['horario'] <= agora]
        for lembrete in lembretes_ativos:
            print(f"LEMBRETE: {lembrete['mensagem']}")
        self.lembretes = [l for l in self.lembretes if l['horario'] > agora]

    def gerar_relatorio_medicacao(self):
        print("Assistente: Aqui está o relatório de medicações tomadas:")
        if self.registros_medicacao:
            for registro in self.registros_medicacao:
                print(f"- {registro['nome']} ({registro['dosagem']}) tomado em {registro['horario']}")
        else:
            print("Assistente: Ainda não há registros de medicações tomadas.")

    def cuidados_pessoais(self):
        self.sugerir_atividade("tomar um banho")
        self.sugerir_atividade("escovar os dentes")
        self.fazer_pergunta("O que você planeja comer na próxima refeição?")
        if self.perfil_neurodivergente in ["TDAH", "TEA"]:
            self.sugerir_atividade("fazer um exercício de respiração por 2 minutos")

    def organizar_tarefas(self):
        nova_tarefa = self.fazer_pergunta("Qual tarefa você precisa realizar?")
        self.tarefas.append(nova_tarefa)
        
        print("Suas tarefas atuais são:")
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f"{i}. {tarefa}")
        
        if self.perfil_neurodivergente == "TDAH":
            print("Assistente: Lembre-se de dividir suas tarefas em etapas menores para facilitar o foco.")
            self.sugerir_divisao_tarefas(nova_tarefa)
        elif self.perfil_neurodivergente == "TEA":
            print("Assistente: Vamos criar uma rotina visual para suas tarefas?")
            self.criar_rotina_visual(nova_tarefa)

    def sugerir_divisao_tarefas(self, tarefa):
        print(f"Assistente: Vamos dividir a tarefa '{tarefa}' em etapas menores.")
        etapas = []
        while True:
            etapa = self.fazer_pergunta("Qual seria uma etapa desta tarefa? (ou digite 'fim' para terminar)")
            if etapa.lower() == 'fim':
                break
            etapas.append(etapa)
        print("Assistente: Ótimo! Aqui estão as etapas da sua tarefa:")
        for i, etapa in enumerate(etapas, 1):
            print(f"{i}. {etapa}")

    def criar_rotina_visual(self, tarefa):
        print(f"Assistente: Vamos criar uma rotina visual para a tarefa '{tarefa}'.")
        print("Assistente: Imagine cada passo da tarefa como um ícone ou imagem.")
        passos = []
        while True:
            passo = self.fazer_pergunta("Descreva um passo da tarefa (ou digite 'fim' para terminar)")
            if passo.lower() == 'fim':
                break
            icone = self.fazer_pergunta(f"Que ícone ou imagem representaria o passo '{passo}'?")
            passos.append((passo, icone))
        print("Assistente: Aqui está sua rotina visual:")
        for i, (passo, icone) in enumerate(passos, 1):
            print(f"{i}. [{icone}] {passo}")

    def iniciar_sessao_foco(self):
        print(f"Assistente: Vamos iniciar uma sessão de foco de {self.tempo_foco} minutos.")
        print("Concentre-se em uma tarefa específica durante esse tempo.")
        for i in range(self.tempo_foco, 0, -1):
            print(f"Tempo restante: {i} minutos")
            time.sleep(1)  # Espera 1 segundo (simulando 1 minuto para a demonstração)
        print("Assistente: Sessão de foco concluída! Ótimo trabalho!")

    def finalizar_dia(self):
        print("Assistente: Vamos organizar o final do seu dia.")
        self.sugerir_atividade("tomar um banho relaxante")
        self.sugerir_atividade("molhar as plantas")
        self.sugerir_atividade("alimentar seu animal de estimação")
        self.fazer_pergunta("O que você planeja jantar?")
        self.sugerir_atividade("escovar os dentes")
        estado = self.fazer_pergunta("Como você se sente sobre o dia de hoje?").lower()
        if estado in self.respostas_emocionais:
            resposta, sugestao = self.respostas_emocionais[estado]
            print(f"Assistente: {resposta}")
            print(f"Assistente: {sugestao}")
        else:
            print(f"Assistente: Obrigado por compartilhar como se sente. Cada dia é uma nova oportunidade. Descanse bem e amanhã será um novo começo!")

    def calcular_tempo_ate(self, horario_alvo):
        agora = datetime.now()
        alvo = datetime.strptime(horario_alvo, "%H:%M").replace(year=agora.year, month=agora.month, day=agora.day)
        if alvo <= agora:
            alvo += timedelta(days=1)
        diferenca = alvo - agora
        return int(diferenca.total_seconds() / 60)

    def interagir(self):
        self.verificar_lembretes()
        print("\nAssistente: O que você gostaria de fazer agora?")
        print("1. Verificar estado emocional e saúde")
        print("2. Gerenciar medicações")
        print("3. Cuidados pessoais")
        print("4. Organizar tarefas")
        print("5. Iniciar sessão de foco")
        print("6. Ver relatório de medicações")
        print("7. Finalizar o dia")
        print("8. Sair")

        escolha = input("Escolha uma opção (1-8): ")

        if escolha == '1':
            self.verificar_estado()
        elif escolha == '2':
            self.gerenciar_medicacoes()
        elif escolha == '3':
            self.cuidados_pessoais()
        elif escolha == '4':
            self.organizar_tarefas()
        elif escolha == '5':
            self.iniciar_sessao_foco()
        elif escolha == '6':
            self.gerar_relatorio_medicacao()
        elif escolha == '7':
            self.finalizar_dia()
        elif escolha == '8':
            print(f"Assistente: Até logo, {self.nome_usuario}! Tenha um ótimo dia.")
            return False
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 8.")
        return True

def demonstracao_3_minutos():
    inicio = time.time()
    duracao = 180  # 3 minutos em segundos

    assistente = AssistenteIA()
    assistente.iniciar_dia()

    print("Iniciando demonstração de 3 minutos...")

    while time.time() - inicio < duracao:
        if not assistente.interagir():
            break
        time_restante = duracao - (time.time() - inicio)
        print(f"Tempo restante: {int(time_restante)} segundos")

    print("Demonstração concluída!")

if __name__ == "__main__":
    demonstracao_3_minutos()
