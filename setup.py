from setuptools import setup, find_packages

# Lire le README pour la description longue
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simulateur-trafic-refka",
    version="1.0.0",
    author="Refka Mechri",
    author_email="ref.kaa2002@gmail.com",
    description="Simulateur de trafic routier avec analyse statistique et visualisation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RefkaMechri/simulateur-trafic",
    project_urls={
        "Bug Tracker": "https://github.com/RefkaMechri/simulateur-trafic/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
    ],
    # Packages à inclure
    packages=["core", "models", "io_utils"],
    # Modules Python individuels (fichiers .py à la racine)
    py_modules=["exceptions"],
    python_requires=">=3.8",
    # Dépendances
    install_requires=[
        "matplotlib>=3.0",
    ],
    # Dépendances optionnelles
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "sphinx>=5.0",
            "sphinx-autodoc-typehints>=1.0",
        ],
    },
    # Inclure les fichiers de données
    include_package_data=True,
    package_data={
        "": ["data/*.json"],
    },
)