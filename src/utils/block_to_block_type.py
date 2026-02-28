import re
from src.utils.BlockType import BlockType

def block_to_block_type(block):
    lines = block.split("\n")
    
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">") or block.startswith("> "):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH 
        return BlockType.QUOTE
    
    if block.startswith("- ") or block.startswith("* "):
        if block.startswith("- "):
            for line in lines:
                if not line.startswith("- "):
                    return BlockType.PARAGRAPH
        else:
            for line in lines:
                if not line.startswith("* "):
                        return BlockType.PARAGRAPH
            
        return BlockType.UNORDERED_LIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
            
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH