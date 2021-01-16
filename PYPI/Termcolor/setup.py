from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='termcolour',
    version='0.0.1',
    description='Change the terminal output color',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Victor Kolis',
    author_email='victorkolis@protonmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='ASCII, terminal, output',
    packages=find_packages(),
    install_requires=['']
)
