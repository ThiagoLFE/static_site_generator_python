def markdown_to_blocks(raw_markdown_string):
    markdown = raw_markdown_string.replace("\r\n", "\n")
    separated_blocks = markdown.split('\n\n')
    new_blocks = []
    for block in separated_blocks:
        if block.strip() == "":
            continue
        new_blocks.append(block.strip())
    return new_blocks