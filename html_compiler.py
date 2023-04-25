import re

# Define regular expressions to match HTML elements
html_tag_regex = r'<\s*([a-zA-Z]+)(?:\s+[^>]*?)?>'
html_close_tag_regex = r'<\s*/\s*([a-zA-Z]+)\s*>'
html_attr_regex = r'([a-zA-Z_-]+)="([^"]+)"'

# Define mapping of HTML elements to corresponding WordPress block components
block_components = {
    "h1": "core/heading",
    "h2": "core/heading",
    "h3": "core/heading",
    "h4": "core/heading",
    "h5": "core/heading",
    "h6": "core/heading",
    "p": "core/paragraph",
    "ul": "core/list",
    "ol": "core/list",
    "li": "core/list-item",
    "img": "core/image",
    "a": "core/button",
}

def compile_html_to_block(html):
    """Compiles an HTML template into a WordPress block"""
    blocks = []
    block_content = ""
    
    # Parse the HTML template and generate the corresponding WordPress blocks
    for line in html.split("\n"):
        # Check if line contains an HTML tag
        match = re.match(html_tag_regex, line)
        if match:
            # Check if tag is a known WordPress block component
            tag_name = match.group(1).lower()
            if tag_name in block_components:
                # Start a new block if necessary
                if block_content:
                    blocks.append({
                        "type": "core/html",
                        "content": block_content,
                    })
                    block_content = ""
                
                # Extract block attributes from HTML tag
                block_attrs = {}
                attrs_match = re.findall(html_attr_regex, line)
                for attr in attrs_match:
                    block_attrs[attr[0]] = attr[1]
                
                # Add the WordPress block component to the list of blocks
                blocks.append({
                    "type": block_components[tag_name],
                    "attrs": block_attrs,
                })
            else:
                # If tag is not a known block component, add it to the content of the current block
                block_content += line
        else:
            # If line does not contain an HTML tag, add it to the content of the current block
            block_content += line
    
    # Add the final block to the list of blocks
    if block_content:
        blocks.append({
            "type": "core/html",
            "content": block_content,
        })
    
    # Generate the block code
    block_code = ""
    for block in blocks:
        block_code += f'[block type="{block["type"]}"'
        if "attrs" in block:
            for attr_name, attr_value in block["attrs"].items():
                block_code += f' {attr_name}="{attr_value}"'
        block_code += ']\n'
        if "content" in block:
            block_code += block["content"]
        block_code += '\n[/block]\n'
    
    return block_code

# Example usage
html_template = """
<h1>Title</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
<img src="image.jpg" alt="Image" />
<a href="#" class="
<button>Click me</button></a>
"""

block_code = compile_html_to_block(html_template)
print(block_code)
