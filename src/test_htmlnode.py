import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        target_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(target_string, node.props_to_html())

    def test_repr(self):
        node = HTMLNode()
        test_string = "HTMLNode(None, None, children: None, None)"
        self.assertEqual(test_string, repr(node))

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a pgraph")
        test_string = "<p>This is a pgraph</p>"
        self.assertEqual(node.to_html(), test_string)

    def test_to_html_props(self):
        node = LeafNode(tag="a", value="ClickMe", props={"href": "https://google.com", "target": "_blank"})
        test_string = '<a href="https://google.com" target="_blank">ClickMe</a>'
        self.assertEqual(node.to_html(), test_string)

class TestParentNode(unittest.TestCase):
    def test_parent_html(self):
        node = ParentNode(
        tag = "p",
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
        test_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), test_result)

    def test_headings(self):
        node = ParentNode(
            tag="h2",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
