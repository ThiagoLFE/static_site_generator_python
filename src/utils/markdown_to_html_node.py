from src.utils.split_nodes import split_nodes_link, split_nodes_image
from src.utils.inline_markdown import split_nodes_delimiter
from src.utils.markdown_to_blocks import markdown_to_blocks
from src.utils.block_to_block_type import block_to_block_type
from src.utils.BlockType import BlockType
from src.classes.textnode import text_node_to_html_node
from src.classes.parentnode import ParentNode
from src.classes.leafnode import LeafNode
from src.utils.text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)

        html_node = create_html_node(block, block_type)
        html_nodes.append(html_node) 

    return ParentNode("div", html_nodes)
    

def create_html_node(block, block_type):
        match block_type:
            case BlockType.PARAGRAPH:
                childrens_nodes = text_to_children(block.replace("\n", " "))
                return ParentNode("p", childrens_nodes)
            case BlockType.HEADING:
                numbers_hash = len(block.split(" ", 1)[0])
                raw_header = block[numbers_hash:].strip()
                childrens_nodes = text_to_children(raw_header)
                return ParentNode(f"h{numbers_hash}", childrens_nodes)
            case BlockType.CODE:
                raw_block = block.split("```")[1]
                if raw_block.startswith("\n"):
                    raw_block = raw_block[1:]
                children = ParentNode("code", [LeafNode(None, raw_block)])
                return ParentNode("pre", [children])
            case BlockType.QUOTE:
                raw_list_quote = []
                for line in block.split("\n"):
                    raw_line = line.split(">")[1].strip()
                    raw_list_quote.append(raw_line)
                childrens_nodes = text_to_children(" ".join(raw_list_quote))
                return ParentNode("blockquote", childrens_nodes)
            case BlockType.UNORDERED_LIST:
                formatted_lines = []
                for line in block.split("\n"):
                    childrens_nodes = []
                    raw_line = ""
                    if "-" in line:
                        raw_line = line.split("-", 1)[1].strip()
                    elif "*" in line:
                        raw_line = line.split("*", 1)[1].strip()
                    else:
                        raise Exception("Not found any character to represent a list")
                    childrens_nodes = text_to_children(raw_line)
                    formatted_lines.append( ParentNode("li", childrens_nodes ) )
                return ParentNode("ul", formatted_lines)
            case BlockType.ORDERED_LIST:
                formatted_lines = []
                i = 1
                for line in block.split("\n"):
                    childrens_nodes = []
                    raw_line = line.split(f"{i}.", 1)[1].strip()
                    childrens_nodes = text_to_children(raw_line)
                    formatted_lines.append( ParentNode("li", childrens_nodes ) )
                    i +=1 # To keeping track each line
                return ParentNode("ol", formatted_lines)
            
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    childrens = []
    for node in text_nodes:
        childrens.append(text_node_to_html_node(node))
    return childrens