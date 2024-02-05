Create a source code in Python using Flask web framework (app.y)
Test it locally on local host
------------------------------------------------------------------
Create a Docker image (Dockerfile)
Creating a Docker file:
1) FROM python:3-alpine3.15 | Base Image, alpine because it is a lighter version
2) WORKDIR /app | folder that contains source codes
3) COPY . /app | copy all source code working directory
4) RUN pip install flask | Install flask framework, as this is a requirement
5) EXPOSE 3000 | Exposing the port (can be anything)
6) CMD python ./app.py | create a entrypoint, run python file <dir>
------------------------------------------------------------------
Creating an image and pushing to docker hub:
1) docker build -t anjan98/webapp-flask:v1 .| building the image locally with tag as v1
2) docker push anjan98/webapp-flask:v1
------------------------------------------------------------------
Running on Kubernetes
1) Create a pod using a manifest file (pod.yaml)
2) Create a service to expose to the network (Service.yaml)
3) minikube services web-service (service name) --url (if using minikube)
4) kubectl get svc web-service and in browser <ext ip:8080> (if in kubernetes)

------------------------------------------------------------------
Manifest for updating image
1) create a deployment using deployment-rolling.yaml file
2) After running the service enter the version at the end to see Version 2 (<ext.ip>:port/version)
