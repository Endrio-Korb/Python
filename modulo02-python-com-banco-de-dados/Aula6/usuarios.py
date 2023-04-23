from database import session, Base, engine
from models import Usuario, UsuarioPerfil

def criar_usuario(email, senha, nome, sexo):
    
    usuario = Usuario(
        email=email, senha=senha
    )

    session.add(usuario)
    session.commit()

    criar_perfil_usuario(usuario, nome, sexo)

def criar_perfil_usuario(usuario, nome, sexo):

    perfil_usuario = UsuarioPerfil(
    id=usuario.id,
    nome=nome,
    sexo=sexo
    )
    session.add(perfil_usuario)
    session.commit()


def lista_usuarios():

    # Consultador todos os registros (SELECT * FROM)
    resultado = session.query(Usuario).all()
    if len(resultado) == 0:
        print("Não há usuário cadastrados no sistema.")
    else:
        print("Usuário cadastrados")
        print("---------------------")
        for usuario in resultado:
            # SELECT * FROM tb_usuaios_perfis WHERE id = :id
            perfil = session.query(UsuarioPerfil).filter_by(id=usuario.id).first()

            print(f"Nome: {perfil.nome}")
            print(f"Sexo: {perfil.sexo}")
            print(f"Email: {usuario.email}")



if __name__ == "__main__":

    while True:

        print("Informe a opção desejada:")
        print("1 - Lista todos os usuários.")
        print("2 - Cadastrar um Usuário.")
        print("3 - Excluir um Usuário.")
        print("4 - Atulizar dados do Usuário.")
        print("5 - Sair.")

        opcao = int(input("OPÇÃO: "))

        if opcao == 1:
            lista_usuarios()

        elif opcao == 2:
            email = input("Informe o email do usuário: ")
            senha = input("Informe a senha do usuário: ")
            nome = input("Informe o nome do usuário: ")
            sexo = input("Infore o sexo do usuário: ")

            criar_usuario(email, senha, nome, sexo)