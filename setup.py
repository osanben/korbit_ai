"""
Korbit AI 项目安装配置
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="korbit-ai",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Korbit AI - 一个现代化的AI项目框架",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/korbit_ai",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
        ],
        "tensorflow": ["tensorflow>=2.13.0"],
        "opencv": ["opencv-python>=4.8.0"],
        "web": ["streamlit>=1.25.0", "fastapi>=0.100.0", "uvicorn>=0.23.0"],
    },
    entry_points={
        "console_scripts": [
            "korbit-ai=korbit_ai.cli:main",
        ],
    },
) 