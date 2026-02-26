import unittest

from src.utils.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocksHarder(unittest.TestCase):
    def test_leading_trailing_newlines_ignored(self):
        md = """


# Title


Paragraph text


"""
        self.assertEqual(markdown_to_blocks(md), ["# Title", "Paragraph text"])

    def test_multiple_blank_lines_collapse(self):
        md = """A


B



C"""
        self.assertEqual(markdown_to_blocks(md), ["A", "B", "C"])

    def test_strips_whitespace_around_each_block(self):
        md = """   A trimmed block   \n\n\t\tB trimmed too\t"""
        self.assertEqual(markdown_to_blocks(md), ["A trimmed block", "B trimmed too"])

    def test_preserves_single_newlines_inside_block(self):
        md = """Line 1
Line 2
Line 3"""
        self.assertEqual(markdown_to_blocks(md), ["Line 1\nLine 2\nLine 3"])

    def test_ignores_blocks_that_are_only_whitespace(self):
        md = "A\n\n   \n\n\t\n\nB"
        self.assertEqual(markdown_to_blocks(md), ["A", "B"])

    def test_windows_newlines(self):
        md = "A\r\n\r\nB\r\n\r\nC"
        self.assertEqual(markdown_to_blocks(md), ["A", "B", "C"])

    def test_list_block_with_blank_lines_between_blocks(self):
        md = """- a
- b


- c
- d"""
        self.assertEqual(markdown_to_blocks(md), ["- a\n- b", "- c\n- d"])


if __name__ == "__main__":
    unittest.main()