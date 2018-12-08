import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='codebench',
    version='0.0.1',
    author='Boxuan Li',
    author_email='liboxuan@connect.hku.hk',
    description='Automated code benchmark solution',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/li-boxuan/codebench',
    packages=setuptools.find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'codebench = codebench.main:main'
        ],
    },
    install_requires=[
        'GitPython',
        'psutil',
        'pyecharts',
    ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
