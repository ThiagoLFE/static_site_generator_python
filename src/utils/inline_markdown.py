from src.classes.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for i in range (len(old_nodes)):

        if old_nodes[i].text_type != TextType.TEXT:
            new_nodes.append(old_nodes[i])
            continue
        
        parts = old_nodes[i].text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed") 

        for j in range(len(parts)):
            if parts[j] == "":
                continue
            if j % 2 == 0:
                new_nodes.append(TextNode(parts[j], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[j], text_type))
            
    return new_nodes