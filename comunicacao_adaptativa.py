import random
class ComunicacaoAdaptativa:
    def __init__(self):
        self.contextos = ["escola", "faculdade", "casa", "trabalho", "lazer", "relacionamentos", "saúde", "finanças", "comunidade"]
        self.emocoes = ["feliz","irritado","aliviado","desapontado","inseguro","entediado", "ansioso", "frustrado", "calmo", "empolgado", "triste", "confuso", "confiante", "estressado", "esperançoso"]
        self.emocoes_adicionais = ["irritado", "aliviado", "desapontado", "inseguro", "entediado"]
self.emocoes_complexas = ["nostálgico", "culpado"]
self.emocoes_contextos_sociais = ["rejeitado", "apoiado"]
self.reacoes_fisicas = ["tenso", "entrando em crise de pânico"]
self.emocoes_relacionadas_ao_aprendizado = ["curioso"]
self.sentimentos_sobre_o_futuro = ["preocupado"]
        self.usuario_atual = None


    def interpretar_contexto(self, mensagem):
         palavras_chave = {
        "escola": ["aula", "professor", "lição", "estudar"],
        "casa": ["família", "lar", "doméstico"],
        "trabalho": ["emprego", "escritório", "carreira", "profissional"],
        "lazer": ["hobby", "diversão", "passatempo", "relaxar"],
        "relacionamentos": ["amigos", "namoro", "família", "social"],
        "saúde": ["bem-estar", "exercício", "médico", "doença"],
        "finanças": ["dinheiro", "economia", "gastos", "investimento"],
        "comunidade": ["bairro", "vizinhos", "voluntariado", "local"],"saúde mental": ["ansiedade", "depressão", "terapia"],
        "educação": ["curso", "ensino", "aprendizado"],
        "tecnologia": ["computador", "internet", "software"],
        "viagens": ["turismo", "viagem", "destino"],
        "cultura": ["arte", "música", "literatura"]
         }
    
        for contexto, palavras in palavras_chave.items():
        if any(palavra in mensagem.lower() for palavra in palavras):
            return contexto
    return random.choice(self.contextos)

    def analisar_emocao(self, mensagem):
        todas_emocoes = {
        "feliz": ["alegre", "contente", "satisfeito"],
        "ansioso": ["nervoso", "preocupado", "tenso"],
        "frustrado": ["irritado", "chateado", "desapontado"],
        "calmo": ["tranquilo", "sereno", "relaxado"],
        "empolgado": ["animado", "entusiasmado", "motivado"],
        "triste": ["melancólico", "abatido", "desanimado"],
        "confuso": ["perdido", "incerto", "em dúvida"],
        "confiante": ["seguro", "determinado", "otimista"],
        "estressado": ["sobrecarregado", "pressionado", "tenso"],
        "esperançoso": ["otimista", "positivo", "confiante"]
    } 
        for emocao, palavras in todas_emocoes.items():
        if any(palavra in mensagem.lower() for palavra in palavras):
            return emocao
    return random.choice(self.emocoes)


    def gerar_resposta(self, mensagem):
        contexto = self.interpretar_contexto(mensagem)
        emocao = self.analisar_emocao(mensagem)
        
        def gerar_resposta(self, mensagem):
    contexto = self.interpretar_contexto(mensagem)
    emocao = self.analisar_emocao(mensagem)
    
    respostas = {
        ("escola", "ansioso"): "Entendo que você está ansioso na escola. Que tal fazermos um exercício de respiração juntos?",
        ("casa", "feliz"): "Que bom que você está feliz em casa! Quer compartilhar o que está te deixando assim?",
        ("trabalho", "frustrado"): "Percebo que você está frustrado no trabalho. Vamos quebrar suas tarefas em partes menores?",
        ("lazer", "empolgado"): "É ótimo ver você empolgado com seu tempo de lazer! Que atividades você tem planejado?",
        ("relacionamentos", "confuso"): "Relacionamentos podem ser complicados. Quer conversar sobre o que está te deixando confuso?",
        ("saúde", "preocupado"): "Sua saúde é importante. Vamos listar suas preocupações e pensar em passos práticos para cada uma?",
        ("finanças", "estressado"): "Finanças podem ser estressantes. Que tal criarmos um plano de orçamento juntos?",
        ("comunidade", "esperançoso"): "É inspirador ver você esperançoso sobre sua comunidade. Tem algum projeto comunitário em mente?"
    }
    
   chave = (contexto, emocao)
    if chave in respostas:
        return respostas[chave]
    else:
        return f"Estou aqui para te apoiar no contexto de {contexto}, percebendo que você está se sentindo {emocao}. Como posso ajudar?"
        if contexto == "escola" and emocao == "ansioso":
            return "Entendo que você está ansioso na escola. Que tal fazermos um exercício de respiração juntos?"
        elif contexto == "casa" and emocao == "feliz":
            return "Que bom que você está feliz em casa! Quer compartilhar o que está te deixando assim?"
        elif contexto == "trabalho" and emocao == "frustrado":
            return "Percebo que você está frustrado no trabalho. Vamos quebrar suas tarefas em partes menores?"
        else:
            return f"Estou aqui para te apoiar no contexto de {contexto}, percebendo que você está se sentindo {emocao}."

    def interagir(self):
        print("Bem-vindo à Plataforma de Comunicação Adaptativa!")
        self.usuario_atual = input("Como você gostaria de ser chamado? ")
        
        while True:
            mensagem = input(f"\n{self.usuario_atual}, como posso te ajudar hoje? (ou digite 'sair' para encerrar) ")
            if mensagem.lower() == 'sair':
                print("Obrigado por usar nossa plataforma. Até a próxima!")
                break
            
            resposta = self.gerar_resposta(mensagem)
            print(f"\nAssistente: {resposta}")
            
            # Feedback em tempo real
            feedback = input("Esta resposta foi útil? (sim/não) ")
            if feedback.lower() == 'não':
                print("Entendo. Vou me esforçar para melhorar minhas respostas no futuro.")

if __name__ == "__main__":
    plataforma = ComunicacaoAdaptativa()
    plataforma.interagir()
