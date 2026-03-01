from src.copy_content import init
from src.utils.load_pages import load_pages
from os import getcwd
from os.path import join

def main():

    root_path = getcwd()
    content_path = join(root_path, "content")
    path_template = join(root_path, "template.html")
    dst_path = join(root_path, "public")    
    
 

    init()
    load_pages(content_path, path_template, dst_path)

main()
