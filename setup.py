from setuptools import setup


def readme():
    with open("README-python.md") as f:
        return f.read()


setup(
    name="stopwordsiso",
    version="0.4",
    description="Collection of stopwords for multiple languages. Using ISO 639-1 language code.",
    url="http://github.com/thothmedia/stopwords-iso",
    author="Arthit Suriyawongkul",
    author_email="arthit@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Text Processing :: Linguistic",
    ],
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="stopwords language",
    license="MIT",
    packages=["stopwordsiso"],
    include_package_data=True,
    package_data={
        "stopwordsiso": ["stopwords-iso.json"],
    },
    zip_safe=False,
)
