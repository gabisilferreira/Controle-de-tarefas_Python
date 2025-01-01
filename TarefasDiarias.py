tarefasPendentes =[]
tarefasConcluidas = []
tarefasProgresso =[]

def modificar():
    try:
        tarefaModificar = input("Digite a tarefa que deseja modificar: ").lower()
        selecao = int(input("Digite a opcao que deseja modificar a tarefa: \n  1- Concluída 2- Em progresso \n"))
        if selecao ==1:
            if tarefaModificar in tarefasPendentes:
                tarefasPendentes.remove(tarefaModificar)
                tarefasConcluidas.append(tarefaModificar)
                print(f"Tarefa '{tarefaModificar}' marcada como concluída!")
            else:
                print("Tarefa não encontrada")
        elif selecao ==2:
            if tarefaModificar in tarefasPendentes:
                tarefasPendentes.remove(tarefaModificar)
                tarefasProgresso.append(tarefaModificar)
                print(f"Tarefa '{tarefaModificar}' marcada como em progresso!")
            else:
                print("Tarefa não encontrada")
        else:
            print("Você não digitou a modificação que deseja")  
    except ValueError:
        print("Você não digitou a opção correta")


def remover():
    tarefaRemover = input("Digite a tarefa que deseja remover: ").lower
    if tarefaRemover in tarefasProgresso:
        tarefasProgresso.remove(tarefaRemover)
        print(f"Tarefa {tarefaRemover} removida com sucesso")
    elif tarefaRemover in tarefasPendentes:
        tarefasPendentes.remove(tarefaRemover)
        print(f"Tarefa {tarefaRemover} removida com sucesso")
    else:
        print("Tarefa não encontrada. Por gentileza verificar se tarefa foi adicionada")


def adicionar():
    tarefa = input("Digite a tarefa que deseja adicionar: ").lower()
    tarefasPendentes.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")


def listar():
        print("\n=== Listagem de Tarefas ===")
        print(f"Tarefas Pendentes: {tarefasPendentes} (Total: {len(tarefasPendentes)})")
        print(f"Tarefas em Progresso: {tarefasProgresso} (Total: {len(tarefasProgresso)})")
        print(f"Tarefas Concluídas: {tarefasConcluidas} (Total: {len(tarefasConcluidas)})")
    
        # Calculando o progresso
        totalTarefas = len(tarefasPendentes) + len(tarefasProgresso) + len(tarefasConcluidas)
        if totalTarefas > 0:
            progresso = (len(tarefasConcluidas) / totalTarefas) * 100
            print(f"Progresso total: {progresso:.2f}% concluído.")
        else:
         print("Nenhuma tarefa registrada ainda.")
    


print("Controle de Tarefas Diárias")

while True:
    try:
        opcao = int(input("Digite o número correspondente a opção que deseja: \n 1- Listar tarefas 2- Adicionar tarefas 3- Remover tarefas 4-Modificar tarefas 5- Sair \n"))
        if opcao ==1:
            listar()
        elif opcao == 2:
            adicionar()
        elif opcao ==3:
            remover()
        elif opcao == 4:
            modificar()
        elif opcao == 5:
            print("Obrigada por utilizar nosso sistema. Até breve")
            exit()
        else:
            print("A opção digitada não existe. Por gentileza, verificar.")

    except ValueError:
        print("Você não digitou a opção correta")