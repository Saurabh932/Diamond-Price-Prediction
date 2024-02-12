# Diamond Price Prediction MLOps Project

## Project Overview

Welcome to the Diamond Price Prediction MLOps Project! This project aims to predict the price of gemstones using various machine learning algorithms and operationalizing the model with best practices in machine learning operations (MLOps).


## Problem Statement

For this project, we aim to predict the price of gemstones based on various factors such as carat, depth, table, dimensions, cut, color, and clarity. By leveraging historical data on gemstone attributes and prices, we can develop machine learning models to accurately predict the price of gemstones, thereby assisting gemstone traders and buyers in making informed decisions.

## Dataset

We utilize a dataset containing information on various gemstones, including their attributes and corresponding prices. This dataset serves as the foundation for training and evaluating our machine learning models. The features in the dataset include carat, depth, table, dimensions (x, y, z), cut, color, and clarity.

## Objectives

1. Develop machine learning models to predict gemstone prices based on their attributes.
2. Implement best practices in machine learning operations (MLOps) to ensure the scalability, reproducibility, and reliability of the prediction pipeline.
3. Deploy the trained models to production environments for real-time price predictions.

## Key Features

- **Machine Learning Model Development**: Utilize various machine learning algorithms to build predictive models for gemstone prices.
- **MLOps Integration**: Implement MLOps practices to streamline the machine learning workflow, including version control, experimentation tracking, model monitoring, and deployment.
- **Deployment**: Deploy the trained models to production environments, enabling real-time gemstone price predictions.

## Repository Purpose

The purpose of this repository is to demonstrate how modern MLOps practices, combined with machine learning algorithms, can be leveraged to predict gemstone prices accurately. By providing a framework for building and deploying machine learning pipelines, this repository aims to empower businesses and individuals in the gemstone industry to make data-driven decisions.

## How to Use This Repository

1. Clone the repository to your local machine.
2. Install the required dependencies specified in the `requirements.txt` file.
3. Explore the project structure to understand the organization of code, data, and resources.
4. Follow the instructions in the README.md file to run the prediction pipeline and deploy the models to production environments.

## Project Structure

-- src/  
  &emsp;&emsp;|- components/    
  &emsp;&emsp;|- exception/     
  &emsp;&emsp;|- logger/    
  &emsp;&emsp;|- pipeline/  
  &emsp;&emsp;|- utils/   
-- dataset/   
-- artifacts/  
-- mlruns/   
-- airflow/   
-- templates/  
-- static/   
-- .dockerignore  
-- .dvcignore  
-- .gitignore  
-- Dockerfile  
-- docker-compose.yaml  
-- README.md  
-- requirements.txt  
-- setup.py  
-- start.sh

      
## Getting Started

-- To run this project on your local machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Saurabh932/First-Mlops-Project.git
    ```
    ```bash
   cd diamond-price-prediction
   ```
    <br>

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    
    <br>
3. ***Run the Application:***
    To run the Flask web application:
    ```bash
    python app.py
    ```
* Access the application in your web browser at http://localhost:8000.

<br>

4. **Run Apache Airflow DAGs:**
    Start the Airflow web server:
    ```bash
    airflow webserver
    ```
* Access the Airflow UI in your web browser at http://localhost:8080.
* Trigger the DAGs training_pipeline and batch_prediction to train models and perform batch predictions, respectively.

<br>

5. **Run with Docker:**
* If you prefer to use Docker, you can easily run the project with Docker Compose. Simply navigate to the project directory and run:
```bash
docker-compose up --build
```
* And the run:
```bash
docker-compose up
```
<br>

## Training Pipeline


The training pipeline is responsible for training machine learning models using the provided dataset. Here's a brief overview of the training pipeline:

1. **Data Ingestion**: The pipeline loads the dataset and preprocesses it to prepare it for training. This may include tasks such as cleaning the data, handling missing values, and encoding categorical variables.

2. **Model Training**: The preprocessed data is used to train machine learning models using various algorithms. The trained models are evaluated using appropriate metrics to assess their performance.

3. **Model Evaluation**: The trained models are evaluated using validation data to assess their generalization performance. This step helps in selecting the best-performing model for deployment.

## Prediction Pipeline

The prediction pipeline, named "PredictPipeline" in the project, is responsible for making predictions using the trained machine learning model. Here's a brief overview of the prediction pipeline:

1. **Data Loading and Preprocessing**: The pipeline loads the input data and preprocesses it using the same preprocessing steps used during training. This ensures that the input data is compatible with the trained model.

2. **Model Loading**: The trained machine learning model is loaded from the saved artifacts directory (`artifacts/`). This includes both the trained model and the preprocessing artifacts.

3. **Feature Engineering**: If necessary, additional feature engineering steps are performed on the input data to prepare it for prediction. This may involve scaling, encoding, or transforming the features as required by the model.

4. **Prediction**: The preprocessed input data is fed into the loaded model to make predictions. The predicted values are returned as the output of the prediction pipeline.



### Techstack Used:

- Python
- Git
- DVC
- AirFlow
- MLFlow
- Docker



## Airflow Demo

**1. First you have to login:**

![](https://github.com/Saurabh932/First-Mlops-Project/blob/main/images/air-1.jpg)


**2. Then find "gemstone-prediction":**

![](https://github.com/Saurabh932/First-Mlops-Project/blob/main/images/air-2.jpg)


**3. Then you can see the CT pipeline**

![](https://github.com/Saurabh932/First-Mlops-Project/blob/main/images/air-3.jpg)
       

## Web Application Demo

**1. Click the button to procedded:**

![](https://github.com/Saurabh932/First-Mlops-Project/blob/main/images/1-predict.jpg)


**2. Enter the values.**

![](https://github.com/Saurabh932/First-Mlops-Project/blob/main/images/2-predict.jpg)


**3. Click on submit to get final Result**

![](https://github.com/Saurabh932/First-Mlops-Project/blob/main/images/3-predict.jpg)
