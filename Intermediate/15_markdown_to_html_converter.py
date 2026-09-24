import re


def convert_markdown_to_html(markdown_text):
    """
    Converts a simple Markdown string into HTML output.
    Supports headers (# to ######), bold (**), italic (*), code blocks (```), inline code (`), and unordered lists (* or -).
    """
    lines = markdown_text.splitlines()
    html_lines = []
    in_code_block = False
    in_list = False

    for line in lines:
        # Handle code blocks delimited by ```
        if line.strip().startswith("```"):
            if in_code_block:
                html_lines.append("</code></pre>")
                in_code_block = False
            else:
                html_lines.append("<pre><code>")
                in_code_block = True
            continue

        if in_code_block:
            # Escape HTML special characters inside code blocks
            escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            html_lines.append(escaped_line)
            continue

        # Handle unordered list items starting with '-' or '*'
        list_match = re.match(r"^\s*[\*\-]\s+(.*)$", line)
        if list_match:
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            content = list_match.group(1)
            content = parse_inline_markdown(content)
            html_lines.append(f"  <li>{content}</li>")
            continue
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False

        # Handle headers (# Header)
        header_match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if header_match:
            level = len(header_match.group(1))
            content = parse_inline_markdown(header_match.group(2))
            html_lines.append(f"<h{level}>{content}</h{level}>")
            continue

        # Handle blank lines or paragraphs
        if line.strip() == "":
            html_lines.append("")
        else:
            content = parse_inline_markdown(line)
            html_lines.append(f"<p>{content}</p>")

    if in_list:
        html_lines.append("</ul>")

    if in_code_block:
        html_lines.append("</code></pre>")

    return "\n".join(html_lines)


def parse_inline_markdown(text):
    """
    Parses inline Markdown syntax: bold (**text**), italic (*text*), and inline code (`code`).
    """
    # Replace inline code: `code` -> <code>code</code>
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Replace bold text: **text** -> <strong>text</strong>
    text = re.sub(r"\*\*([^\*]+)\*\*", r"<strong>\1</strong>", text)
    # Replace italic text: *text* -> <em>text</em>
    text = re.sub(r"\*([^\*]+)\*", r"<em>\1</em>", text)
    return text


if __name__ == "__main__":
    print("=== Markdown to HTML Converter ===")

    sample_markdown = """# Welcome to Markdown Converter

This is a **simple** Markdown to HTML converter built in *Python*.

## Features
* Supports headers
* Supports **bold** and *italic* text
* Supports `inline code` and code blocks
* Supports unordered lists

```
def hello_world():
    print("Hello, HTML!")
```
"""

    print("\n--- Original Markdown ---")
    print(sample_markdown)

    html_output = convert_markdown_to_html(sample_markdown)

    print("--- Converted HTML Output ---")
    print(html_output)
