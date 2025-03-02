import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_attributes(self):
        node = HTMLNode(
            tag='a',
            value='Google',
            props={'href': 'https://www.google.com', 'target': '_blank'}
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_without_attributes(self):
        node = HTMLNode(tag='p', value='Hello World')
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_not_implemented(self):
        node = HTMLNode(tag='div', value='Test')
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode(tag='p', value='Paragraph', props={'class': 'text'})
        rep = repr(node)
        self.assertIn("HTMLNode", rep)
        self.assertIn("tag='p'", rep)
        self.assertIn("value='Paragraph'", rep)
        self.assertIn("props={'class': 'text'}", rep)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == '__main__':
    unittest.main()


