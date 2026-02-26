import unittest
from src.classes.textnode import TextNode, TextType
from src.utils.text_to_textnodes import text_to_textnodes



class TestTextToTextNodesExtra(unittest.TestCase):
    def test_plain_text(self):
        self.assertEqual(
            text_to_textnodes("just text"),
            [TextNode("just text", TextType.TEXT)],
        )

    def test_only_bold(self):
        self.assertEqual(
            text_to_textnodes("**bold**"),
            [TextNode("bold", TextType.BOLD)],
        )

    def test_only_italic(self):
        self.assertEqual(
            text_to_textnodes("_it_"),
            [TextNode("it", TextType.ITALIC)],
        )

    def test_only_code(self):
        self.assertEqual(
            text_to_textnodes("`x = 1`"),
            [TextNode("x = 1", TextType.CODE)],
        )

    def test_adjacent_formats(self):
        self.assertEqual(
            text_to_textnodes("**b**_i_`c`"),
            [
                TextNode("b", TextType.BOLD),
                TextNode("i", TextType.ITALIC),
                TextNode("c", TextType.CODE),
            ],
        )

    def test_link_only(self):
        self.assertEqual(
            text_to_textnodes("[boot](https://boot.dev)"),
            [TextNode("boot", TextType.LINK, "https://boot.dev")],
        )

    def test_image_only(self):
        self.assertEqual(
            text_to_textnodes("![alt](https://img.com/a.png)"),
            [TextNode("alt", TextType.IMAGE, "https://img.com/a.png")],
        )

    def test_mix_image_link_and_text(self):
        self.assertEqual(
            text_to_textnodes("a ![x](u) b [y](v) c"),
            [
                TextNode("a ", TextType.TEXT),
                TextNode("x", TextType.IMAGE, "u"),
                TextNode(" b ", TextType.TEXT),
                TextNode("y", TextType.LINK, "v"),
                TextNode(" c", TextType.TEXT),
            ],
        )