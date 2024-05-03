from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text_node1 = TextNode("jeff", "bold", "boot.dev")
    text_node2 = TextNode("jeff", "bold", "boot.dev")
    text_node3 = TextNode("John", "italics", "bootdev.com")

    html_node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})

    print(html_node.props_to_html())

    print(text_node1.__repr__)
    print(text_node1.__eq__(text_node2))
    print(text_node1.__eq__(text_node3))


if __name__ == "__main__":
    main()