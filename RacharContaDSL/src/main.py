import sys
import os
from rachaconta.interpreter import interpret #Importa a função que executa o interpretador ANTLR

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    #Verifica se o usuário passou o arquivo como argumento
    if len(sys.argv) < 2:
        print("Uso: python src/main.py <arquivo.rc>")
        return
    
    filename = sys.argv[1]

    try:
        #Lê o conteúdo o arquivo com o comando
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        #Executa o interpretador 
        result = interpret(content)
        
        #Exibe a lista de gastos registradas no arquivo
        print("\n=== Extrato do Evento ===")
        for log in result['log']:
            print(f"- {log['payer']} pagou R${log['amount']:.2f} ({log['desc']})")
        
        #Exibe o cálculo das dívidas minimizadas
        print("\n" + "="*40)
        print("ACERTO DE CONTAS (MÍNIMO DE TRANSAÇÕES)")
        print("="*40)
        
        if not result['final_transfers']:
            print("Tudo quitado! Ninguém deve nada.")
        else:
            #Mostra quem deve pagar para quem
            for t in result['final_transfers']:
                print(f" -> {t['from']} deve pagar R$ {t['value']:.2f} para {t['to']}")
            
        print("-" * 40 + "\n")
    
    #Caso o arquivo não exista
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")

    #Erros durante a interpretação 
    except Exception as e:
        print(f"Erro durante a interpretação: {str(e)}")


if __name__ == "__main__":
    main()
