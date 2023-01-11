import dao
def listar_tarefas():
        tarefas_BD=dao.select_tarefa()
        for x in tarefas_BD:
            print('Data de criação:',x[1],'Tarefa:',x[0],'\n')   
 
def desfazer_tarefa():
        validacao=False
        tarefas_BD=dao.select_com_id()  

        for x in tarefas_BD:
            print('ID:',x[0],'Tarefa:',x[1],'Data de criação:',x[2])
        try:    
            pergunta=int(input("Digite o ID da tarefa que deseja apagar:\n"))
            for x in tarefas_BD:     
                if pergunta == x[0]:
                    validacao=True  

            if validacao==True:
                pergunta=int(pergunta)
                dao.apagar_tarefa(pergunta)
                print("Pergunta apagada")
            else:
                print("Valor valido")
        except:
            print("Valor invalido")
            

def refazer_tarefa():
    validacao=False
    tarefas_BD=dao.select_com_id_status0()
    for x in tarefas_BD:
        print('ID:',x[0],'Tarefa:',x[1],'Data de criação:',x[2])
    try:
        pergunta=int(input("Digite o ID da tarefa que deseja recuperar:\n"))
        for x in tarefas_BD:
            if pergunta == x[0]:
                validacao=True
            print('Verificando')

        if validacao==True:
                pergunta=int(pergunta)
                dao.recuperar_ultima_tarefa(pergunta)
                print("Pergunta recuperada")
        else:
            print("Valor não consta no banco de dados")
    except:
        print("Valor invalido")
     

while True:
    tarefa=input('''\t Lista de tarefas
    - Digite a tarefa que deseja adicionar
    - Digite "listar" para listar as tarefas
    - Digite "desfazer" para desfazer a ultima tarefa
    - Digite "refazer" para refazer a ultima tarefa
    - Digite "sair" para sair da sua lista de tarefas \n''').lower()


    if tarefa =='listar':
        listar_tarefas()
    
    elif tarefa == "desfazer":
        desfazer_tarefa()
    
    elif tarefa == "refazer":
        refazer_tarefa()
    
    elif tarefa == 'sair':
        break
    else:
        dao.insert_tarefa(tarefa)
        


        


