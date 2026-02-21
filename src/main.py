from static_site_generator_python.src.classes.textnode import TextNode
from static_site_generator_python.src.classes.textnode import TextType

def main():
    dummy_obj = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy_obj)
main()