import unittest
from src.classes.textnode import TextNode, TextType
from src.utils.split_nodes import split_nodes_image, split_nodes_link


class TestParentNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "Welcome to the [kitchen master website](https://kitchenmasterwebsite) see our most famous recipe [white cake](https://thebestwhitecakeofwholeworld) he is the best",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Welcome to the ", TextType.TEXT),
                TextNode("kitchen master website", TextType.LINK, "https://kitchenmasterwebsite"),
                TextNode(" see our most famous recipe ", TextType.TEXT),
                TextNode(
                    "white cake", TextType.LINK, "https://thebestwhitecakeofwholeworld"
                ),
                TextNode(" he is the best", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_link_on_start(self):
        node = TextNode(
            "[Click on me](evilsite) you enter a random site, trust click on this link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Click on me", TextType.LINK, "evilsite"),
                TextNode(" you enter a random site, trust click on this link", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_on_start(self):
        node = TextNode(
            "![evil image](evilimage.png) you enter a random site, trust click on this beautifull image",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("evil image", TextType.IMAGE, "evilimage.png"),
                TextNode(" you enter a random site, trust click on this beautifull image", TextType.TEXT),
            ],
            new_nodes,
        )
    
    