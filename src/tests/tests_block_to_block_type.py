import unittest
from src.utils.block_to_block_type import block_to_block_type
from src.utils.BlockType import BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_1(self):
        self.assertEqual(block_to_block_type("# Título"), BlockType.HEADING)

    def test_heading_6(self):
        self.assertEqual(block_to_block_type("###### Título"), BlockType.HEADING)

    def test_not_heading_without_space(self):
        self.assertEqual(block_to_block_type("###Título"), BlockType.PARAGRAPH)


    def test_not_code_block_without_newline_after_ticks(self):
        md = "```print('oi')\n```"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_quote_single_line(self):
        self.assertEqual(block_to_block_type("> citação"), BlockType.QUOTE)

    def test_quote_multi_line(self):
        md = "> a\n> b\n> c"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_not_quote_if_any_line_missing_prefix(self):
        md = "> a\nb"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        md = "- a\n- b\n- c"
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_not_unordered_list_if_any_line_wrong(self):
        md = "- a\n* b"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        md = "1. a\n2. b\n3. c"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_not_ordered_list_if_not_start_at_1(self):
        md = "2. a\n3. b"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_not_ordered_list_if_not_incrementing(self):
        md = "1. a\n3. b"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_paragraph_default(self):
        md = "isso é só um parágrafo\ncom duas linhas"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()