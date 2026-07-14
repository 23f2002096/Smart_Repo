from setuptools import setup, find_packages

setup(
    name="smart_repo",
    version="0.1.0",
    description="AI-powered source code knowledge graph for repository understanding",
    author="Neeraj Kumar",
    python_requires=">=3.11",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
)