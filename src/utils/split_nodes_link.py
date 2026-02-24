from src.classes.textnode import TextNode, TextType
from src.utils.extract_markdown_links import extract_markdown_link, extract_markdown_image
import re

REGEX_MD_IMAGE = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
REGEX_MD_LINK = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def split_nodes_link(nodes_list):
    new_nodes = []

    for node in nodes_list:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if not re.search(REGEX_MD_LINK, node.text):
            new_nodes.append(node)
            continue

        texto_restante = node.text
        separadores = extract_markdown_link(texto_restante)

        for separador in separadores:
            texto_separador = f"[{separador[0]}]({separador[1]})" 
            partes = texto_restante.split(texto_separador, 1)
            anterior = partes[0]
            posterior = partes[1]

            if not anterior == "":
                new_nodes.append(TextNode(anterior, TextType.TEXT))
                new_nodes.append(TextNode(separador[0], TextType.LINK, separador[1]))
                texto_restante = posterior
            
        if len(texto_restante) > 0:
            new_nodes.append(TextNode(texto_restante, TextType.TEXT)) 
            
        
    return new_nodes

def split_nodes_image(nodes_list):
    new_nodes = []

    for node in nodes_list:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if not re.search(REGEX_MD_IMAGE, node.text):
            new_nodes.append(node)
            continue

        texto_restante = node.text
        separadores = extract_markdown_image(texto_restante) # Me retorna uma lista [(texto alternativo imagem, link imagem)]

        for separador in separadores:
            texto_separador = f"![{separador[0]}]({separador[1]})" 
            partes = texto_restante.split(texto_separador, 1)
            anterior = partes[0]
            posterior = partes[1]

            if not anterior == "":
                new_nodes.append(TextNode(anterior, TextType.TEXT))
            new_nodes.append(TextNode(separador[0], TextType.IMAGE, separador[1]))
            texto_restante = posterior
            
        if len(texto_restante) > 0:
            new_nodes.append(TextNode(texto_restante, TextType.TEXT)) 
            
        
    return new_nodes