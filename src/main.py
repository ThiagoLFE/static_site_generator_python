from src.classes.textnode import TextNode, TextType

def main():
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) Arroz com franguinho", TextType.TEXT)
    print(node)
    
main()