--=======================================================
-- Criando Banco de Dados: db_praia
-- Data: 03/08/2025
-- Autor: Carlos A. Zarzar
--=======================================================

DROP DATABASE IF EXISTS db_praia;
CREATE DATABASE db_praia
    WITH
    OWNER = zarzar
    ENCODING = 'UTF8'
    LC_COLLATE = 'pt_BR.UTF-8'
    LC_CTYPE = 'pt_BR.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE db_praia IS 'Rascunho para banco de dados do app PRAIA';

--=======================================================
-- Conectar ao banco criado
-- \c db_praia

--=======================================================
-- Criando Tabelas
--=======================================================

-- Usuários do sistema
CREATE TABLE "user" (
    id_user SERIAL PRIMARY KEY,
    nome_completo VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100),
    nome_login VARCHAR(50)
);

-- Proprietários de fazendas
CREATE TABLE "proprietario" (
    id_proprietario SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL,
    cpf CHAR(11) NOT NULL,
    idade INT,
    sexo VARCHAR(1),
    id_user INT NOT NULL REFERENCES "user"(id_user)
);

-- Fazendas aquícolas
CREATE TABLE "fazenda" (
    id_fazenda SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    sist_cultivo VARCHAR(50),
    cnpj CHAR(14),
    gps DECIMAL(10,6),
    especie VARCHAR(50),
    id_user INT NOT NULL REFERENCES "user"(id_user),
    id_proprietario INT NOT NULL REFERENCES "proprietario"(id_proprietario),
    id_endereco INT,
    id_telefone INT
);

--=======================================================
-- Inserindo Dados Simulados
--=======================================================

-- Usuários
INSERT INTO "user" (nome_completo, email, senha, nome_login) VALUES
('Carlos Andrade', 'carlos.andrade@example.com', 'senha123', 'carlos_a'),
('Fernanda Lima', 'fernanda.lima@example.com', 'senha456', 'fer_lima'),
('João Silva', 'joao.silva@example.com', 'senha789', 'joaos'),
('Maria Oliveira', 'maria.oliveira@example.com', 'senha321', 'maria_ol'),
('Pedro Santos', 'pedro.santos@example.com', 'senha654', 'pedros');

-- Proprietários
INSERT INTO "proprietario" (nome, cpf, idade, sexo, id_user) VALUES
('Carlos Andrade', '12345678900', 45, 'M', 1),
('Fernanda Lima', '23456789001', 38, 'F', 2),
('João Silva', '34567890123', 50, 'M', 3);

-- Fazendas
INSERT INTO "fazenda" (nome, sist_cultivo, cnpj, gps, especie, id_user, id_proprietario, id_endereco, id_telefone) VALUES
('Fazenda Mar Azul', 'Tanque Escavado', '11223344000199', -1.455833, 'Tilápia', 1, 1, 1, 1),
('Fazenda Rio Doce', 'Viveiro Escavado', '22334455000188', -1.234567, 'Tambaqui', 2, 2, 2, 2),
('Fazenda Sol Nascente', 'Rede em Reservatório', '33445566000177', -1.876543, 'Pirarucu', 3, 3, 3, 3);

--=======================================================
-- Fim do Script
--=======================================================

