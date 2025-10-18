```
    ==========================================================================================
    Sistema Bancário v1.2- POO em Python
    ==========================================================================================

    Objetivo:
        Consolidar o aprendizado sobre Programação Orientada a Objetos (POO) em Python.

    Autor:
        Luiz Carlos Machado

    Descrição geral:
        Este sistema simula operações bancárias básicas, aplicando conceitos de POO 
        como classes, encapsulamento, herança e composição.

    Regras e funcionalidades:
        - Permitir o cadastro de novos usuários.
        - Impedir o cadastro de mais de um usuário com o mesmo CPF.
        - Permitir a abertura de contas bancárias.
        - Cada conta possui: agência, número da conta, saldo e extrato.
        - O número da conta é sequencial, iniciando em "001".
        - Todas as contas abertas são, por padrão, do tipo Conta Corrente.
        A estrutura do código, porém, permite expansão para múltiplos tipos de conta.
        - As contas bancárias devem ser armazenadas em uma lista.
        - Um usuário pode possuir várias contas, mas cada conta pertence a apenas um usuário.
        - Permitir depósitos de valores positivos (inteiros ou decimais).
        - O extrato deve exibir o histórico de depósitos e saques.
        - Permitir até 3 saques diários, com limite máximo de R$ 500,00 por saque.
        - O saldo não pode ficar negativo.
    =============================================================================================
```
---

## Funcionalidades

- **Cadastro de clientes** com validação de CPF e data de nascimento.  
- **Abertura de contas correntes** vinculadas a clientes existentes.  
- **Depósitos e saques** com validação de valores e limite diário de operações.  
- **Histórico detalhado** de todas as transações realizadas.  
- **Registro automático de data e hora** em cada operação.  
- **Interface de menu interativo** via terminal. 

```
        ╔══════════════════════════════════════╗
        ║         SISTEMA BANCÁRIO v1.2        ║
        ╠══════════════════════════════════════╣
        ║             MENU PRINCIPAL           ║
        ╠══════════════════════════════════════╣
        ║ [a] Abrir conta                      ║
        ║ [d] Depositar                        ║
        ║ [s] Sacar                            ║
        ║ [e] Extrato                          ║
        ║ [l] Listar clientes                  ║ 
        ║ [p] Pesquisar Clientes               ║ 
        ║ [q] Sair                             ║
        ╚══════════════════════════════════════╝
        => 
```
---

## Estrutura do Projeto

```
python-sistema-bancario-v1.2/
│
├── sistema_bancario.py # Arquivo principal (menu e fluxo do sistema)
├── cliente.py # Classe Cliente (dados do titular)
├── pessoa_fisica.py # Subclasse de Cliente com CPF e data de nascimento
├── conta.py # Classe base Conta
├── conta_corrente.py # Subclasse ContaCorrente com limite de saque
├── transacao.py # Classe abstrata para operações financeiras
├── deposito.py # Classe para operações de depósito
├── saque.py # Classe para operações de saque
└── historico.py # Classe responsável por registrar transações
```


---

## Conceitos Aplicados

- **Programação Orientada a Objetos (POO)**  
  - Herança  
  - Encapsulamento  
  - Polimorfismo  
  - Abstração  

- **Boas Práticas**
  - Separação de responsabilidades  
  - Validação de dados de entrada  
  - Modularização de classes  
  - Docstrings e tipagem clara  

---

## Como Executar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/python-sistema-bancario-v1.2.git
   cd python-sistema-bancario-v1.2

    Execute o sistema:

    python3 sistema_bancario.py


## Diagrama de Classes

```mermaid
classDiagram
    direction TB

    class SistemaBancario {
        +clientes : list[PessoaFisica]
        +contas : list[ContaCorrente]
        +cadastrar_cliente()
        +abrir_conta()
        +depositar()
        +sacar()
        +exibir_historico()
        +executar()
    }

    class Cliente {
        <<abstract>>
        -nome : str
        -endereco : str
        +__init__(nome, endereco)
    }

    class PessoaFisica {
        -cpf : str
        -data_nascimento : str
        +__init__(nome, cpf, data_nascimento, endereco)
    }

    class Conta {
        <<abstract>>
        -numero : int
        -cliente : Cliente
        -saldo : float
        -historico : Historico
        +__init__(cliente)
        +sacar(valor)
        +depositar(valor)
    }

    class ContaCorrente {
        -limite : float
        -limite_saques : int
        +sacar(valor)
    }

    class Historico {
        -transacoes : list[Transacao]
        +adicionar_transacao(transacao)
        +listar_transacoes()
    }

    class Transacao {
        <<abstract>>
        +registrar(conta)
    }

    class Deposito {
        -valor : float
        +registrar(conta)
    }

    class Saque {
        -valor : float
        +registrar(conta)
    }

    %% Relações
    PessoaFisica --|> Cliente
    ContaCorrente --|> Conta
    Deposito --|> Transacao
    Saque --|> Transacao
    Conta --> Historico
    Conta --> Cliente
    Historico --> Transacao
    SistemaBancario --> PessoaFisica
    SistemaBancario --> ContaCorrente

