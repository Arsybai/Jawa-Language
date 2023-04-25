import setuptools

setuptools.setup(
    name="jawalang",
    version="1.0.5",
    author="Arsybai",
    description="Javanese programming language base on python",
    packages=["jawalang"],
    license="MIT",
    author_email="me@arsybai.com",
    url="https://github.com/Arsybai/jawa-language",
    keywords=[
        'programming languages',
        'languages',
    ],
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "jawalang = jawalang.__main__:main"
        ]
    },
    long_description="""# Jawa-Language
Jawa-Language, Programming language for javanese people.
this language is based on python.

### Required
- Python 3.x

### Installation
```shell
> pip3 install jawalang
```
Or clone this repository and 
```shell
> pip3 install -e .
```

## Run
```shell
> jawalang run <your_file.jw>
```

### Syntax Highlighter
Install Visual Studio Code extension
[Jawa-Language-Support](https://marketplace.visualstudio.com/items?itemName=arsybai.jawa-language-support)

### Example
You can find more in `example` folder
```python
a = 0
b = 1

# if a == b
yen a podo karo b:
    nyetak("podo")
# elif a != b:
liyane tur a bedo karo b:
    nyetak("bedo")
# else
liyane:
    nyetak("Bedo cuk")

# Short hand if else
nyetak("Bedo") yen a bedo karo b liyane nyetak("podo")
```"""
)
