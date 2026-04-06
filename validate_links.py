#!/usr/bin/env python3
"""
Markdown Internal Links Validator

This script validates all internal relative links in markdown files within the /docs folder.
It checks if linked files actually exist and reports broken links in VS Code-clickable format.

Usage:
    python validate_links.py
"""

import os
import re
from pathlib import Path


def validate_internal_links(workspace_root):
    """
    Validates all internal markdown links in the docs folder.
    
    Parses markdown links in the following formats:
    - [text](../folder/file.md)
    - [text](docs/folder/file.md)
    - [text](../folder/file.md#section)
    
    Outputs broken links in VS Code clickable format: path/to/file.md:line_number
    
    Args:
        workspace_root: Path to the project root (where docs folder is located)
    """
    
    docs_root = os.path.join(workspace_root, 'docs')
    
    # Pattern to match markdown links: [text](path)
    # This captures link text and the URL/path inside parentheses
    link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    
    broken_links = []
    total_links_checked = 0
    
    # Walk through all markdown files in docs folder
    for root, dirs, files in os.walk(docs_root):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    for line_num, line_content in enumerate(lines, 1):
                        # Find all links in this line
                        matches = re.finditer(link_pattern, line_content)
                        
                        for match in matches:
                            link_text = match.group(1)
                            link_path = match.group(2)
                            total_links_checked += 1
                            
                            # Remove anchor/fragment if present (e.g., #section)
                            if '#' in link_path:
                                link_path_only = link_path.split('#')[0]
                            else:
                                link_path_only = link_path
                            
                            # Skip empty paths and external links
                            if not link_path_only or link_path_only.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                                continue
                            
                            # Resolve the path based on its format
                            if link_path_only.startswith('docs/'):
                                # Absolute path from workspace root: docs/folder/file.md
                                resolved_path = os.path.join(workspace_root, link_path_only)
                            elif link_path_only.startswith('/docs/'):
                                # Absolute path with leading slash: /docs/folder/file.md
                                resolved_path = os.path.join(workspace_root, link_path_only.lstrip('/'))
                            else:
                                # Relative path from current file: ../folder/file.md or ./file.md
                                current_dir = os.path.dirname(file_path)
                                resolved_path = os.path.join(current_dir, link_path_only)
                            
                            # Normalize the path (handles .. and . and removes duplicate separators)
                            resolved_path = os.path.normpath(resolved_path)
                            
                            # Check if the file exists
                            if not os.path.isfile(resolved_path):
                                broken_links.append({
                                    'file_path': file_path,
                                    'line': line_num,
                                    'link': link_path,
                                    'resolved': resolved_path,
                                    'link_text': link_text
                                })
                
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    # Output results
    print(f"\n{'='*80}")
    print(f"Link Validation Report")
    print(f"{'='*80}\n")
    
    if broken_links:
        print(f"❌ Found {len(broken_links)} broken link(s) out of {total_links_checked} total links:\n")
        
        for item in broken_links:
            # Format for VS Code: file:line (clickable format)
            rel_file = os.path.relpath(item['file_path'], workspace_root)
            vscode_link = f"{rel_file}:{item['line']}"
            
            print(f"{vscode_link}")
            print(f"   Link text:    [{item['link_text']}]")
            print(f"   Link path:    {item['link']}")
            print(f"   Expected at:  {os.path.relpath(item['resolved'], workspace_root)}")
            print()
        
        print(f"{'='*80}\n")
        print("💡 Tip: Click on any 'file:line' link above while holding Ctrl to open it in VS Code\n")
    else:
        print(f"✓ All {total_links_checked} internal links are valid!\n")
        print(f"{'='*80}\n")


if __name__ == "__main__":
    # Determine workspace root (directory where this script is located)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("🔍 Validating internal markdown links...\n")
    validate_internal_links(script_dir)
