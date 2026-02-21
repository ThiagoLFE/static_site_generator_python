# def test_delim_bold(self):
#     node = TextNode("This is text with a **bolded** word", TextType.TEXT)
#     new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
#     self.assertListEqual(
#         [
#             TextNode("This is text with a ", TextType.TEXT),
#             TextNode("bolded", TextType.BOLD),
#             TextNode(" word", TextType.TEXT),
#         ],
#         new_nodes,
#     )

# from textnode import TextNode
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return ""