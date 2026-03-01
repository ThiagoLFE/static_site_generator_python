from src.utils.markdown_to_html_node import markdown_to_html_node
from src.utils.extract_title import extract_title
from os import makedirs
from os.path import exists, dirname, join, basename

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Pegando informações do markdown + template para injetar blocos html.
    md_file = open(from_path, "r").read()
    template = open(template_path, "r").read()
    
    # Criando os nós html
    html_node = markdown_to_html_node(md_file)

    # transformando em string de html
    content_html = html_node.to_html()

    # informação do título da página
    title = extract_title(md_file)

    # Formatando template com as informações do markdown
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content_html)

    # Pegando informações do caminho de destino da página a ser gerada
    directory_dst_name = dirname(dest_path)
    file_name = basename(dest_path)
    
    # Cria caminho se não existir
    makedirs(directory_dst_name, exist_ok=True)

    # Caminho completo do arquivo a ser gerado
    full_path = join(directory_dst_name, file_name)

    # Criando arquivo dentro da  pasta correta
    new_page = open(full_path, "w")
    
    # Adicionando o conteúdo formatado no arquivo
    new_page.write(template)

    new_page.close()
