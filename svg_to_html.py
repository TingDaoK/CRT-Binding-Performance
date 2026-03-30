#!/usr/bin/env python3
"""
Convert SVG flamegraphs to interactive HTML files.

This script takes an SVG flamegraph (with embedded JavaScript for interactivity)
and wraps it in a proper HTML document with styling.

Usage:
    python svg_to_html.py input.svg [output.html]

If output.html is not specified, it will use the input filename with .html extension.
"""

import sys
import os
from pathlib import Path


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flamegraph - {title}</title>
    <style>
        body {{
            margin: 0;
            padding: 10px;
            font-family: monospace;
            background-color: #f5f5f5;
        }}
        .container {{
            width: 98%;
            max-width: none;
            margin: 0 auto;
            background-color: white;
            padding: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 4px;
        }}
        h1 {{
            margin: 0 0 10px 0;
            font-size: 18px;
            color: #333;
        }}
        .info {{
            margin-bottom: 10px;
            padding: 8px;
            background-color: #f9f9f9;
            border-left: 4px solid #4CAF50;
            font-size: 12px;
        }}
        svg {{
            display: block;
            width: 100%;
            height: auto;
            min-height: 600px;
            margin: 0 auto;
            border: 1px solid #ddd;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Flamegraph Visualization - {title}</h1>
        <div class="info">
            <strong>Instructions:</strong> Click on frames to zoom in. Use the "Reset Zoom" button to zoom out.
            Search using Ctrl+F or the search box in the flamegraph.
        </div>
        {svg_content}
    </div>
</body>
</html>"""


def convert_svg_to_html(svg_path, html_path=None):
    """
    Convert an SVG flamegraph to an HTML file.

    Args:
        svg_path: Path to the input SVG file
        html_path: Path to the output HTML file (optional)

    Returns:
        Path to the created HTML file
    """
    svg_path = Path(svg_path)

    # Validate input file
    if not svg_path.exists():
        raise FileNotFoundError(f"SVG file not found: {svg_path}")

    if not svg_path.suffix.lower() == '.svg':
        raise ValueError(f"Input file must be an SVG file: {svg_path}")

    # Determine output path
    if html_path is None:
        html_path = svg_path.with_suffix('.html')
    else:
        html_path = Path(html_path)

    # Read SVG content
    print(f"Reading SVG file: {svg_path}")
    with open(svg_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()

    # Extract title from filename
    title = svg_path.stem

    # Create HTML content
    html_content = HTML_TEMPLATE.format(
        title=title,
        svg_content=svg_content
    )

    # Write HTML file
    print(f"Writing HTML file: {html_path}")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Successfully converted {svg_path.name} to {html_path.name}")
    return html_path


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python svg_to_html.py input.svg [output.html]")
        print("\nExample:")
        print("  python svg_to_html.py flamegraph.svg")
        print("  python svg_to_html.py flamegraph.svg output.html")
        sys.exit(1)

    svg_path = sys.argv[1]
    html_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        output_path = convert_svg_to_html(svg_path, html_path)
        print(f"\nYou can now open the file in your browser:")
        print(f"  open {output_path}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
