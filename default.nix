with import <nixpkgs> {};

python.buildEnv.override {
  extraLibs = [ pkgs.python36Packages.django_2_0 pkgs.python36Packages.djangorestframework pkgs.python36Packages.psycopg2 pkgs.python36Packages.gunicorn ];
  ignoreCollisions = true;
}
