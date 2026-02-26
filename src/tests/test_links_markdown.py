import unittest
from src.utils.extract_markdown_links import extract_markdown_image, extract_markdown_link

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_image(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_image(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_link(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_links_not_images(self):
        # Garante que extract_markdown_links NÃO capture imagens
        text = "This is an ![image](https://url.com/img.png) and a [link](https://boot.dev)"
        matches = extract_markdown_link(text)
        self.assertListEqual([("link", "https://boot.dev")], matches)

    def test_extract_markdown_no_matches(self):
        text = "Este texto não tem links nem imagens."
        self.assertEqual(extract_markdown_image(text), [])
        self.assertEqual(extract_markdown_link(text), [])