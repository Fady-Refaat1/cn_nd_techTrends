# The first project in cloud native nanodegree program Udacity 

## Running TechTrends Project

### Build the docker image 
```sh
docker build -t YOUR_DOCKER_HUB_USERNAME/techtrends .
```

### Run the docker image
```sh
docker run -d -p 7111:3111 YOUR_DOCKER_HUB_USERNAME/techtrends
```

### Access the application on port 7111

![alt text](https://github.com/Fady-Refaat1/cn_nd_techTrends/blob/main/screenshots/docker-run-local.png)

### Work with kubernetes 

<li>Start your virtual box by </li>
```sh
vagrant up 
```

<li>ssh into it</li>
```sh
vagrant ssh 
```

<li>Login as Administrator</li>
```sh
sudo su
```

<li> Install kubernetes </li>
```sh
curl -sfL https://get.k3s.io | sh -
```

<li>Create kubernetes files (namespace.yaml ,deploy.yaml, service.yaml) </li>

<li>Apply kubernetes files</li>
```sh
kubectl apply -f namespace.yaml
kubectl apply -f deploy.yaml
kubectl apply -f service.yaml
```

### Work with Argocd
<li>Install argocd</li>
```sh
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
<li>Create argocd/argocd-nodeport.yaml file</li>

```sh
kubectl apply -f argocd-nodeport.yaml
```
<li>Login to argocd and deploy the files in the argocd folder</li>
