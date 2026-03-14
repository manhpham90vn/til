#!/usr/bin/env python3
"""Convert all .md files in Programming_Languages/ to .ipynb in Notebooks/.

Usage:
    python md_to_notebook.py
"""

import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
INPUT_DIR = os.path.join(PROJECT_ROOT, "Programming_Languages")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "Notebooks")

# Mapping: filename (without .md) -> { code_lang: language tag in code blocks, kernelspec }
LANGUAGE_CONFIG = {
    "Python": {
        "code_langs": ["python", "bash", "sh", "pip"],
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
            "pygments_lexer": "ipython3",
            "version": "3.11.0",
        },
    },
    "JavaScript": {
        "code_langs": ["javascript"],
        "kernelspec": {
            "display_name": "JavaScript (Node.js)",
            "language": "javascript",
            "name": "javascript",
        },
        "language_info": {
            "file_extension": ".js",
            "mimetype": "application/javascript",
            "name": "javascript",
            "version": "18.0.0",
        },
    },
    "TypeScript": {
        "code_langs": ["typescript", "tsx"],
        "kernelspec": {
            "display_name": "TypeScript",
            "language": "typescript",
            "name": "typescript",
        },
        "language_info": {
            "file_extension": ".ts",
            "mimetype": "application/typescript",
            "name": "typescript",
            "version": "5.0.0",
        },
    },
    "Go": {
        "code_langs": ["go"],
        "kernelspec": {
            "display_name": "Go",
            "language": "go",
            "name": "gophernotes",
        },
        "language_info": {
            "file_extension": ".go",
            "mimetype": "text/x-go",
            "name": "go",
            "version": "1.21.0",
        },
    },
    "Java": {
        "code_langs": ["java"],
        "kernelspec": {
            "display_name": "Java",
            "language": "java",
            "name": "java",
        },
        "language_info": {
            "file_extension": ".java",
            "mimetype": "text/x-java",
            "name": "java",
            "version": "17.0.0",
        },
    },
    "C": {
        "code_langs": ["c"],
        "kernelspec": {
            "display_name": "C",
            "language": "c",
            "name": "c",
        },
        "language_info": {
            "file_extension": ".c",
            "mimetype": "text/x-csrc",
            "name": "c",
            "version": "11",
        },
    },
    "C++": {
        "code_langs": ["cpp"],
        "kernelspec": {
            "display_name": "C++",
            "language": "c++",
            "name": "xcpp17",
        },
        "language_info": {
            "file_extension": ".cpp",
            "mimetype": "text/x-c++src",
            "name": "c++",
            "version": "17",
        },
    },
    "Rust": {
        "code_langs": ["rust"],
        "kernelspec": {
            "display_name": "Rust",
            "language": "rust",
            "name": "rust",
        },
        "language_info": {
            "file_extension": ".rs",
            "mimetype": "text/x-rustsrc",
            "name": "rust",
            "version": "1.70.0",
        },
    },
    "PHP": {
        "code_langs": ["php"],
        "kernelspec": {
            "display_name": "PHP",
            "language": "php",
            "name": "php",
        },
        "language_info": {
            "file_extension": ".php",
            "mimetype": "text/x-php",
            "name": "php",
            "version": "8.2.0",
        },
    },
}


def get_language_config(filename: str) -> dict | None:
    """Get language config from filename (without extension)."""
    name = os.path.splitext(filename)[0]
    return LANGUAGE_CONFIG.get(name)


def md_to_notebook(md_path: str, ipynb_path: str, code_langs: list[str],
                   kernelspec: dict, language_info: dict, magic_langs: dict | None = None):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    cells: list[dict] = []

    # Split content into blocks: markdown text and code blocks
    parts = re.split(r"(```\w*\n.*?\n```)", content, flags=re.DOTALL)

    for part in parts:
        part = part.strip()
        if not part:
            continue

        code_match = re.match(r"^```(\w*)\n(.*)\n```$", part, flags=re.DOTALL)

        if code_match:
            language = code_match.group(1).lower()
            code = code_match.group(2)

            if language in code_langs:
                # Matching language -> code cell
                cells.append(
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": code.splitlines(keepends=True),
                    }
                )
            elif magic_langs and language in magic_langs:
                # Language that can be run with ! prefix -> code cell
                magic = magic_langs[language]
                lines = code.splitlines(keepends=True)
                source = []

                for line in lines:
                    stripped = line.strip()
                    # Add ! prefix to non-empty, non-comment lines
                    if stripped and not stripped.startswith("#"):
                        source.append(magic + line)
                    else:
                        source.append(line)

                cells.append(
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": source,
                    }
                )
            else:
                # Other language (toml, yaml, json, etc.) -> markdown cell
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
            "kernelspec": kernelspec,
            "language_info": language_info,
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
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    md_files = sorted(f for f in os.listdir(INPUT_DIR) if f.endswith(".md"))

    if not md_files:
        print(f"❌ No .md files found in {INPUT_DIR}")
        sys.exit(1)

    print(f"📂 Reading from: {INPUT_DIR}")
    print(f"📂 Writing to:   {OUTPUT_DIR}")
    print(f"📄 Found {len(md_files)} markdown file(s)\n")

    converted = 0
    skipped = 0

    for md_file in md_files:
        config = get_language_config(md_file)
        if config is None:
            print(f"⏭️  Skipping {md_file} (no language config)")
            skipped += 1
            continue

        md_path = os.path.join(INPUT_DIR, md_file)
        ipynb_file = os.path.splitext(md_file)[0] + ".ipynb"
        ipynb_path = os.path.join(OUTPUT_DIR, ipynb_file)
        md_to_notebook(
            md_path, ipynb_path,
            code_langs=config["code_langs"],
            kernelspec=config["kernelspec"],
            language_info=config["language_info"],
            magic_langs=config.get("magic_langs")
        )
        converted += 1
        print()

    print(f"🎉 Done! Converted {converted} file(s), skipped {skipped}.")
