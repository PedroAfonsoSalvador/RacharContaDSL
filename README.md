# DSL RachaConta: Acerto de Contas Ponderado

## Equipe
- **Pedro Afonso Cavalcanti Salvador**

---

## Motivação
Dividir despesas de forma justa, especialmente em viagens, jantares ou eventos com múltiplos participantes e itens de consumo variado, é complexo e propenso a erros. Calcular quem deve pagar o quê, e minimizar o número total de transações, é um problema de otimização ideal para uma Linguagem de Domínio Específico (DSL).
A DSL RachaConta automatiza:
- O cálculo do consumo individual, suportando rateio ponderado.
- A determinação dos saldos finais (quem deve e quem tem a receber).
- A simplificação das dívidas, gerando o número mínimo de transferências necessárias.

---

## Descrição Informal da Linguagem
A linguagem foi projetada para funcionar como um "extrato inteligente", onde o usuário descreve o que aconteceu no evento e o interpretador resolve a matemática financeira. A estrutura de um programa segue um fluxo lógico de três etapas:

1. Declaração do Evento: Inicia o programa com a palavra-chave "evento" e o nome do evento entre aspas.
2. Registro de Transações: O corpo do programa é composto por uma lista de comandos "gasto". Cada linha narra uma despesa financeira, definindo:
- O Valor: Quanto custou.
- O Item: Descrição textual do gasto.
- O Pagador: Quem desembolsou o dinheiro.
- Os Beneficiários: Quem usufruiu do item (suportando pesos, ex: Joao(2) para quem consumiu duas cotas, ou a palavra-chave todos).
3. Fechamento: O comando "fechar" encerra a lista de gastos e dispara a execução do algoritmo de acerto de contas.

---

## Passo a Passo da Execução
1. Pré-requisitos:
- Python 3.7 ou superior.
- ANTLR 4 instalado e configurado.
- Dependência ANTLR para Python:
```bash
pip install antlr4-python3-runtime==4.13.1
```
2. Clone o repositório:
```bash
git clone https://github.com/PedroAfonsoSalvador/RachaContaDSL.git
cd RachaContaDSL
```
3. Gere os analisadores (Lexer, Parser e Visitor):
```bash
antlr4 -Dlanguage=Python3 -o src/rachaconta -visitor -no-listener grammar/RachaConta.g4
```
4. Execute com um arquivo de exemplo:
```bash
python src/main.py examples/churrasco.rc
```

---

## Exemplo de Programas
Exemplo 01:

Entrada
```bash
evento "Churrasco da Aprovação"
gasto 120.00 em "Picanha" por Pedro para todos
gasto 60.00 em "Cerveja" por Ana para Pedro(1),Ana(1),Joao(2)
gasto 30.00 em "Refrigerante" por Joao para todos
gasto 15.00 em "Gelo" por Maria para todos
fechar
```
Saída
```bash
=== Extrato do Evento ===
- Pedro pagou R$120.00 (Picanha)
- Ana pagou R$60.00 (Cerveja)
- Joao pagou R$30.00 (Refrigerante)
- Maria pagou R$15.00 (Gelo)

========================================
ACERTO DE CONTAS (MÍNIMO DE TRANSAÇÕES)
========================================
 -> Joao deve pagar R$ 41.25 para Pedro
 -> Maria deve pagar R$ 22.50 para Pedro
 -> Maria deve pagar R$ 3.75 para Ana
----------------------------------------
```

Exemplo 02:

Entrada
```bash
evento "Viagem para o Rio"
gasto 150.00 em "Gasolina" por Lucas para todos
gasto 30.00 em "Pedagios" por Maria para Lucas(1), Pedro(3), Maria(1)
gasto 45.00 em "Cafe da Manha" por Pedro para Lucas, Maria
gasto 20.00 em "Lembranca" por Lucas para Lucas
fechar
```
Saída
```bash
=== Extrato do Evento ===
- Lucas pagou R$150.00 (Gasolina)
- Maria pagou R$30.00 (Pedagios)
- Pedro pagou R$45.00 (Cafe da Manha)
- Lucas pagou R$20.00 (Lembranca)

========================================
ACERTO DE CONTAS (MÍNIMO DE TRANSAÇÕES)
========================================
 -> Pedro deve pagar R$ 23.00 para Lucas
 -> Maria deve pagar R$ 48.50 para Lucas
----------------------------------------
```

Exemplo 03:

Entrada
```bash
evento "Happy Hour da Firma"
gasto 40.00 em "Batata Frita" por Ana para todos
gasto 60.00 em "Torre de Chopp" por Beto para Ana, Beto, Carla
gasto 100.00 em "Whisky Importado" por Davi para Carla, Davi
fechar
```
Saída
```bash
=== Extrato do Evento ===
- Ana pagou R$40.00 (Batata Frita)
- Beto pagou R$60.00 (Torre de Chopp)
- Davi pagou R$100.00 (Whisky Importado)

========================================
ACERTO DE CONTAS (MÍNIMO DE TRANSAÇÕES)
========================================
 -> Carla deve pagar R$ 40.00 para Davi
 -> Carla deve pagar R$ 30.00 para Beto
 -> Carla deve pagar R$ 10.00 para Ana
----------------------------------------
```
