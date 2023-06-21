from setuptools import setup, find_packages

from __init__ import __author__, __description__, __email__, __version__

setup(
    name='codemonkeys',
    version=__version__,
    description=__description__,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cooleydw494/codemonkeys',
    author=__author__,
    author_email=__email__,
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'openai', 'pyyaml', 'python-dotenv', 'python-Levenshtein',
        'termcolor', 'tiktoken', 'psutil', 'ruamel.yaml'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'codemonkeys=codemonkeys.__main__:main',
        ],
    },
    scripts=['scripts/monk']
)
