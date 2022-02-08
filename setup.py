import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DIDACTIC-WADDLE-odob",
    version="0.1.0",
    author="odob",
    author_email="oordonezb@unal.edu.co",
    description="A package for data structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YamiYume/didactic-waddle",
    project_urls={
        "Git hub": "https://github.com/YamiYume/didactic-waddle",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
