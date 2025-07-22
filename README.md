## MLOps-deploy

A beginner-friendly MLOps project demonstrating the end-to-end deployment of an Iris flower classification machine learning model using Docker and Kubernetes.

This project trains a machine learning model to classify Iris flower species based on input features. The model is saved using `joblib`, wrapped inside a FastAPI application, containerized with Docker, and deployed on a Kubernetes cluster.

### Features

- Trains a simple ML model using scikit-learn
- Model persistence with `joblib`
- Provides REST API endpoints for prediction via FastAPI
- Dockerized for easy container deployment
- Kubernetes manifests for Deployment and Service
- Demonstrates real-world MLOps workflows: build, containerize, deploy


### Prerequisites

- Python 3.8+
- Docker
- Kubernetes cluster (e.g., Minikube, Docker Desktop Kubernetes)
- kubectl CLI configured
- Git

### Getting Started

## 1. Clone the repository

git clone https://github.com/pragnyaD8/MLOps-deploy.git
cd MLOps-deploy

## 2. Build Docker image

docker build -t iris-app .

## 3. Run Docker container locally

docker run -p 2000:2000 iris-app
Open http://localhost:2000/docs to test the API.

## 4. Push Docker image to Docker Hub

docker tag iris-app your-dockerhub-username/iris-app:latest
docker login
docker push your-dockerhub-username/iris-app:latest

## 5. Deploy on Kubernetes

kubectl apply -f iris-deployment.yaml
kubectl apply -f iris-service.yaml

## 6.Check pods:

kubectl get pods 

After deployment, access the application using the NodePort or Ingress URL exposed by the Kubernetes service.  
Use `kubectl get svc` to to retrieve the external access URL or IP.

Access URL:
http://localhost:<NodePort>

## 7.API Usage

Send POST requests to /predict endpoint with JSON input features. Example payload:

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
