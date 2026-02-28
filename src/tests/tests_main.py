import unittest
from src.utils.markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node1(self):
        # Teste de Parágrafo e Título
        md = """
# Este é um título

Este é um parágrafo com **negrito**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Este é um título</h1><p>Este é um parágrafo com <b>negrito</b></p></div>"
        )

    def test_quote(self):
        # Teste de Citação (Múltiplas linhas)
        md = """
> Citação linha 1
> Citação linha 2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Note que não deve haver espaços extras no início do texto
        self.assertEqual(
            html,
            "<div><blockquote>Citação linha 1 Citação linha 2</blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        )

    def test_markdown_to_html_node2(self):
        md = """
# Este é um título

Este é um parágrafo com **negrito** e _itálico_.

> Esta é uma citação
> que ocupa duas linhas

* Item de lista 1
* Item de lista 2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        
        # Verificando a estrutura geral
        self.assertTrue(html.startswith("<div>"))
        self.assertTrue(html.endswith("</div>"))
        self.assertIn("<h1>Este é um título</h1>", html)
        self.assertIn("<p>Este é um parágrafo com <b>negrito</b> e <i>itálico</i>.</p>", html)
        self.assertIn("<blockquote>Esta é uma citação que ocupa duas linhas</blockquote>", html)
        self.assertIn("<ul><li>Item de lista 1</li><li>Item de lista 2</li></ul>", html)

    def test_complex_ordered_list(self):
        md = """
1. Primeiro item com `código`
2. Segundo item com [link](https://boot.dev)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ol><li>Primeiro item com <code>código</code></li><li>Segundo item com <a href="https://boot.dev">link</a></li></ol></div>'
        self.assertEqual(html, expected)


    def test_codeblock_no_inline_parsing(self):
        md = """```
- linha 1 com **bold**
- linha 2 com _italic_ e `code`
- linha 3 com [link](https://example.com)
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>linha 1 com **bold**\nlinha 2 com _italic_ e `code`\nlinha 3 com [link](https://example.com)\n</code></pre></div>",
        )

    def test_headers_levels(self):
        md = "### Título 3\n\n###### Título 6"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<h3>Título 3</h3>", html)
        self.assertIn("<h6>Título 6</h6>", html)