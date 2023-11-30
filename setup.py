from setuptools import setup, find_packages

setup(
    name='codemonkeys',
    version='1.0.5',
    description="CodeMonkeys gives devs control over their automated GPT logic. The current focus is working on "
                "codebases but it is lovingly designed to enable automations of all kinds. This framework aims to use "
                "AI effectively, while being reliable, predictable, and tailored to your needs. There is a strong "
                "focus on only involving AI at crucial areas of strength, and using good old-fashioned code for "
                "everything else.",
    long_description="CodeMonkeys gives devs control over their automated GPT logic. The current focus is working on "
                     "codebases but it is lovingly designed to enable automations of all kinds. This framework aims "
                     "to use AI effectively, while being reliable, predictable, and tailored to your needs. There is "
                     "a strong focus on only involving AI at crucial areas of strength, and using good old-fashioned "
                     "code for everything else.",
    long_description_content_type='text/markdown',
    url='https://github.com/cooleydw494/codemonkeys',
    author='David Wallace Cooley Jr',
    author_email='cooleydw494@gmail.com',
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'openai', 'python-dotenv', 'Levenshtein', 'pandas', 'termcolor', 'tiktoken', 'psutil', 'json-repair',
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
            'monk=codemonkeys.scripts.monk',
            'monk-new=codemonkeys.scripts.monk_new:main',
        ],
    }
)
