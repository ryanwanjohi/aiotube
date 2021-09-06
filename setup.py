from setuptools import setup

def readme():
    with open('README.md') as file:
        README = file.read()
    return README


setup(
    name = 'dya',
    version = '3.4.5',
    description = 'Get Unlimited YouTube Public Data without YouTubeData API',
    long_description = readme(),
    long_description_content_type="text/markdown",
    py_modules = ["DYA"],
    package_dir = {'': 'src'},
    install_requires = [
        'urllib3'
    ],
    url = 'https://github.com/jnsougata/Ditch-YouTubeAPI/blob/main/README.md',
    project_urls={
        "Bug Tracker": "https://github.com/jnsougata/Ditch-YouTube-API/issues"
    },
    author = 'Sougata Jana',
    author_email = 'jnsougata@gmail.com',
    license = 'MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)