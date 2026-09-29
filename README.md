# Especificação do Projeto: Sistema de Gestão de Equipamentos Industriais

## Objetivo

Desenvolver um módulo de gestão de ativos e equipamentos para controle operacional de chão de fábrica e oficinas, aplicando os conceitos fundamentais do framework Django: criação e modelagem de banco de dados relacional com o ORM, controle de versionamento de esquema via migrações, customização avançada da interface administrativa nativa (Django Admin) e execução completa do ciclo de operações de banco de dados (CRUD: Create, Read, Update, Delete) utilizando dados fictícios baseados na rotina industrial.

## Descrição Geral do Sistema

O aplicativo Equipamentos atua como o registro mestre de ativos operacionais de uma oficina ou planta industrial. O sistema centraliza informações críticas sobre as máquinas utilizadas nas operações diárias — como elevadores hidráulicos, compressores de ar, scanners de diagnóstico e inversores de solda.

Através do módulo, a equipe de gestão e manutenção consegue controlar o ciclo de vida dos ativos, monitorar datas e intervalos de manutenção preventiva, rastrear códigos de patrimônio (TAGs) e filtrar equipamentos por seu estado operacional (Ativo, Em Manutenção ou Inativo), garantindo maior rastreabilidade e integridade das informações no banco de dados.

## Começando

Escolha um diretório onde ficará o projeto, como `~/Documents`, e crie a pasta `oficina`:

```bash
pwd
cd ~/Documents # ou um diretório de sua preferência
mkdir -p oficina
cd oficina
```

Depois de entrar no diretório do projeto, crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente no terminal utilizado.

**Linux — Bash**

```bash
source venv/bin/activate
```

**Windows — PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows — Prompt de Comando**

```bash
venv\Scripts\activate.bat
```

**Instale as dependências:**

```bash
python -m pip install -r requirements.txt
```

O ambiente virtual mantém as dependências Python do projeto separadas das demais instalações.

## Instalando o Django

Com o ambiente virtual ativo, instale o Django:

```bash
python -m pip install django
```

Verifique a instalação:

```bash
django-admin --version
```

O uso de `python -m pip` associa a instalação ao interpretador Python selecionado no terminal.

## Criando o projeto

Dentro da pasta `carros`, execute:

```bash
django-admin startproject core .
```

### Entendendo o comando

- **`django-admin`:** interface de linha de comando do Django para tarefas administrativas.
- **`startproject`:** comando que cria a estrutura inicial de um projeto.
- **`core`:** nome escolhido para o pacote de configuração. Pode ser outro nome Python válido, desde que não conflite com módulos existentes.
- **`.` (ponto):** indica o diretório atual como destino. Assim, `manage.py` e o pacote `core/` são criados diretamente dentro de `oficina/`.

Neste contexto, `oficina/` é o diretório de trabalho e `core/` é o pacote de configuração do projeto.

## O projeto padrão

Após os passos anteriores, a pasta `oficina/` contém:

| Caminho | Origem e finalidade |
| --- | --- |
| `oficina/venv/` | Ambiente virtual criado com `python -m venv venv`. |
| `oficina/core/` | Pacote de configuração criado por `startproject`. |
| `oficina/manage.py` | Script de gerenciamento criado por `startproject`. |

A pasta `venv/` faz parte do ambiente preparado para o projeto, mas não é gerada pelo Django.

### Arquivos fundamentais

| Arquivo | Responsabilidade |
| --- | --- |
| `manage.py` | Permite executar comandos administrativos, como iniciar o servidor, criar cores e trabalhar com migrações. Define o valor padrão de `DJANGO_SETTINGS_MODULE` como `core.settings`; o Django carrega a configuração indicada. |
| `core/__init__.py` | Identifica o diretório `core/` como um pacote Python regular. |
| `core/settings.py` | Centraliza configurações de banco de dados, idioma, fuso horário, arquivos estáticos e cores instalados. |
| `core/urls.py` | Declara as rotas do projeto, associando caminhos de URL a views ou a outros conjuntos de rotas. |
| `core/wsgi.py` | Disponibiliza o ponto de entrada para servidores compatíveis com WSGI, uma interface síncrona. |
| `core/asgi.py` | Disponibiliza o ponto de entrada para servidores compatíveis com ASGI, que suporta execução assíncrona. |

Na configuração inicial, `BASE_DIR` aponta para o diretório-base do projeto, onde está `manage.py`. A lista `INSTALLED_APPS` indica as aplicações instaladas.

ASGI também comporta protocolos como WebSocket, mas a existência de `asgi.py` não implementa esse recurso automaticamente; ele exige componentes e configuração adicionais.

## Executando o projeto

Com o ambiente virtual ativo, execute no diretório que contém `manage.py`:

```bash
python manage.py runserver
```

Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador para verificar a página inicial. Para encerrar o servidor, pressione `Ctrl+C` no terminal.

O comando `runserver` inicia o servidor de desenvolvimento local.

## 🛠️ Módulo de Gestão de Equipamentos Industriais

Este módulo faz parte do sistema de gestão para oficina/indústria, desenvolvido em Python e Django.

### 🎯 Funcionalidades Implementadas
- **Modelagem ORM:** Entidade `Equipamento` com suporte a datas, valores, regras de atributos únicos (TAG) e enums de status (`choices`).
- **Migrações:** Versionamento do banco de dados relacional.
- **Django Admin:** Painel completo para gestão do ciclo de vida dos ativos.
- **CRUD Operacional:** Inserção e validação de equipamentos reais de chão de fábrica (Elevadores, Compressores, Scanners).

### 🚀 Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Aplique as migrações: `python manage.py migrate`
3. Crie o superusuário: `python manage.py createsuperuser`
4. Inicie o servidor: `python manage.py runserver`

[Screenshot do painel Admin](./docs/evidencias/admin_equipamentos_equipment.png)

---

**Referência técnica:** [documentação oficial do Django](https://docs.djangoproject.com/en/5.2/intro/tutorial01/). Selecionar a versão correspondente à instalação.

- Origem das notas sincronizadas
    
    Página de origem do conteúdo sincronizado exibido nesta atividade.
    
    [Projeto Django — notas sincronizadas](https://app.notion.com/p/Projeto-Django-notas-sincronizadas-3cd56cb3ac7380a8b429fb30d28cd027?pvs=21)