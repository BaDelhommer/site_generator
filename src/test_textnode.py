import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("ligma", "iladies")
        node2 = TextNode("ligma", "boffa")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("ligma", "iladies", "deeznutz.nutz")
        node2 = TextNode("ligma", "iladies", "deeznutz.nutz")
        self.assertEqual(node, node2)

    def test_url_noteq(self):
        node = TextNode("ligma", "iladies", "deeznutz.nutz")
        node2 = TextNode("ligma", "iladies", "boffa.deeznutz")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("ligma", "i-ladies", "deez.nutz")
        self.assertEqual(
            "TextNode(ligma, i-ladies, deez.nutz)",
            repr(node)
        )


if __name__ == "__main__":
    unittest.main()
