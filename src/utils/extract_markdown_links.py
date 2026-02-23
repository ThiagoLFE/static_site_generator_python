REGEX_MD_IMAGE = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
REGEX_MD_LINK = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

import re
def extract_markdown_images(text):
        return re.findall(REGEX_MD_IMAGE, text)

def extract_markdown_links(text):
       return re.findall(REGEX_MD_LINK, text)



