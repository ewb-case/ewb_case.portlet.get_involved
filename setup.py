from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(
    name='ewb_case.static_portlets',
    version=version,
    description="Static portlets for the EWB Case website",
    long_description=open("README.txt").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      "Development Status :: 4 - Beta",
      ],
    keywords='',
    author='',
    author_email='',
    url='http://github.com/mattbierner/ewb_case.static_portlets/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['ewb_case', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone>=4.0',
        'zope.i18nmessageid',
    ],
    entry_points="""
    # -*- Entry points: -*-
    
    [z3c.autoinclude.plugin]
    target = plone
    """,
    setup_requires=[]
)
