from .htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):

        if self.value == None:
            # to debbug error
            print("=-"* 20)
            print("DEBUG ERROR LeafNode sem valor:")
            print("tag:", self.tag)
            print("props:", self.props)
            print("value:", self.props)
            print("children:", self.children)
            print("=-"* 20)
            
            raise ValueError("All leaf nodes must have a value.")
        
        if not self.tag:
            return self.value
        
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"