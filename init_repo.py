#!/usr/bin/env python3
"""
Initialize a new repository from the py_template using Copier.

This script initializes a new Python project from the current template
by using Copier to perform variable replacement throughout the files.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Initialize a new Python project from the template using Copier."
    )
    parser.add_argument(
        "project_name",
        help="Name of the new project (will be used as both the repository name and the Python package name)"
    )
    parser.add_argument(
        "--description", 
        default="A Python project created from template",
        help="Short description of the project"
    )
    parser.add_argument(
        "--author-name", 
        default="", 
        help="Author name"
    )
    parser.add_argument(
        "--author-email", 
        default="", 
        help="Author email"
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory where the new project will be created (default: current directory)"
    )
    return parser.parse_args()

def run_copier(args):
    """Run Copier to create the new project."""
    # Determine template path (current directory)
    template_path = Path(__file__).parent.absolute()
    output_path = Path(args.output_dir).absolute() / args.project_name
    
    # Prepare Copier command
    cmd = ["copier", "copy", str(template_path), str(output_path)]
    
    # Add answers for Copier prompts
    cmd.extend(["--data", f'{{"project_name": "{args.project_name}", "project_description": "{args.description}", "author_name": "{args.author_name}", "author_email": "{args.author_email}"}}'])
    
    print(f"Creating new project: {args.project_name}")
    print(f"Template path: {template_path}")
    print(f"Output path: {output_path}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print(f"Project created successfully at: {output_path}")
        
        # Print instructions for next steps
        print("\n== Next steps ==")
        print(f"1. cd {args.project_name}")
        print("2. Initialize Git repository: git init")
        print("3. Install dependencies: rye sync")
        print("4. Activate environment: rye shell")
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating project: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)

def main():
    args = parse_arguments()
    run_copier(args)

if __name__ == "__main__":
    main()