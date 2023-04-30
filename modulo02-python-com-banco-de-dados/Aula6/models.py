#Classe que será herdada nas nossas models
from database import Base

# Tipos das colunas que serão criadas na tabela mapeada
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, func, Table

from sqlalchemy.orm import relationship

postagens_categorias = Table(
    "tb_postagens_categorias", Base.metadata,
    Column("postagem_id", Integer, ForeignKey("tb_postagem.id"), primary_key=True ),
    Column("categoria_id", Integer, ForeignKey("tb_categorias.id"), primary_key=True)
)


class Usuario(Base):
    
    # O atributo _tablename_ indica  nome da tabela que será criada
    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key = True, autoincrement = True)
    email = Column(String(100), nullable= False)
    senha = Column(String(100), nullable= False)

    # Atributos do tipo relationship fazem a ligação entre os objetos que representam as tabelas que possuem relacionamento
    # Esse campo não existira fisicamente no banco de dados

    # Primeiro argumento: Nome da classe relacional <UsuarioPerfil>
    # back_populates: Representa o campo de ligação no objeto relaional
    # userlist: Indicamos se queremos trazer uma lista de objetos relacionados ou não
    perfil = relationship("UsuarioPerfil",back_populates="usuario", uselist=False)

    def __repr__(self):
        return f"<Usuario>{self.email}"

class UsuarioPerfil(Base):

    __tablename__ = "tb_usuarios_perfis"
    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(200), nullable=False)
    sexo = Column(String(1), nullable=False)

    # Como a relação é de 1:1, uselist será False pois apenas 1 registro será retornado.
    usuario = relationship("Usuario", back_populates="perfil", uselist=False)

    # Como UsuarioPerfil tem uma relação de 1:N com Postagem, uselist será True. Pois o valor retornado
    # pode ser uma lista vaia, ou uma lista com 1 ou mais registros.
    postagens = relationship("Postagem", back_populates="usuario", uselist=True)
    comentarios = relationship("Comentario", back_populates="usuario", uselist=True)

class Postagem(Base):

    __tablename__ = "tb_postagem"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("tb_usuarios_perfis.id"), nullable=False)
    titulo = Column(String(200), nullable=False)
    corpo = Column(Text, nullable=False)
    data_hora = Column(DateTime, default=func.now)  

    usuario = relationship("UsuarioPerfil", back_populates="postagens", uselist=False)
    categorias = relationship("Categoria", secondary=postagens_categorias, back_populates="postagens",uselist=True)
    comentarios = relationship("Comentario", back_populates="postagem", uselist=True)

class Categorias(Base):

    __tablename__ = "tb_categorias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    # Quando temos uma relação de N:N obrigatoriamente precisamos criar uma tabela associativa, para relacionar os objetos que
    # representam essas tabelas, precisamos passar o argumento secondary para a função relationship, dessa maneira conseguimos
    # relacionar os objetos.
    postagens = relationship("Postagem", secondary=postagens_categorias, back_populates="categorias", uselist=True)

class Comentario(Base):

    __tablename__ = "tb_comentarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("tb_usuarios_perfis.id"), nullable=False)
    postagem_id = Column(Integer, ForeignKey("tb_postagem.id"), nullable=False)
    texto = Column(String(200), nullable=False)
    data_hora = Column(DateTime, default=func.now)

    usuario = relationship("UsuarioPerfil", back_populates="comentarios", uselist=False)
    postagem = relationship("Postagem", back_populates="comentarios", uselist=False)

class Log(Base):

    __tablename__ = "tb_logs"

    id = Column(Integer, primary_key=True,autoincrement=True)
    log = Column(Text,nullable=False)