from os.path import exists, join, isfile
from os import getcwd, listdir, mkdir
from shutil import rmtree, copy

def init(path_dest):
    # Caminhos
    root_path = getcwd() 
    path_sources = join(root_path, "src")
    path_public = join(root_path, path_dest)
    path_static = join(path_sources, "static")

    # Se existir o caminho x tem que apagar o diretório inteiro (no mercy)
    if exists(path_public):

        # Da um tiro no diretório publico
        rmtree(path_public)

        # Criar diretório publico
        mkdir(path_public)

        # Copia diretório stático
        copy_content(path_static, path_public)
        
    else:
        # print("Inicializando Diretório")
        mkdir(path_public)
        copy_content(path_static, path_public)

def copy_content(current_path_static, current_path_public):

    # Acessar lista de conteudo no diretório estático
    # Valores iniciais, depois altera conforme a recursividade
    items_in_directory = listdir(current_path_static)

    # Verificar lista no diretorio se é um file
    for item in items_in_directory:
        path_item = join(current_path_static, item)
        destine_path = join(current_path_public, item)
        
        if isfile(path_item):
            # Copia arquivo do caminho atual para o caminho destino
            copy(path_item, destine_path)
            # Se file pegar o caminho atual e replica para o diretório publico
            # print(f"{item} adicionado com sucesso!")
            
        else:
            # Criar diretório faltante em public
            mkdir(destine_path)

            # Chama a função recursivamente varrendo a árvore
            copy_content(path_item, destine_path)

    # print("Site atualizado com sucesso!")
