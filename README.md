## Deploying Machine Learning Models as a Scalable Web Service

---

### Introduction:
Contrary to what you may believe, most data science projects never end up in production. The reasons vary spanning organization issues, project management issues, data issues etc... Moreover, there are large organizations that still struggle to get models off of their Data Scientist's laptops and into production. This lab will introduce you FastAPI for serving machine learning models as an API. 

An __API__ (Applications Programming Interface) is a set of functions and procedures for building and integrating software.

#### Before you start
1. Review the introduction to fastapi 

#### Instructions:
1. Create a new virtual environment 
1. Install the requirements.txt 
1. Run the Jupyter notebook that trains and produces a machine learning model in the `models` dir
1. Create a Pydantic model to validate incoming data to our API 
1. Create a `main.py` that uses your pydantic model (`models.py`) and inference pipeline (provided in `score.py`) to serve predictions
1. Run the sample payload script to ensure your machine learning web service works properly (the test case does the same thing)



