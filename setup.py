"""Setup file for nbtools."""
from setuptools import setup

setup(
    name='nbtools',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=['nbtools'],

    # metadata
    author="K.-Michael Aye",
    author_email="kmichael.aye@gmail.com",
    description="Tools for working with Jupyter notebook",
    license="ISC",
    keywords="Jupyter notebook multiprocessing",
    url="http://github.com/michaelaye/nbtools",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ]

)
