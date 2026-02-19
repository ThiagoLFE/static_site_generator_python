import unittest
from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("this is a link text node", TextType.LINK)
        node2 = TextNode("this is a italic text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_is_instance(self):
        node1 = TextNode("this is a link text node", TextType.LINK)
        self.assertIsInstance(node1, TextNode)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main()