from textnode import TextNode
from textnode import TextType

def main():
    dummy_obj = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy_obj)
main()