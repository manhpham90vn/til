#!/usr/bin/env python3
"""Convert Python.md to Python.ipynb (Jupyter Notebook).

Usage:
    python md_to_notebook.py Python.md Python.ipynb
"""

import json
import re
import sys


def md_to_notebook(md_path: str, ipynb_path: str):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    cells = []

    # Split content into blocks: markdown text and code blocks
    parts = re.split(r"(```\w*\n.*?\n```)", content, flags=re.DOTALL)

    for part in parts:
        part = part.strip()
        if not part:
            continue

        code_match = re.match(r"^```(\w*)\n(.*)\n```$", part, flags=re.DOTALL)

        if code_match:
            language = code_match.group(1)
            code = code_match.group(2)

            if language == "python":
                # Python code -> code cell
                cells.append(
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": code.splitlines(keepends=True),
                    }
                )
            else:
                # Non-python code (bash, toml, yaml, json) -> markdown cell
                md_content = f"```{language}\n{code}\n```"
                cells.append(
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": md_content.splitlines(keepends=True),
                    }
                )
        else:
            # Markdown text -> split on --- for separate sections
            sections = re.split(r"\n---\n", part)
            for section in sections:
                section = section.strip()
                if section:
                    cells.append(
                        {
                            "cell_type": "markdown",
                            "metadata": {},
                            "source": section.splitlines(keepends=True),
                        }
                    )

    # Fix source: ensure each line ends with \n except the last
    for cell in cells:
        source = cell["source"]
        if source:
            fixed = []
            for i, line in enumerate(source):
                if not line.endswith("\n") and i < len(source) - 1:
                    fixed.append(line + "\n")
                else:
                    fixed.append(line)
            cell["source"] = fixed

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbformat_minor": 5,
                "pygments_lexer": "ipython3",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    with open(ipynb_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)

    print(f"✅ Converted {md_path} -> {ipynb_path}")
    print(f"   Total cells: {len(cells)}")
    code_cells = sum(1 for c in cells if c["cell_type"] == "code")
    md_cells = sum(1 for c in cells if c["cell_type"] == "markdown")
    print(f"   Code cells: {code_cells}")
    print(f"   Markdown cells: {md_cells}")


if __name__ == "__main__":
    md_path = sys.argv[1] if len(sys.argv) > 1 else "Python.md"
    ipynb_path = sys.argv[2] if len(sys.argv) > 2 else "Python.ipynb"
    md_to_notebook(md_path, ipynb_path)
