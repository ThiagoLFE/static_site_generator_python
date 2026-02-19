from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        
        if not self.children:
            raise ValueError("Parent node must have at least a children")
        
        parsed_html = f"<{self.tag}>"

        for children in self.children:

            if children is isinstance(children, ParentNode):
                parsed_html += children.to_html()

            if children is isinstance(children, LeafNode):
                parsed_html += children.to_html()
        
        parsed_html += f"</{self.tag}>"
        
        return parsed_html