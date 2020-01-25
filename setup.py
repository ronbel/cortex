from setuptools import setup, find_packages


setup(
    name = 'cortex',
    version = '0.1.0',
    author = 'Ron Belkin',
    description = 'My submission for the Advanced System Design class in Tel Aviv University',
    packages = find_packages(),
    install_requires = ['click', 'flask'],
    tests_require = ['pytest', 'pytest-cov'],
)
