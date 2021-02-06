# Movie Recommender System

## Badges
(https://travis-ci.org/stefan-beuchert/MovieRecommender.svg?branch=main)

## Exercise A for Advanced Software Engineering

### General
This repository contains a backend, that can be used to get movie recommendations based on a dataset of movies represented by documents.
But this software is not only limited to movie datasets. By simply changing some values in the config.py, 
this backend be used as a recommender system for all sorts of documents.


### Prerequisites
* (Movie-)Dataset (I included a small sample under src/data)
* MongoDB server
* Postman (for Requests)

### Handling
1. Clone this repository
2. Create a virtual environment
3. Install pybuilder 

(`pip install pybuilder`)
4. Start MongoDb
5. Make necessary adjustments in config.py (especially for the database and dataset paths)
6. Build the project 

(`pyb publish`)
7. Install the target 

( `pip install target/dist/ContentBasedRecommenderSystem-1.0.dev0/dist/ContentBasedRecommenderSystem-1.0.dev0.tar.gz`)
8. Start the backend 

(`start_api.py`)
9. Post HTTP-requests via a browser or postman
10. Enjoy :)

## Exercise B for Advanced Software Engineering
### 1 UML
   
I made 3 UML diagrams for this project.
   * [Use Case diagram](tasks/uml_diagrams/use_case_diagram.png)
   * [Sequence diagram](tasks/uml_diagrams/sequence_diagram.png)
   * [Activity diagram](tasks/uml_diagrams/activity_diagram.png)
  
### 2 DDD

### 3 Metrics

### 4 Clean Code Development
   
A cheat sheet with my most important clean code principles:
   * [Cheat Sheet](tasks/clean_code_cheat_sheet.py)
   
and the five points, that proof my use of clean code:
   * A
   * B
   * C
   * D
   * E
   
### 5 Build Management
   
I used pybuilder as my build management. This was the first time I used a build management in Python 
and after some struggles at the beginning, I now see the advantages of pybuiler :)
   * [build file](build.py)
   * [automated documentation with sphinx](docs)
   * [example document](tasks/documentation/documentation.html)
<<<<<<< HEAD
   
For unit tests see point 6
=======
   For unit tests see point 6
   
>>>>>>> c35597c482dc306d0aec164153587bb97f3d94f3
### 6 Unit-Tests

   * [unit tests I](src/unittest/python/modeling/model_training_tests.py)
   * [unit tests II](src/unittest/python/processing/data_processing_tests.py)
   
### 7 Continuous Delivery

### 8 IDE

   * [PyCharm](tasks/ide_pycharm.md)
   
### 9 DSL

   * [DSL](tasks/dsl)
   
### 10 Functional Programming
