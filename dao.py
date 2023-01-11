import mysql.connector as conexao

def conecta_banco():
    conect=conexao.connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database = "bd_tarefas"
    )
    return conect
def insert_tarefa(tarefa):
    sql='insert into tarefas(tarefa) values(%s)'
    conexao=conecta_banco()
    manipulador=conexao.cursor()
    valores=(tarefa,)
    manipulador.execute(sql,valores)
    conexao.commit()
def select_tarefa():
    sql='select tarefa,criacao from tarefas where status_tarefa=1'
    conexao=conecta_banco()
    manipulador=conexao.cursor()
    manipulador.execute(sql)
    return manipulador.fetchall()

def apagar_tarefa(id):
    sql='update tarefas set status_tarefa = 0 where id=%s'
    conexao=conecta_banco()
    manipulador=conexao.cursor()
    valores=(id,)
    manipulador.execute(sql,valores)
    conexao.commit()

def select_com_id():
    sql='select id,tarefa,criacao from tarefas where status_tarefa=1'
    conexao=conecta_banco()
    manipulador=conexao.cursor()
    manipulador.execute(sql)
    return manipulador.fetchall()

def select_com_id_status0():
    sql='select id,tarefa,criacao from tarefas where status_tarefa=0'
    conexao=conecta_banco()
    manipulador=conexao.cursor()
    manipulador.execute(sql)
    return manipulador.fetchall()

def recuperar_ultima_tarefa(id):
    sql='update tarefas set status_tarefa = 1 where id=%s'
    conexao=conecta_banco()
    manipulador=conexao.cursor()
    valores=(id,)
    manipulador.execute(sql,valores)
    conexao.commit()