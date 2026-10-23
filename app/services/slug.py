import re

def slugify(titre: str) -> str:
    lowerTitle = titre.lower()
    replaced = re.sub(r'\W+', '-', lowerTitle)
    return replaced