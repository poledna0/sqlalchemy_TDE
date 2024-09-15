import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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

# instanciando e adicionando clientes
clientes = [
    Clientes(nome='Henrique', comida_favorita='todas as batatas', idade=30, dia_todo_mes_recebe=15, endereco_completo='Rua das Flores, 123'),
    Clientes(nome='Pedro', comida_favorita='feijão', idade=25, dia_todo_mes_recebe=10, endereco_completo='Avenida Brasil, 456'),
    Clientes(nome='Mari', comida_favorita='temaki', idade=28, dia_todo_mes_recebe=20, endereco_completo='Rua da Praia, 789'),
    Clientes(nome='Eduardo', comida_favorita='bis', idade=23, dia_todo_mes_recebe=26, endereco_completo='Avenida Central, 2222')
]

sessao.add_all(clientes)
sessao.commit()

# adicionando estoque
estoques = [
    Estoque(comida_estoque='batata', quantidade=123),
    Estoque(comida_estoque='bis', quantidade=23),
    Estoque(comida_estoque='tomate', quantidade=10),
    Estoque(comida_estoque='temaki', quantidade=42),
    Estoque(comida_estoque='feijão', quantidade=765),
    Estoque(comida_estoque='farinha de trigo', quantidade=29),
    Estoque(comida_estoque='cerveja', quantidade=92)
]

sessao.add_all(estoques)
sessao.commit()

# recuperando IDs dos clientes recém-criados
pedro = sessao.query(Clientes).filter_by(nome='Pedro').first()
mari = sessao.query(Clientes).filter_by(nome='Mari').first()
eduardo = sessao.query(Clientes).filter_by(nome='Eduardo').first()

# adicionando entregas
entregas = [
    Entrega(cliente_id=pedro.id, data_entrega_escolhida=pedro.dia_todo_mes_recebe),
    Entrega(cliente_id=mari.id, data_entrega_escolhida=mari.dia_todo_mes_recebe),
    Entrega(cliente_id=eduardo.id, data_entrega_escolhida=eduardo.dia_todo_mes_recebe),
]

sessao.add_all(entregas)
sessao.commit()

# adicionando fornecedores
fornecedores = [
    Fornecedor(
        nome_empresa='omicrom joao',
        telefone_empresa='1111-1111',
        endereco_empresa='Rua dos Fornecedores, 100',
        cidade_empresa='São Paulo',
        estado_empresa='SP',
        cep_empresa='01234-567'
    ),
    Fornecedor(
        nome_empresa='Fornecedor ABC',
        telefone_empresa='2222-2222',
        endereco_empresa='Avenida Central, 200',
        cidade_empresa='Rio de Janeiro',
        estado_empresa='RJ',
        cep_empresa='87654-321'
    ),
    Fornecedor(
        nome_empresa='Fornecedor DEF',
        telefone_empresa='22222-2222',
        endereco_empresa='Rua das Indústrias, 300',
        cidade_empresa='Belo Horizonte',
        estado_empresa='MG',
        cep_empresa='123456-1234'
    )
]

sessao.add_all(fornecedores)
sessao.commit()

# Consulta
consulta_usuario = sessao.query(Clientes).filter_by(nome='Mari').first()
print(consulta_usuario)

for instance in sessao.query(Clientes).order_by(Clientes.id):
    print(instance.nome, instance.comida_favorita, instance.idade)

# Update
usuario_atualiza = sessao.query(Clientes).filter_by(nome='Pedro').first()
usuario_atualiza.comida_favorita = "sushi"
usuario_atualiza.idade = 26  
sessao.commit()

for instance in sessao.query(Clientes).order_by(Clientes.id):
    print(instance.nome, instance.comida_favorita, instance.idade)

# Deletar
pessoa_delet = sessao.query(Clientes).filter_by(nome='Henrique').first()
sessao.delete(pessoa_delet)
sessao.commit()

# contar quantos Henrique tem no banco
contador_henrique = sessao.query(Clientes).filter_by(nome='Henrique').count()
print(f"Quantidade de usuários com o nome 'Henrique': {contador_henrique}")
