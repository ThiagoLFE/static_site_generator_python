from src.utils.extract_title import extract_title
import unittest

class TestExtract_title(unittest.TestCase):

    def test_extract_title(self):
        md = """
# Um Titulo Tituloso

Alguns textos so pra fingir que se trata de um arquivo markdown veridico e funcional.
"""

        self.assertEqual(extract_title(md), "Um Titulo Tituloso")

    def test_extract_title2(self):
        self.assertAlmostEqual(extract_title("# Hello"), "Hello")
if __name__ == "__main__":
    unittest.main()