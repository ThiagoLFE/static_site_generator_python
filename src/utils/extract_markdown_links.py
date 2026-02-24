REGEX_MD_IMAGE = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
REGEX_MD_LINK = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

import re
def extract_markdown_image(text):
        return re.findall(REGEX_MD_IMAGE, text)

def extract_markdown_link(text):
       return re.findall(REGEX_MD_LINK, text)



