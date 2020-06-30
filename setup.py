import setuptools

setuptools.setup(
    name='query-string',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
