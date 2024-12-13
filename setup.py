from setuptools import setup, find_packages

setup(
    name='leetcode-cli',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'lc=cli:main',
        ],
    },
    author='Harsh Panchal, Anmol Panchal',
    description='A CLI tool for LeetCode',
    url='https://github.com/HarshPanchal01/LeetCode-CLI',
)