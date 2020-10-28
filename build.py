#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "MovieRecommender"
version = "1.0"

summary = "API for movie recommender system"
url     = ""

description = """API that let's you find your new favorite movies, based on the movies you already enjoied.
Just use this API, that is directly linked to the offical Imdb-databes and be surprised what results you will get :)"""

authors      = [Author("Stefan Beuchert", "stefan.beuchert@gmx.de")]
license      = "None"
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on("mockito")

@init
def set_properties(project):
    pass
