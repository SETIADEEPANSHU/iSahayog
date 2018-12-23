## Readme

## Demo:
![](https://lh6.googleusercontent.com/_QSsEYwDSR7ukLIzeGUbPYasf7FS9bYFxKc-OGIbTvs3P1A_SIdiDmuekSLVs9UWI3Rd5JfsRixWELQyEfXlQ7n0xBCyO1WB-hToVrjr)


## Problem Statement: 
Mapping college neighbourhood and Social Possibilities
## Problem Description:
There are many locally relevant problems which come across to UGC where the nearby educational institution can play a vital role. Bringing such problems into the notice of nearby educational institution can be thought of as an open-source innovation /crowd-sourced solution. For example, managing traffic or reducing accident rates by the initiative/involvement of an institution in the vicinity. Or, sharing an innovation on water harvesting (an MRP or a Project) and impacting the real saving of water may be mapped. Many student projects can be well aligned to local social problems. Can we have a digital tool for such project based collaborations with real impact. Can we map such colleges and link it with the digital platform to share innovations (as mentioned in problem statement 3). This can directly impact the curriculum with the real regional requirement, a way to ensure relevance of learning.
An example: A district has very unfavourable number of old-young ratio of citizens. This clearly indicates the possibility for having a course in geriatrics or assistive healthcare in the colleges in that district.
## Solution:
Collaboration based innovative solutions through Portal 
## Solution Description:
A Web App which gathers all problems related to society and neighbourhood from various sources like Grievance Portal , Complaints portal (crawlers), Social Media like twitter,facebook (based on sentimental analysis) stack rank them and gathers in our database. The problems are then categorised through Machine Learning categorisation algorithm using Scikit-learn Library . These categorized problems are then mapped to nearby local colleges . Finally problem solvers can pick the problem and collaborate(with other solvers) through Slack API integrated client in our website. Lastly monitoring of projects and their status in real-time by UGC through UGC-console. 
## TECHNOLOGY STACK 
Front End:  • Bootstrap/SemanticUl • HTML5, CSS • JavaScript/JQuery 
Database:  • MySql/MongoDB • Hadoop. 
Server Side:  • Python • AJAX • Machine Learning. 
## USE CASE
![](https://lh5.googleusercontent.com/tpFPdHXjdLbSUW7Dgp76xEDkHFgANL19u6ixXETsF4WUarWxwHy4Hugo7-vDpfN8EAHykTjSb5sn4DVq4x1Ike0XpZi4362v-YH7-kFY0nIYO29Y4T9toKCTqY1dwSndrUIbVGTB)

web2py is a free open source full-stack framework for rapid development of fast, scalable, secure and portable database-driven web-based applications.

It is written and programmable in Python. LGPLv3 License

Learn more at http://web2py.com

## Google App Engine deployment

    cp examples/app.yaml ./
    cp handlers/gaehandler.py ./

Then edit ./app.yaml and replace "yourappname" with yourappname.

## Important reminder about this GIT repo

An important part of web2py is the Database Abstraction Layer (DAL). In early 2015 this was decoupled into a separate code-base (PyDAL). In terms of git, it is a sub-module of the main repository.

The use of a sub-module requires a one-time use of the --recursive flag for git clone if you are cloning web2py from scratch.

    git clone --recursive https://github.com/web2py/web2py.git

If you have an existing repository, the commands below need to be executed at least once:

    git submodule update --init --recursive

If you have a folder gluon/dal you must remove it:

    rm -r gluon/dal

PyDAL uses a separate stable release cycle to the rest of web2py. PyDAL releases will use a date-naming scheme similar to Ubuntu. Issues related to PyDAL should be reported to its separate repository.


## Documentation (readthedocs.org)

[![Docs Status](https://readthedocs.org/projects/web2py/badge/?version=latest&style=flat-square)](http://web2py.rtfd.org/)

## Tests

[![Build Status](https://img.shields.io/travis/web2py/web2py/master.svg?style=flat-square&label=Travis-CI)](https://travis-ci.org/web2py/web2py)
[![MS Build Status](https://img.shields.io/appveyor/ci/web2py/web2py/master.svg?style=flat-square&label=Appveyor-CI)](https://ci.appveyor.com/project/web2py/web2py)
[![Coverage Status](https://img.shields.io/codecov/c/github/web2py/web2py.svg?style=flat-square)](https://codecov.io/github/web2py/web2py)


## Installation Instructions

To start web2py there is NO NEED to install it. Just unzip and do:

    python web2py.py

That's it!!!

## web2py directory structure

    project/
        README
        LICENSE
        VERSION                    > this web2py version
        web2py.py                  > the startup script
        anyserver.py               > to run with third party servers
        ...                        > other handlers and example files
        gluon/                     > the core libraries
            packages/              > web2py submodules
              dal/
            contrib/               > third party libraries
            tests/                 > unittests
        applications/              > are the apps
            admin/                 > web based IDE
                ...
            examples/              > examples, docs, links
                ...
            welcome/               > the scaffolding app (they all copy it)
                ABOUT
                LICENSE
                models/
                views/
                controllers/
                sessions/
                errors/
                cache/
                static/
                uploads/
                modules/
                cron/
                tests/
            ...                    > your own apps
        examples/                  > example config files, mv .. and customize
        extras/                    > other files which are required for building web2py
        scripts/                   > utility and installation scripts
        handlers/
            wsgihandler.py         > handler to connect to WSGI
            ...                    > handlers for Fast-CGI, SCGI, Gevent, etc
        site-packages/             > additional optional modules
        logs/                      > log files will go in there
        deposit/                   > a place where web2py stores apps temporarily

## Issues?

Report issues at https://github.com/web2py/web2py/issues
