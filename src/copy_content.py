from os.path import exists, join
from os import getcwd, listdir

def tests():
    # caminhos
    root_path = getcwd() 
    path_sources = join(root_path, "src")
    path_public = join(root_path, "public")

    # Visualizar diretórios do sources
    listdir(path_sources)

    # verificar se um diretório existe ou não
    print(f"caminho: {path_public}")

    # Se existir o caminho x tem que apagar o diretório inteiro (no mercy)
    if exists(path_public):
        print("Achei o publico!!!")
        # Arrancar o diretório
    else:
        print("Num achei o public")
        