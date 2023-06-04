from setuptools import setup, find_packages

setup(
    name='logidrivepy',
    version='0.2.0',
    description='A Python module for interfacing with Logitech steering wheels.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cengizozel/logidrivepy',
    author='Cengiz Ozel',
    author_email='cozel@cs.rochester.edu',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={'logidrivepy': ['dll/*.dll']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='logitech, g920, driving, wheel, controller',
    install_requires=[
    ],
)
