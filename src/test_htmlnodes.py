import unittest

from htmlnode import HTMLNode 


class TestHtmlNode(unittest.TestCase):

    def test_raise_error_into_to_html(self):
        htmlNode = HTMLNode("p", "Make pudim", None, None)
        with self.assertRaises(NotImplementedError):
            htmlNode.to_html()

    def test_props_working(self):
        htmlNode = HTMLNode("img", None, None, {
    "href": "https://www.google.com",
    "target": "_blank",
})

if __name__ == "__main__":
    unittest.main()