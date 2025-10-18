from conta_corrente import ContaCorrente
from pessoa_fisica import PessoaFisica
from datetime import datetime
from deposito import Deposito
from saque import Saque
import os

class SistemaBancario:
    
    """
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
    """
    
    _clientes = []

    @staticmethod
    def _limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    # -------------------------------
    # MÉTODO BUSCAR CLIENTE POR CPF
    # -------------------------------  
    @classmethod
    def _buscar_cliente_por_cpf(cls, cpf):
        for cliente in cls._clientes:
            if getattr(cliente, "cpf", None) == cpf:
                return cliente
        return None
    
    # -------------------------------
    # MÉTODO VERIFICAR CONTA EXISTENTE
    # -------------------------------  
    @classmethod
    def _verificar_conta_existente(cls, cliente, numero_agencia, numero_conta):
        for conta in cliente.contas:
            if conta.numero == numero_conta and conta.agencia == numero_agencia:
                return numero_agencia, numero_conta
        return None, None
    
    # -------------------------------
    # MÉTODO VERIFICAR CLIENTE EXISTENTE
    # -------------------------------  
    @classmethod
    def _verificar_cliente_existente(cls):
        cls._limpar_tela()
        if not cls._clientes:
            print("Nenhum cliente cadastrado.")
        else:
            return True   
    
    # -------------------------------
    # MÉTODO GERAR NÚMERO DA CONTA
    # -------------------------------
    @classmethod
    def _gerar_numero_conta(cls) -> int:
        """
            Gera o próximo número de conta disponível.
            Percorre todos os clientes e suas contas existentes.
        """
        numeros_existentes = []

        # Percorre todos os clientes cadastrados
        for cliente in getattr(cls, "_clientes", []):
            # Cada cliente tem uma lista de contas
            for conta in cliente.contas:
                try:
                    numeros_existentes.append(int(conta.numero))
                except Exception:
                    pass  # ignora se algo estiver errado no número
                
        # Retorna o próximo número disponível (máximo + 1)
        return str(max(numeros_existentes) + 1 if numeros_existentes else 1).zfill(3)
    
    # -------------------------------
    # MÉTODO ABRIR CONTA
    # -------------------------------
    @classmethod
    def _abrir_conta_corrente(cls, cliente):
        ContaCorrente.nova_conta(cliente, agencia="0001", numero=cls._gerar_numero_conta())
        print(f"\nConta criada com sucesso!")
        
    # -------------------------------
    # MÉTODO FORMULÁRIO DE CADASTRO CLIENTE
    # -------------------------------
    @classmethod
    def _formulario_cadastro_cliente(cls):
        cls._limpar_tela()
        print("\n=== Cadastro de Novo Cliente ===")

        nome = input("\nNome completo: ").strip()
        endereco = input("Endereço: ").strip()

        # Capturar e validar data de nascimento
        data_nasc = cls._obter_data_nascimento()

        return {
            "nome": nome,
            "data_nascimento": data_nasc,
            "endereco": endereco
        }

    @staticmethod
    def _obter_data_nascimento():
        """Solicita e valida a data de nascimento no formato DD/MM/YYYY."""
        while True:
            try:
                ano = int(input("Ano de nascimento (YYYY): "))
                mes = int(input("Mês (MM): "))
                dia = int(input("Dia (DD): "))
                data = datetime(ano, mes, dia)
                return data.strftime("%d/%m/%Y")
            except ValueError:
                print("Data inválida. Tente novamente.\n")

    # -------------------------------
    # MÉTODO ABRIR CONTA
    # -------------------------------
    @classmethod
    def _abrir_conta(cls):
        """
        Abre uma nova conta para um cliente existente
        ou cadastra um novo cliente e cria sua conta.
        """
        cls._limpar_tela()
        cpf = cls._validar_cpf()
        cliente = cls._buscar_cliente_por_cpf(cpf)
        abrir_conta = False

        if cliente:
            cls._exibir_dados_cliente(cliente)
            resposta = input("\nDeseja abrir uma nova conta para este cliente? (s/n): ").strip().lower()
            abrir_conta = (resposta == "s")
        elif cpf:
            print("\nCliente não encontrado. Vamos realizar o cadastro:")
            dados = cls._formulario_cadastro_cliente()
            cliente = PessoaFisica(
                nome=dados["nome"],
                cpf=cpf,
                data_nascimento=dados["data_nascimento"],
                endereco=dados["endereco"]
            )
            cls._clientes.append(cliente)
            abrir_conta = True  # cliente novo, cria conta automaticamente

        if abrir_conta:
            cls._abrir_conta_corrente(cliente)

        input("\nPressione Enter para continuar...")

    # -------------------------------
    # MÉTODO AUXILIAR PARA EXIBIÇÃO
    # -------------------------------
    @staticmethod
    def _exibir_dados_cliente(cliente):
        cls_linha = "═" * 50
        print(f"\n{cls_linha}")
        print(f"DADOS DO CLIENTE".center(50))
        print(f"{cls_linha}")

        print(f"Nome: {cliente.nome}")
        print(f"CPF: {cliente.cpf}")
        print(f"Data de Nascimento: {cliente.data_nascimento}")
        
        print(f"{'-'*50}")
        if cliente.contas:
            print(f"Contas Vinculadas ({len(cliente.contas)}):")
            for i, conta in enumerate(cliente.contas, start=1):
                print(f"   {i}. Agência: {conta.agencia}  |  Conta: {conta.numero}")
        else:
            print("Nenhuma conta vinculada.")

        print(f"{cls_linha}\n")

    # -------------------------------
    # MÉTODO DEPOSITAR
    # -------------------------------
    @classmethod
    def _depositar(cls):
        if cls._verificar_cliente_existente():
            cpf = cls._validar_cpf()
            cliente = cls._buscar_cliente_por_cpf(cpf)
            if cliente:
                agencia, conta = cls._verificar_conta_existente(cliente, input("Digite o numero da agência:"), input("Digite o numero da conta:"))
                if agencia or conta:
                    for c in cliente.contas:
                        if c.numero == conta and c.agencia == agencia:
                            operacao_deposito = Deposito(input("Digite o valor do depósito: "), datetime.now().strftime("%d/%m/%Y %H:%M"))
                            if(operacao_deposito.executar(c)):
                                c.historico.adicionar_transacao(operacao_deposito)
                else: 
                    print("Conta não encontrada.")

        input("\nPressione Enter para continuar...")
    
    # -------------------------------
    # MÉTODO SACAR
    # -------------------------------
    @classmethod
    def _sacar(cls):
        if cls._verificar_cliente_existente():
            cpf = cls._validar_cpf()
            cliente = cls._buscar_cliente_por_cpf(cpf)
            if cliente:
                agencia, conta = cls._verificar_conta_existente(cliente, input("Digite o numero da agência:"), input("Digite o numero da conta:"))
                if agencia or conta:
                    for c in cliente.contas:
                        if c.numero == conta and c.agencia == agencia:
                            operacao_saque = Saque(input("Digite o valor do saque: "), datetime.now().strftime("%d/%m/%Y %H:%M"))
                            if(operacao_saque.executar(c)):
                                c.historico.adicionar_transacao(operacao_saque)
                else: 
                    print("Conta não encontrada.")

        input("\nPressione Enter para continuar...")
    
    # -------------------------------
    # MÉTODO EXTRATO
    # -------------------------------
    @classmethod
    def _extrato(cls):
        if cls._verificar_cliente_existente():
            cpf = cls._validar_cpf()
            cliente = cls._buscar_cliente_por_cpf(cpf)
            if cliente:
                agencia, conta = cls._verificar_conta_existente(cliente, input("Digite o numero da agência:"), input("Digite o numero da conta:"))
                if agencia or conta:
                    for c in cliente.contas:
                        if c.numero == conta and c.agencia == agencia:
                            cls._limpar_tela()
                            print(f"{'='*60}")
                            print(f"{'EXTRATO BANCÁRIO':^60}")
                            print(f"{'='*60}")
                            print(f"Cliente: {cliente.nome}")
                            print(f"CPF: {cliente.cpf}")
                            print(f"Agência: {agencia}")
                            print(f"Conta: {conta}")
                            print(f"{'-'*60}")
                            c.historico.exibir_historico()
                            print(f"{'-'*60}")
                            print(f"Saldo atual: R$ {c.saldo:>8.2f}")
                            print(f"{'='*60}")
                else: 
                    print("Conta não encontrada.")

        input("\nPressione Enter para continuar...")
    
    # -------------------------------
    # MÉTODO VALIDAR CPF
    # -------------------------------
    @classmethod
    def _validar_cpf(cls):
        """
        Solicita e valida o CPF do usuário.
        Aceita entrada com ou sem pontos e traços, desde que contenha 11 dígitos válidos.
        
        Retorna:
            str: CPF válido contendo apenas números.
        """
        while True:
            cpf = input("Digite o CPF (com ou sem pontuação): ").strip()

            # Remove pontos e traços, caso existam
            cpf = cpf.replace(".", "").replace("-", "")

            if len(cpf) != 11 or not cpf.isdigit():
                print("\nCPF inválido. O CPF deve conter exatamente 11 números.")
                continue

            print(f"\nCPF {cpf} validado com sucesso!\n")
            return cpf
         
    # -------------------------------
    # MÉTODO LISTAR CLIENTES
    # -------------------------------
    @classmethod
    def _listar_clientes(cls):
        if cls._verificar_cliente_existente():
            print("\nClientes cadastrados:")
            for cliente in cls._clientes:
                print(f"{cliente.nome} | CPF: {cliente.cpf} | Contas: {len(cliente.contas)}")
        input("\nPressione Enter para continuar...")
    
    # -------------------------------
    # MÉTODO PESQUISAR CLIENTES
    # -------------------------------
    @classmethod
    def _pesquisar_cliente(cls):
        """
        Busca os dados do cliente com base no cpf
        """
        if cls._verificar_cliente_existente():
            cpf = cls._validar_cpf()
            cliente = cls._buscar_cliente_por_cpf(cpf)
        
            if cliente:
                cls._exibir_dados_cliente(cliente)
            else:
                print("\nCliente não encontrado.")
        input("\nPressione Enter para continuar...")
        
    # -------------------------------
    # MÉTODO MENU INTERATIVO
    # -------------------------------
    @classmethod
    def _menu(cls):
        _interface = """
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
        => """
    
        while True:
            cls._limpar_tela()
            opcao = input(_interface).lower()
            if opcao == "a":
                cls._abrir_conta()
            elif opcao == "d":
                cls._depositar()
            elif opcao == "s":
                cls._sacar()
            elif opcao == "e":
                cls._extrato()
            elif opcao == "l":
                cls._listar_clientes()
            elif opcao == "p":
                cls._pesquisar_cliente()
            elif opcao == "q":
                break
            
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
                input("\nPressione Enter para continuar...")
                
# -------------------------------
# INÍCIO DO PROGRAMA
# -------------------------------
if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema._menu()
    