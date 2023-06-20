from setuptools import setup

from __init__ import __author__, __description__, __email__, __version__, __website__, __licenses__, __dependencies__

setup(
    name='codemonkeys',
    version=f'{__version__}',
    description=f'{__description__}',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url=f'{__website__}',
    author=f'{__author__}',
    author_email=f'{__email__}',
    license=__licenses__[0],
    packages=['codemonkeys'],
    install_requires=__dependencies__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'codemonkeys=codemonkeys.__main__:main',
            'monk=codemonkeys.monk.__main__:main',
        ],
    },
)
