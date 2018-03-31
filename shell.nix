with import <nixpkgs> {};

(python36.withPackages (ps: [ps.django ps.djangorestframework ps.gunicorn ps.psycopg2])).env
