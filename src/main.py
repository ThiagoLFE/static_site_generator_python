from src.classes.textnode import TextNode, TextType
from src.copy_content import init
from src.utils.generate_page import generate_page
from os import getcwd
from os.path import join

def main():
    root_path = getcwd()
    markdown_path = join(join(root_path, "content"), "index.md")
    path_template = join(root_path, "template.html")
    dst_path = join(join(root_path, "public"), "index.html")

    init()
    generate_page(markdown_path, path_template, dst_path)
main()