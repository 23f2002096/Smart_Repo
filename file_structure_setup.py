from pathlib import Path

# =====================================================
# Smart-Repo Project Structure Creator
# =====================================================

ROOT = Path.cwd()

folders = [
    # Source
    "src/smart_repo",
    "src/smart_repo/parser",
    "src/smart_repo/database",
    "src/smart_repo/routes",
    "src/smart_repo/services",
    "src/smart_repo/utils",
    "src/smart_repo/visualization",

    # Data
    "data/uploads",
    "data/extracted",
    "data/graphs",

    # Frontend
    "templates",
    "static/css",
    "static/js",
    "static/images",

    # Tests
    "tests",
]

files = [
    # Root
    ".env",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",

    # Source Package
    "src/smart_repo/__init__.py",
    "src/smart_repo/app.py",
    "src/smart_repo/config.py",

    # Parser
    "src/smart_repo/parser/__init__.py",
    "src/smart_repo/parser/scanner.py",
    "src/smart_repo/parser/ast_parser.py",
    "src/smart_repo/parser/extractor.py",
    "src/smart_repo/parser/graph_builder.py",

    # Database
    "src/smart_repo/database/__init__.py",
    "src/smart_repo/database/db.py",
    "src/smart_repo/database/models.py",
    "src/smart_repo/database/repository.py",

    # Routes
    "src/smart_repo/routes/__init__.py",
    "src/smart_repo/routes/upload_routes.py",
    "src/smart_repo/routes/dashboard_routes.py",
    "src/smart_repo/routes/ai_routes.py",

    # Services
    "src/smart_repo/services/__init__.py",
    "src/smart_repo/services/analyzer.py",
    "src/smart_repo/services/summary.py",
    "src/smart_repo/services/ai_service.py",

    # Utils
    "src/smart_repo/utils/__init__.py",
    "src/smart_repo/utils/file_utils.py",
    "src/smart_repo/utils/logger.py",
    "src/smart_repo/utils/zip_utils.py",

    # Visualization
    "src/smart_repo/visualization/__init__.py",
    "src/smart_repo/visualization/graph_visualizer.py",
    "src/smart_repo/visualization/charts.py",

    # Templates
    "templates/base.html",
    "templates/index.html",
    "templates/upload.html",
    "templates/dashboard.html",
    "templates/graph.html",
]

# -----------------------------------------------------
# Create folders
# -----------------------------------------------------

for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------
# Create files
# -----------------------------------------------------

for file in files:
    path = ROOT / file
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()

print("=" * 55)
print(" Smart-Repo project structure created successfully!")
print("=" * 55)
print(f"Project Root : {ROOT}")
print(f"Folders Created : {len(folders)}")
print(f"Files Created   : {len(files)}")
print("=" * 55)