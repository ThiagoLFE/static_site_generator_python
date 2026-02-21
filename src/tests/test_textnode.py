import unittest
from static_site_generator_python.src.classes.textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()