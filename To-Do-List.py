class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[len(self.tasks) + 1] = task
        print('\n**********************')
        print(f'Tarefa "{task}" adicionada com sucesso.')
        print('**********************')

    def remove_task(self, task_number):
        if task_number in self.tasks:
            removed_task = self.tasks.pop(task_number)
            print('\n**********************')
            print(f'Tarefa "{removed_task}" removida com sucesso.')
            print('**********************')
        else:
            print('\n**********************')
            print(f'Tarefa com número {task_number} não encontrada.')
            print('**********************')

    def show_tasks(self):
        if not self.tasks:
            print('\n**********************')
            print('A lista de tarefas está vazia.')
            print('**********************')
        else:
            print('\n**********************')
            print('Lista de Tarefas:')
            for number, task in self.tasks.items():
                print(f'{number}. {task}')
            print('**********************')

# Instanciar a lista de tarefas
to_do_list = ToDoList()

while True:
    print('\n**********************')
    print("Escolha uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Mostrar Tarefas")
    print("0. Sair")
    print('**********************')

    choice = input("Digite o número da opção desejada: ")

    if choice == '1':
        task = input("Digite a nova tarefa: ")
        to_do_list.add_task(task)
    elif choice == '2':
        task_number = int(input("Digite o número da tarefa a ser removida: "))
        to_do_list.remove_task(task_number)
    elif choice == '3':
        to_do_list.show_tasks()
    elif choice == '0':
        print('\n**********************')
        print("Saindo do programa. Até mais!")
        print('**********************')
        break
    else:
        print('\n**********************')
        print("Opção inválida. Tente novamente.")
        print('**********************')
