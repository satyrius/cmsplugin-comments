from setuptools import setup, find_packages

from cmsplugin_comments import __version__


CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Topic :: Internet :: WWW/HTTP :: Site Management',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='cmsplugin-comments',
    version=__version__,
    description='Django CMS page comments plugin',
    author='Anton Egorov',
    author_email='anton.egoroff@gmail.com',
    url='https://github.com/satyrius/cmsplugin-comments',
    license='MIT',
    long_description=open('README.rst').read(),
    classifiers=CLASSIFIERS,
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-cms',
    ],
    tests_require=['tox>=1.8'],
    zip_safe=False,
)
