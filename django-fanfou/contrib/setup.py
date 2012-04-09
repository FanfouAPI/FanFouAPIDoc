#!/usr/bin/env python

from distutils.core import setup

setup(name='fanfouapi',
            version='0.1.0',
            description='Python django api',
            author='Zeng Ke',
            author_email='zengke@fanfou.com',
            packages=['fanfouapi', 'fanfouapi.management', 'fanfouapi.management.commands'],
           )


