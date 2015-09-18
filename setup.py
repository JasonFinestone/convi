import os

from setuptools import setup, find_packages

setup(
        name='convi',
        version='0.1.0',
        description='Help me convert objects into tests.',
        long_description=('use the convi api and a flask and angularjs frontend package'),
        url='http://gitscrub.com/jfinestone/convi',
        license='CC',
        author='Jason Finestone',
        author_email='jasonfinestone@gmail.com',
        packages=find_packages(exclude=['tests*']),
        install_requires=["Flask==0.10.1",
                          "Flask-RESTful==0.3.4",
                          "Flask-SQLAlchemy==2.0",
                          "Jinja2==2.8",
                          "MarkupSafe==0.23",
                          "SQLAlchemy==1.0.8",
                          "Tempita==0.5.2",
                          "Werkzeug==0.10.4",
                          "aniso8601==1.0.0",
                          "decorator==4.0.2",
                          "itsdangerous==0.24",
                          "pbr==1.8.0",
                          "pytz==2015.4",
                          "requests==2.7.0",
                          "six==1.9.0",
                          "sqlalchemy-migrate==0.10.0",
                          "sqlparse==0.1.16",
                          "wsgiref==0.1.2"
                          ],
        include_package_data=True,
        entry_points = {
                'console_scripts': [
                    'db_create = convi.scripts.db_create:main',
                    'db_downgrade = convi.scripts.db_downgrade:main',
                    'db_upgrade = convi.scripts.db_upgrade:main',
                    'db_migrate= convi.scripts.db_migrate:main',
                    'run_server = convi.scripts.run_server:run_server'
                    ]
            },
        package_data={'static': 'convi/static/*',
                      'templates': 'convi/templates/*'},
        classifiers=[
                    "Private :: Do Not Upload"
                    ],
)
