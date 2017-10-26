from setuptools import setup, find_packages


setup(
    name='html-similarity',
    version='0.2',
    url='https://github.com/matiskay/html-similarity',
    description='A set of similarity metricts to compare html files.',
    include_package_data=True,
    author='Edgar Marca',
    maintainer='Edgar Marca',
    maintainer_email='matiskay@gmail.com',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'parsel==1.2.0',
    ],
)
