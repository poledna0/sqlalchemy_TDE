
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Adicionar Cliente
def adicionar_cliente():
    nome = input("Nome: ")
    comida_favorita = input("Comida Favorita: ")
    idade = int(input("Idade: "))
    dia_todo_mes_recebe = int(input("Dia do mês que recebe: "))
    endereco_completo = input("Endereço Completo: ")

    novo_cliente = Clientes(
        nome=nome, 
        comida_favorita=comida_favorita, 
        idade=idade, 
        dia_todo_mes_recebe=dia_todo_mes_recebe, 
        endereco_completo=endereco_completo
    )
    
    sessao.add(novo_cliente)
    sessao.commit()
    print(f"Cliente {nome} adicionado com sucesso!")

# Atualizar Cliente
def atualizar_cliente():
    nome_atualizar = input("Nome do cliente a ser atualizado: ")
    cliente = sessao.query(Clientes).filter_by(nome=nome_atualizar).first()

    if cliente:
        nova_comida_favorita = input(f"Nova comida favorita para {cliente.nome}: ")
        nova_idade = int(input(f"Nova idade para {cliente.nome}: "))
        
        cliente.comida_favorita = nova_comida_favorita
        cliente.idade = nova_idade
        
        sessao.commit()
        print(f"Cliente {cliente.nome} atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")

# Deletar Cliente
def deletar_cliente():
    nome_deletar = input("Nome do cliente a ser deletado: ")
    cliente = sessao.query(Clientes).filter_by(nome=nome_deletar).first()

    if cliente:
        sessao.delete(cliente)
        sessao.commit()
        print(f"Cliente {cliente.nome} deletado com sucesso!")
    else:
        print("Cliente não encontrado.")

# Visualizar Clientes
def visualizar_clientes():
    clientes = sessao.query(Clientes).all()
    for cliente in clientes:
        print(cliente)

# Adicionar Estoque
def adicionar_estoque():
    comida_estoque = input("Comida no estoque: ")
    quantidade = int(input("Quantidade: "))

    novo_estoque = Estoque(
        comida_estoque=comida_estoque, 
        quantidade=quantidade
    )
    
    sessao.add(novo_estoque)
    sessao.commit()
    print(f"Item {comida_estoque} adicionado ao estoque com sucesso!")

# Atualizar Estoque
def atualizar_estoque():
    comida_atualizar = input("Nome da comida no estoque a ser atualizada: ")
    estoque = sessao.query(Estoque).filter_by(comida_estoque=comida_atualizar).first()

    if estoque:
        nova_quantidade = int(input(f"Nova quantidade de {estoque.comida_estoque}: "))
        estoque.quantidade = nova_quantidade
        
        sessao.commit()
        print(f"Estoque de {estoque.comida_estoque} atualizado com sucesso!")
    else:
        print("Comida não encontrada no estoque.")

# Deletar Estoque
def deletar_estoque():
    comida_deletar = input("Nome da comida no estoque a ser deletada: ")
    estoque = sessao.query(Estoque).filter_by(comida_estoque=comida_deletar).first()

    if estoque:
        sessao.delete(estoque)
        sessao.commit()
        print(f"Item {estoque.comida_estoque} deletado do estoque com sucesso!")
    else:
        print("Comida não encontrada no estoque.")

# Visualizar Estoque
def visualizar_estoque():
    estoques = sessao.query(Estoque).all()
    for estoque in estoques:
        print(estoque)

# Adicionar Fornecedor
def adicionar_fornecedor():
    nome_empresa = input("Nome da empresa: ")
    telefone_empresa = input("Telefone da empresa: ")
    endereco_empresa = input("Endereço da empresa: ")
    cidade_empresa = input("Cidade da empresa: ")
    estado_empresa = input("Estado da empresa: ")
    cep_empresa = input("CEP da empresa: ")

    novo_fornecedor = Fornecedor(
        nome_empresa=nome_empresa, 
        telefone_empresa=telefone_empresa, 
        endereco_empresa=endereco_empresa, 
        cidade_empresa=cidade_empresa, 
        estado_empresa=estado_empresa, 
        cep_empresa=cep_empresa
    )
    
    sessao.add(novo_fornecedor)
    sessao.commit()
    print(f"Fornecedor {nome_empresa} adicionado com sucesso!")

# Atualizar Fornecedor
def atualizar_fornecedor():
    nome_atualizar = input("Nome do fornecedor a ser atualizado: ")
    fornecedor = sessao.query(Fornecedor).filter_by(nome_empresa=nome_atualizar).first()

    if fornecedor:
        novo_telefone = input(f"Novo telefone para {fornecedor.nome_empresa}: ")
        novo_endereco = input(f"Novo endereço para {fornecedor.nome_empresa}: ")
        
        fornecedor.telefone_empresa = novo_telefone
        fornecedor.endereco_empresa = novo_endereco
        
        sessao.commit()
        print(f"Fornecedor {fornecedor.nome_empresa} atualizado com sucesso!")
    else:
        print("Fornecedor não encontrado.")

# Deletar Fornecedor
def deletar_fornecedor():
    nome_deletar = input("Nome do fornecedor a ser deletado: ")
    fornecedor = sessao.query(Fornecedor).filter_by(nome_empresa=nome_deletar).first()

    if fornecedor:
        sessao.delete(fornecedor)
        sessao.commit()
        print(f"Fornecedor {fornecedor.nome_empresa} deletado com sucesso!")
    else:
        print("Fornecedor não encontrado.")

# Visualizar Fornecedores
def visualizar_fornecedores():
    fornecedores = sessao.query(Fornecedor).all()
    for fornecedor in fornecedores:
        print(fornecedor)

def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Adicionar Cliente")
        print("2. Atualizar Cliente")
        print("3. Deletar Cliente")
        print("4. Visualizar Clientes")
        print("5. Adicionar Estoque")
        print("6. Atualizar Estoque")
        print("7. Deletar Estoque")
        print("8. Visualizar Estoque")
        print("9. Adicionar Fornecedor")
        print("10. Atualizar Fornecedor")
        print("11. Deletar Fornecedor")
        print("12. Visualizar Fornecedores")
        print("13. Sair")

        escolha = input("Escolha uma opção (1-13): ")

        if escolha == '1':
            adicionar_cliente()
        elif escolha == '2':
            atualizar_cliente()
        elif escolha == '3':
            deletar_cliente()
        elif escolha == '4':
            visualizar_clientes()
        elif escolha == '5':
            adicionar_estoque()
        elif escolha == '6':
            atualizar_estoque()
        elif escolha == '7':
            deletar_estoque()
        elif escolha == '8':
            visualizar_estoque()
        elif escolha == '9':
            adicionar_fornecedor()
        elif escolha == '10':
            atualizar_fornecedor()
        elif escolha == '11':
            deletar_fornecedor()
        elif escolha == '12':
            visualizar_fornecedores()
        elif escolha == '13':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    # criando engine para o banco
    engine_banco = sqlalchemy.create_engine('sqlite:///bancohenrique.db', echo=True)

    # criando a base para os modelos
    Base_banc = declarative_base()

    # definindo o modelo Cliente
    class Clientes(Base_banc):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        nome = Column(String(50))
        comida_favorita = Column(String(60))
        idade = Column(Integer)
        dia_todo_mes_recebe = Column(Integer)
        endereco_completo = Column(String(50))

        def __repr__(self):
            return (f"<Clientes(id={self.id}, nome={self.nome}, comida_favorita={self.comida_favorita}, "
                    f"idade={self.idade}, dia_todo_mes_recebe={self.dia_todo_mes_recebe}, "
                    f"endereco_completo={self.endereco_completo})>")

    # Estoque da empresa batatatinha entrega
    class Estoque(Base_banc):
        __tablename__ = 'alimento_que_recebe'
        id = Column(Integer, primary_key=True)
        comida_estoque = Column(String(60))
        quantidade = Column(Integer)

        def __repr__(self):
            return (f"<Estoque(id={self.id}, comida_estoque={self.comida_estoque}, "
                    f"quantidade={self.quantidade})>")

    class Entrega(Base_banc):
        __tablename__ = 'batatinha_em_casa'
        id = Column(Integer, primary_key=True)
        cliente_id = Column(Integer, ForeignKey('users.id'))
        data_entrega_escolhida = Column(Integer)
        endereco_entrega = Column(String(100))

        cliente = relationship("Clientes")

        def __repr__(self):
            return (f"<Entrega(id={self.id}, cliente_id={self.cliente_id}, "
                    f"data_entrega_escolhida={self.data_entrega_escolhida}, "
                    f"endereco_entrega={self.endereco_entrega})>")
        
    class Fornecedor(Base_banc):
        __tablename__ = 'fornecedores'
        id = Column(Integer, primary_key=True)
        nome_empresa = Column(String(100))
        telefone_empresa = Column(String(20))
        endereco_empresa = Column(String(100))
        cidade_empresa = Column(String(50))
        estado_empresa = Column(String(50))
        cep_empresa = Column(String(10))

        def __repr__(self):
            return (f"<Fornecedor(id={self.id}, nome_empresa={self.nome_empresa}, telefone_empresa={self.telefone_empresa}, "
                    f"endereco_empresa={self.endereco_empresa}, cidade_empresa={self.cidade_empresa}, "
                    f"estado_empresa={self.estado_empresa}, cep_empresa={self.cep_empresa})>")

    # criando as tabelas no banco de dados
    Base_banc.metadata.create_all(engine_banco)

    # criando a sessão
    Sessao = sessionmaker(bind=engine_banco)
    sessao = Sessao()

    menu_principal()

# instanciando e adicionando clientes
# clientes = [
#     Clientes(nome='Henrique', comida_favorita='todas as batatas', idade=30, dia_todo_mes_recebe=15, endereco_completo='Rua das Flores, 123'),
#     Clientes(nome='Pedro', comida_favorita='feijão', idade=25, dia_todo_mes_recebe=10, endereco_completo='Avenida Brasil, 456'),
#     Clientes(nome='Mari', comida_favorita='temaki', idade=28, dia_todo_mes_recebe=20, endereco_completo='Rua da Praia, 789'),
#     Clientes(nome='Eduardo', comida_favorita='bis', idade=23, dia_todo_mes_recebe=26, endereco_completo='Avenida Central, 2222')
# ]

# sessao.add_all(clientes)
# sessao.commit()

# # adicionando estoque
# estoques = [
#     Estoque(comida_estoque='batata', quantidade=123),
#     Estoque(comida_estoque='bis', quantidade=23),
#     Estoque(comida_estoque='tomate', quantidade=10),
#     Estoque(comida_estoque='temaki', quantidade=42),
#     Estoque(comida_estoque='feijão', quantidade=765),
#     Estoque(comida_estoque='farinha de trigo', quantidade=29),
#     Estoque(comida_estoque='cerveja', quantidade=92)
# ]

# sessao.add_all(estoques)
# sessao.commit()

# # recuperando IDs dos clientes recém-criados
# pedro = sessao.query(Clientes).filter_by(nome='Pedro').first()
# mari = sessao.query(Clientes).filter_by(nome='Mari').first()
# eduardo = sessao.query(Clientes).filter_by(nome='Eduardo').first()

# # adicionando entregas
# entregas = [
#     Entrega(cliente_id=pedro.id, data_entrega_escolhida=pedro.dia_todo_mes_recebe),
#     Entrega(cliente_id=mari.id, data_entrega_escolhida=mari.dia_todo_mes_recebe),
#     Entrega(cliente_id=eduardo.id, data_entrega_escolhida=eduardo.dia_todo_mes_recebe),
# ]

# sessao.add_all(entregas)
# sessao.commit()

# # adicionando fornecedores
# fornecedores = [
#     Fornecedor(
#         nome_empresa='omicrom joao',
#         telefone_empresa='1111-1111',
#         endereco_empresa='Rua dos Fornecedores, 100',
#         cidade_empresa='São Paulo',
#         estado_empresa='SP',
#         cep_empresa='01234-567'
#     ),
#     Fornecedor(
#         nome_empresa='Fornecedor ABC',
#         telefone_empresa='2222-2222',
#         endereco_empresa='Avenida Central, 200',
#         cidade_empresa='Rio de Janeiro',
#         estado_empresa='RJ',
#         cep_empresa='87654-321'
#     ),
#     Fornecedor(
#         nome_empresa='Fornecedor DEF',
#         telefone_empresa='22222-2222',
#         endereco_empresa='Rua das Indústrias, 300',
#         cidade_empresa='Belo Horizonte',
#         estado_empresa='MG',
#         cep_empresa='123456-1234'
#     )
# ]

# sessao.add_all(fornecedores)
# sessao.commit()

# # Consulta
# consulta_usuario = sessao.query(Clientes).filter_by(nome='Mari').first()
# print(consulta_usuario)

# for instance in sessao.query(Clientes).order_by(Clientes.id):
#     print(instance.nome, instance.comida_favorita, instance.idade)

# # Update
# usuario_atualiza = sessao.query(Clientes).filter_by(nome='Pedro').first()
# usuario_atualiza.comida_favorita = "sushi"
# usuario_atualiza.idade = 26  
# sessao.commit()

# for instance in sessao.query(Clientes).order_by(Clientes.id):
#     print(instance.nome, instance.comida_favorita, instance.idade)

# # Deletar
# pessoa_delet = sessao.query(Clientes).filter_by(nome='Henrique').first()
# sessao.delete(pessoa_delet)
# sessao.commit()

# # contar quantos Henrique tem no banco
# contador_henrique = sessao.query(Clientes).filter_by(nome='Henrique').count()
# print(f"Quantidade de usuários com o nome 'Henrique': {contador_henrique}")
