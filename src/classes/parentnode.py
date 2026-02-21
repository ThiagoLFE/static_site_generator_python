from static_site_generator_python.src.classes.htmlnode import HTMLNode
from static_site_generator_python.src.classes.leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        
        if not self.children:
            raise ValueError("Parent node must have at least a children")
        
        parsed_html = f"<{self.tag}>"
        if self.props:
            parsed_html = f"<{self.tag} {self.props_to_html()}>"

        for child in self.children:
                parsed_html += child.to_html()

        parsed_html += f"</{self.tag}>"

        return parsed_html
    