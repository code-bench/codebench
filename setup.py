import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='codebench',
    version='0.1',
    author="Boxuan Li",
    author_email="liboxuan@connect.hku.hk",
    description="Automated code benchmark solution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/li-boxuan/codebench",
    packages=setuptools.find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'codebench = codebench.main:main'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
