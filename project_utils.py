#!/usr/bin/env python3
"""
==============================================
Oracle ONE - Data Science Course
==============================================

File: project_utils.py
Author: Mateus Alves de Mendonça
Description: Utility script for project automation and management
Created: Oracle ONE Data Science Program
License: MIT

Usage:
    python project_utils.py --help
    python project_utils.py --count-files
    python project_utils.py --setup-env
"""

import argparse
import os
import sys
import subprocess
from pathlib import Path


def count_project_files():
    """Count various file types in the project."""
    project_root = Path(__file__).parent
    
    # File extensions to count
    extensions = {
        '.py': 'Python files',
        '.md': 'Markdown files',
        '.csv': 'CSV data files',
        '.txt': 'Text files',
        '.ipynb': 'Jupyter notebooks'
    }
    
    print("📊 Project Statistics")
    print("=" * 50)
    
    total_files = 0
    for ext, description in extensions.items():
        files = list(project_root.rglob(f"*{ext}"))
        count = len(files)
        total_files += count
        print(f"{description:20}: {count:3d}")
    
    print("-" * 50)
    print(f"{'Total files':20}: {total_files:3d}")
    
    # Count directories by formation
    formations = list(project_root.glob("*-formacao_*"))
    print(f"\n📚 Formations: {len(formations)}")
    for formation in formations:
        courses = list(formation.glob("*-*"))
        print(f"  {formation.name}: {len(courses)} courses")


def setup_environment():
    """Setup development environment."""
    print("🚀 Setting up development environment...")
    
    # Check if virtual environment exists
    venv_path = Path(".venv")
    if not venv_path.exists():
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"])
    
    # Activate virtual environment and install requirements
    if sys.platform.startswith("win"):
        activate_script = venv_path / "Scripts" / "activate.bat"
        pip_path = venv_path / "Scripts" / "pip.exe"
    else:
        activate_script = venv_path / "bin" / "activate"
        pip_path = venv_path / "bin" / "pip"
    
    if Path("requirements.txt").exists():
        print("Installing requirements...")
        subprocess.run([str(pip_path), "install", "-r", "requirements.txt"])
    
    print("✅ Environment setup complete!")
    print(f"Activate with: source {activate_script}" if not sys.platform.startswith("win") 
          else f"Activate with: {activate_script}")


def check_code_quality():
    """Run basic code quality checks."""
    print("🔍 Running code quality checks...")
    
    python_files = list(Path(".").rglob("*.py"))
    print(f"Found {len(python_files)} Python files")
    
    # Basic syntax check
    syntax_errors = 0
    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                compile(f.read(), py_file, 'exec')
        except SyntaxError as e:
            print(f"❌ Syntax error in {py_file}: {e}")
            syntax_errors += 1
    
    if syntax_errors == 0:
        print("✅ No syntax errors found!")
    else:
        print(f"❌ Found {syntax_errors} syntax errors")


def list_courses():
    """List all available courses."""
    print("📚 Available Courses")
    print("=" * 50)
    
    formations = sorted(Path(".").glob("*-formacao_*"))
    
    for formation in formations:
        print(f"\n📁 {formation.name}")
        courses = sorted(formation.glob("*-*"))
        
        for i, course in enumerate(courses, 1):
            course_name = course.name.replace("_", " ").title()
            
            # Check different completion indicators
            aula_file = course / "aula.py"
            has_subdirs = any(Path(course / item).is_dir() for item in os.listdir(course) if not item.startswith('.'))
            has_python_files = any(course.rglob("*.py"))
            
            # Determine status
            if aula_file.exists():
                status = "✅"  # Has main aula.py file
            elif has_subdirs and has_python_files:
                status = "✅"  # Has subdirectories with Python files (completed exercises)
            elif has_python_files:
                status = "🔄"  # Has some Python files but might be in progress
            else:
                status = "⏳"  # No Python files found
            
            print(f"  {i:2d}. {status} {course_name}")
    
    print("\n" + "=" * 50)
    print("Legenda: ✅ Concluído | 🔄 Em andamento | ⏳ Não iniciado")


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="Oracle ONE Data Science Project Utilities"
    )
    
    parser.add_argument(
        "--count-files", 
        action="store_true",
        help="Count files in the project"
    )
    
    parser.add_argument(
        "--setup-env", 
        action="store_true",
        help="Setup development environment"
    )
    
    parser.add_argument(
        "--check-quality", 
        action="store_true",
        help="Run code quality checks"
    )
    
    parser.add_argument(
        "--list-courses", 
        action="store_true",
        help="List all available courses"
    )
    
    args = parser.parse_args()
    
    if args.count_files:
        count_project_files()
    elif args.setup_env:
        setup_environment()
    elif args.check_quality:
        check_code_quality()
    elif args.list_courses:
        list_courses()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
