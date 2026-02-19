import unittest

from htmlnode import HTMLNode 


class TestHtmlNode(unittest.TestCase):

    def test_raise_error_into_to_html(self):
        htmlNode = HTMLNode("p", "Make pudim", None, None)
        with self.assertRaises(NotImplementedError):
            htmlNode.to_html()

    def test_props_working(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        htmlNode = HTMLNode("img", None, None, props)

        res_of_method = htmlNode.props_to_html()
        expected_res =  "href=\"https://www.google.com\" target=\"_blank\""

        self.assertEqual(res_of_method, expected_res)

    def test_without_props_and_using_to_props_method(self):

        htmlNode = HTMLNode("img", None, None, None)

        res_of_method = htmlNode.props_to_html()
        expected_res =  ""

        self.assertEqual(res_of_method, expected_res)



if __name__ == "__main__":
    unittest.main()