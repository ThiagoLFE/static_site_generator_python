import unittest

from static_site_generator_python.src.classes.leafnode import LeafNode
from static_site_generator_python.src.classes.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>'
        )

    def test_to_html_with_multiple_props(self):
        child_node = LeafNode("p", "Hello")
        parent_node = ParentNode("div", [child_node], {"id": "main", "class": "wrapper"})
        # Nota: a ordem dos atributos pode variar dependendo da sua implementação
        self.assertIn('id="main"', parent_node.to_html())
        self.assertIn('class="wrapper"', parent_node.to_html())

    def test_nested_parent_with_props(self):
        grandchild = LeafNode("b", "bold text")
        child = ParentNode("p", [grandchild], {"class": "paragraph"})
        parent = ParentNode("div", [child], {"id": "container"})
        self.assertEqual(
            parent.to_html(),
            '<div id="container"><p class="paragraph"><b>bold text</b></p></div>'
        )

if __name__ == "__main__":
    unittest.main()