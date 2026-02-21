import unittest

from static_site_generator_python.src.classes.leafnode import LeafNode

class testLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_without_value_and_tries_to_parse_html(self):
        with self.assertRaises(ValueError):
            html_content = LeafNode("p", None, None).to_html()
    

if __name__ == "__main__":
    unittest.main()