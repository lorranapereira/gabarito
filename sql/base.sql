drop table aluno;
create table aluno(
    codigo serial,
    login VARCHAR(100) NOT NULL UNIQUE,
    idade integer not null,
    CONSTRAINT codigo PRIMARY KEY (codigo)
);
insert into aluno (login, idade) values ('guilherme',18),('lorrana',19),('suelen',20);