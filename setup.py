import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freeg",
    version="0.8",
    author="refk32",
    author_email="refk32@gmail.com",
    description="Scrape limited free games",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/refk32/freeg",
    packages=setuptools.find_packages(),
    install_requires=[            
          'requests',
          'beautifulsoup4',
          'tldextract'
        ],
    entry_points={
        "console_scripts" : [
            "freeg = freeg.freeg_cli:main"
        ],

    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop"
    ],
    python_requires='>=3.6',
)
