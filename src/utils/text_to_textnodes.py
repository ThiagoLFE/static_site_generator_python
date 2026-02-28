from src.classes.textnode import TextType, TextNode
from src.utils.inline_markdown import split_nodes_delimiter
from src.utils.split_nodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    split_images = split_nodes_image([TextNode(text, TextType.TEXT)])
    split_links = split_nodes_link(split_images)
    inline_text_bold = split_nodes_delimiter(split_links, "**", TextType.BOLD)
    inline_text_italic = split_nodes_delimiter(inline_text_bold, "_", TextType.ITALIC)
    inline_text_code = split_nodes_delimiter(inline_text_italic, "`", TextType.CODE)
    
    return inline_text_code

    

