import setuptools

setuptools.setup(
    name='riskcore',
    version='0.1.0',
    packages=setuptools.find_packages(),
    install_requires=[
        "tensorflow==2.15.0"
    ],
    url='https://github.com/jialuechen/riskcore',
    license='Apache-2.0',
    author='Jialue Chen',
    author_email='jialuechen@outlook.com',
    description='Python Machine Learning Library for Financial Risk Management'
)