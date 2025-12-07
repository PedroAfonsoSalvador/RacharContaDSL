from .RachaContaParser import RachaContaParser
from .RachaContaVisitor import RachaContaVisitor
from antlr4 import InputStream, CommonTokenStream
from .RachaContaLexer import RachaContaLexer

class RachaContaInterpreter(RachaContaVisitor):
    def __init__(self):
        self.participants = set() #Armazena participantes
        self.raw_expenses = [] #Armazena os gastos brutos

    #Coleta todos os dados e participantes
    def visitProgram(self, ctx):
        self.visitChildren(ctx)
        return self._process_passes()

    #Coleta os dados de cada gasto e identifica participantes
    def visitExpense(self, ctx):
        payer = ctx.payer().getText()
        self.participants.add(payer)
        
        amount = round(float(ctx.value().getText()), 2)
        desc = ctx.description().getText().strip('"')
        
        beneficiaries_ctx = ctx.beneficiaries()
        
        #Coleta os beneficiários e seus pesos
        consumers = []
        if beneficiaries_ctx.getText() == 'todos':
            consumers = 'todos' # Marcador especial
        else:
            people_list = beneficiaries_ctx.list_of_people().person_share()
            for p in people_list:
                name = p.ID().getText()
                weight = 1
                if p.weight():
                    weight = int(p.weight().getText())
                consumers.append({'name': name, 'weight': weight})
                self.participants.add(name) # Adiciona novos participantes
        
        self.raw_expenses.append({
            'desc': desc, 
            'payer': payer, 
            'amount': amount,
            'consumers': consumers
        })

    #Calcula os saldos e resolve as dívidas
    def _process_passes(self):
        balances = {p: 0.0 for p in self.participants}
        transactions_log = []
        
        #Processa os gastos e calcula o débito/crédito
        for exp in self.raw_expenses:
            payer = exp['payer']
            amount = exp['amount']
            consumers_info = exp['consumers']
            
            balances[payer] += amount
            
            #Determina a lista final de consumidores e pesos
            final_consumers = []
            if consumers_info == 'todos':
                final_consumers = [{'name': p, 'weight': 1} for p in self.participants]
            else:
                final_consumers = consumers_info
            
            total_weight = sum(c['weight'] for c in final_consumers)
            
            if total_weight == 0: continue 

            cost_per_share = amount / total_weight

            #Aplica o débito (-)
            for c in final_consumers:
                debt = cost_per_share * c['weight']
                balances[c['name']] -= round(debt, 2) #Subtrai o débito individual (arredondado)

            transactions_log.append({
                'desc': exp['desc'], 
                'payer': exp['payer'], 
                'amount': exp['amount'],
                'consumers': len(final_consumers)
            })

        #Resolve as dívidas
        return self._solve_debts(balances, transactions_log)

    def _solve_debts(self, balances, transactions_log):
        #Resolve as dívidas a partir dos saldos finais
        debtors = []
        creditors = []

        for person, amount in balances.items():
            amount = round(amount, 2)
            if amount < -0.01: 
                debtors.append({'name': person, 'amount': amount})
            elif amount > 0.01:
                creditors.append({'name': person, 'amount': amount})

        transfers = []
        
        #Ordenar para simplificar a matriz de dívida
        debtors.sort(key=lambda x: x['amount']) #Devedores 
        creditors.sort(key=lambda x: x['amount'], reverse=True) #Credores 

        i = 0 
        j = 0 
        while i < len(debtors) and j < len(creditors):
            debtor = debtors[i]
            creditor = creditors[j]

            #Valor a transferir
            amount = min(abs(debtor['amount']), creditor['amount'])
            
            transfers.append({
                'from': debtor['name'], 'to': creditor['name'], 'value': round(amount, 2) 
            })

            #Atualiza saldos
            debtor['amount'] += amount
            creditor['amount'] -= amount

            #Move ponteiros
            if abs(debtor['amount']) < 0.01: i += 1
            if creditor['amount'] < 0.01: j += 1

        return {'log': transactions_log, 'final_transfers': transfers}


def interpret(input_text):
    lexer = RachaContaLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = RachaContaParser(stream)
    tree = parser.program()
    visitor = RachaContaInterpreter()
    return visitor.visit(tree)