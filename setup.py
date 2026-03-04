from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='python_carbon',
    packages=['python_carbon'],
    version='CURRENT_VERSION',
    license='MIT',
    description='PHP Carbon library adapted for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Roger Vilà',
    author_email='rogervila@me.com',
    url='https://github.com/rogervila/python_carbon',
    download_url='https://github.com/rogervila/python_carbon/archive/CURRENT_VERSION.tar.gz',
    keywords=['php nesbot carbon', 'php carbon'],
    install_requires=[
        'python-dateutil>=2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)
