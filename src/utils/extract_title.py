def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.split("#", 1)[1].strip()
    
    raise Exception("Markdown file must be a header (# Títle)")
    