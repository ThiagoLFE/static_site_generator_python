from src.utils.generate_page import generate_page
from os import listdir, mkdir
from os.path import join, isfile

def load_pages(path_data, template_path, path_data_dst):
    # dentro do content path temos que fazer a lógica de adicionar diretórios e arquivos conforme necessidade e usar o generate_page() com o caminho completo de cada novo arquivo

    # Listar o que temos em content
    list_content_items =  listdir(path_data)

    for item in list_content_items:

        # caminho completo do arquivo/diretório
        full_content_path = join(path_data, item)
        full_dest_path = join(path_data_dst, item)

        # Se for arquivo adiciona a página formatada
        if isfile(full_content_path):
            full_dest_path = full_dest_path.replace(".md", ".html")
            generate_page(full_content_path, template_path, full_dest_path)
        
        #Se for diretório
        else:
            # criar diretório no caminho de destino
            mkdir(full_dest_path)

            # chamar gerate_page de recursivamente para verificar items internos
            load_pages(full_content_path, template_path, full_dest_path)