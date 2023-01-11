create database if not exists bd_tarefas;
use bd_tarefas;
create table tarefas(
id int auto_increment primary key,
tarefa varchar(150) not null,
status_tarefa boolean  default 1,
criacao timestamp null default current_timestamp
);
use bd_tarefas;
insert into tarefas(tarefa)
values ("Isso é um teste");

s

