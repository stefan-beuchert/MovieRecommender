# Movie Recommender System

## Badges
![travis_build](https://travis-ci.org/stefan-beuchert/MovieRecommender.svg?branch=main)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=security_rating)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=sqale_index)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=bugs)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=code_smells)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)

## Exercise A for Advanced Software Engineering

### General
This repository contains a backend, that can be used to get (movie) recommendations based on a dataset of movies represented by text documents.
This software is not only limited to a specific dataset. By simply changing some values in the config.py, this backend is used as a recommender system for all sorts of text documents.


### Prerequisites
* A (Movie-)Dataset (I included a small sample for testing under src/data)
* A MongoDB server
* Postman or other another software (for Requests)

### Handling
1. Clone this repository
2. Create a virtual environment
3. Install pybuilder 

   `pip install pybuilder`

4. Start MongoDb
5. Make necessary adjustments in config.py (especially for the database and dataset paths)
6. Build the project 

   `pyb publish`

7. Install the target 

   `pip install target/dist/ContentBasedRecommenderSystem-1.0.dev0/dist/ContentBasedRecommenderSystem-1.0.dev0.tar.gz`
8. Start the backend 

   `start_api.py`
9. Post HTTP-requests via a browser or postman
10. Enjoy :)

## Exercise B for Advanced Software Engineering
### 1 UML
   
I made 3 UML diagrams for this project. Each of those diagram has blue and orange parts. The blue parts are features that are already implemented in this project and the orang features may be added in future versions.
   * A [Use Case diagram](tasks/uml_diagrams/use_case_diagram.png) that shows the different actors and the various functions of the system. 
   * A [Sequence diagram](tasks/uml_diagrams/sequence_diagram.png) that shows the different interactions between the different components. 
   * A [Activity diagram](tasks/uml_diagrams/activity_diagram.png) that shows the flow between different activities. 
  
### 2 DDD

   For the DDD part, I made multiple sketches, that consist of multiple components/domains / bounded context. I have marked the implemented parts in blue and the not yet implemented parts in yellow (same as in the UML diagrams).

   * Problem Space
      * [Domain](tasks/ddd/ddd_problem_space.png) with Subdomains.

   * Solution Space
      * [Context Map](tasks/ddd/ddd_solution_space.png) with Bounded Contexts and realationships.

   * Ubiquitous Language
      * [Glossary](tasks_ddd/ubiquitous_language.pdf) with the most important terms. 


### 3 Metrics
For metrics, I used Sonarqube (SonarCloud to be specific).
I used multiple different metrics to ensure the quality of my code. Each metric is documented by a batch (which updates after each push). The metrics are:
   * bugs

      [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=bugs)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)

   * code smells

      [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=code_smells)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)

   * security

      [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=security_rating)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)

   * reliability

      [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)

   * maintainability

      [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)

   * technical debt

      [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=sqale_index)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)

   * vulnerability

      [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=stefan-beuchert_MovieRecommender&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender)


The SonarCloud overview for this project can be accessed by using this [link](https://sonarcloud.io/dashboard?id=stefan-beuchert_MovieRecommender). 

And [this](tasks/SonarCloud.PNG) is a screenshot of the website if it should not be available for some reason.


### 4 Clean Code Development
   
A cheat sheet with my most important clean code principles. I decided to write my cheat sheet in python, so I can test my code examples right on the spot.
   * [Cheat Sheet](tasks/clean_code_cheat_sheet.py)
   
And the five points, that prove my use of clean code. You can find more details for each point in the linked file.

   * Cheat Sheet points 3 and 4:

      Keeping statements simple and making them multiline, if necessary.
      This can also help debugging code, by just commenting out one or more lines
      and still, keep the statement syntactically correct.

      [backend.py](src/main/python/api/backend.py)

   * Cheat Sheet point  8: 
   
      Choosing good variable names, to make code self-explanatory. 

      [data_processing.py](src/main/python/processing/data_preprocessing.py)

   * Cheat Sheet point 16

      Use as few function parameters as possible.

      [data_processing.py](src/main/python/processing/data_preprocessing.py)

   * Cheat Sheet point 9

      Use short explaining comments for code, that may be not intuitively understandable.
      
      [model_training.py](src/main/python/modeling/model_training.py) 
   
   * Cheat Sheet point 18

      Use a config file!

      [config.py](src/main/python/config.py)
   
### 5 Build Management
   
I used pybuilder as my build management. This was the first time I used a build management in Python 
and after some struggles at the beginning, I now see the advantages of pybuiler :)
   * My [build file](build.py)
   * The files for [automated documentation with sphinx](docs)
   * An [example documentation](tasks/documentation/documentation.html), but it seems that GitHub only shows raw HTML code. [This](https://htmlpreview.github.io/) website can help, to render the documentation even if it does not display everything correctly.

### 6 Unit-Tests

I made unit tests with the python unittest library. These are the two files that implement my tests. When building my project with pybuilder, all tests get run by default.
   * [unit tests I](src/unittest/python/modeling/model_training_tests.py)
   * [unit tests II](src/unittest/python/processing/data_processing_tests.py)
   
### 7 Continuous Delivery

For the CD pipeline, I made use of Travis CI.
Whenever I push new code to my git repo, a new build gets triggered. [This](https://travis-ci.org/github/stefan-beuchert/MovieRecommender) is the corresponding website for this project.

More information can be found in the [properties file](sonar-project.properties)

As proof, that my last build was successful, I embedded this batch:

![travis_build](https://travis-ci.org/stefan-beuchert/MovieRecommender.svg?branch=main)

I also encluded a [screenshot](tasks/travis_ci/travis_ci.PNG) and the [log file](tasks/travis_ci/travis_ci_log.txt).

### 8 IDE

I used the PyCharm IDE for my project.

My first choice for an IDE would have been Visual Studio Code. But after I had decided to implement my project in Python, I chose PyCharm. This was not because of any specific feature, but just the fact that I had heard of PyCharm in the past and wanted to test it out.


Some features that made my life easier while implementing this project are:
* Code completion
* Easy refactoring
* The overall simple UI with the possibility to open multiple tabs and highlight files, that are tracked by git
* The terminal, which I used a lot


Sadly I realized only after implementing most of the core features, that I could have used the professional edition for free because I am a student. This would have allowed me to use .http / .rest files, which can send HTTP-request directly from the IDE. I had to use Postman for this. Also, I could have used integrated support for IPython Notebook, which would have made it possible to run and edit .ipynb files inside of the IDE.

Now I know better for the next time :)

My favorite shortcuts are:
* 'ctrl' + '/' (on the numpad), for commenting out a block of code, or reversing this process
* hitting 'shift' twice, for quickly going in search mode
* 'ctrl' + 'alt' + 'l', for reformating the current file, without going through the suggestion menu

### 9 DSL

My DSL is independent from the movie recommender system. 

The [.dsl file](tasks/dsl/simple.dsl) contains my external DSL code. I made a simple language, that allows simple mathematical operations, by using written language instead of mathematical operators (+, -, *, /).
The [interpreter](tasks/dsl/dsl_interpreter.py) is used to convert the .dsl file into python code and execute each line.
   
### 10 Functional Programming

Throughout my project, I used functional programming as much as possible. 
In the following, you can find the proof of the function concepts with a detailed descriptions in the .py files.

   * Only final data structures
      [model_training.py](src/main/python/modeling/model_training.py)
   * (Mostly) side effect free functions
      [model_training.py](src/main/python/modeling/model_training.py)
   * The use of higher-order functions
      [data_preparation](src/main/python/preparation/data_preparation.py)
      [data_processing.py](src/main/python/processing/data_preprocessing.py)
   * Use closures / anonymous functions
      [data_processing.py](src/main/python/processing/data_preprocessing.py)

