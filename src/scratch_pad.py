from markdown_blocks import markdown_to_blocks

print(markdown_to_blocks(
    """This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
    This is the same paragraph on a new line

    * This is a list
    * with items"""
))