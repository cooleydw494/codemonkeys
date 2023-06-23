from setuptools import setup, find_packages

setup(
    name='codemonkeys',
    version='0.0.5',
    description="CodeMonkeys is a highly configurable tool for creating/running strategic AI automations (and "
                "more). Beyond that, its a thoughtful and extensible codemonkeys for creating automation abilities. "
                "CodeMonkeys' design was heavily influenced by how much it was used in its own development, "
                "naturally converging to a sublime synergy of the tool and the codemonkeys files.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cooleydw494/codemonkeys',
    author='David Wallace Cooley Jr',
    author_email='cooleydw494@gmail.com',
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
