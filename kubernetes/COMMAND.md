# Command

## Common

```shell
pod > replicaSet > deployment
```

```shell
kubectl get all
```

### log

```shell
kubectl logs
kubectl logs service/myapp-service
kubectl logs pod/myapp-pod -f
kubectl logs pod/myapp-pod -c nginx-container -f
```

### exec

```shell
kubectl exec -it pod/myapp-pod -c nginx-container -- sh
```

## Name Spaces

```shell
kubectl get namespaces
```

### describe Name Spaces

```shell
kubectl describe namespaces default
```

## Node

```shell
kubectl get node
```

### describe node

```shell
kubectl describe node minikube
```

## Pod

### Deploy pod

```shell
kubectl create -f pod.yml
```

### get pods

```shell
kubectl get pods -o wide
kubectl get pods -A
kubectl get pods -w # watching
```

### describe pod

```shell
kubectl describe pod myapp-pod
kubectl describe pod etcd-minikube -n kube-system
```

### delete pod

```shell
kubectl delete pod myapp-pod
```

## Replication Controllers

### Deploy

```shell
kubectl create -f replicationcontroller.yml
```

### get

```shell
kubectl get replicationcontroller
```

## Replica set

### Deploy Replica set

```shell
kubectl create -f replicaset.yml
```

### get Replica set

```shell
kubectl get replicaset
```

### delete Replica set

```shell
kubectl delete replicaset nginx-rs
```

## Deployment

### Deploy Deployment

```shell
kubectl create -f deployment.yml --record
```

### get Deployment

```shell
kubectl get deployments
```

### delete Deployment

```shell
kubectl delete deployments nginx-deployment
```

### update

```shell
kubectl apply -f deployment.yml
```

### check status deployment

```shell
kubectl rollout status deployment.apps/nginx-deployment
```

### check history

```shell
kubectl rollout history deployment.apps/nginx-deployment
```

### rollback

```shell
kubectl rollout undo deployment.apps/nginx-deployment
```

### update CHANGE-CAUSE

```shell
kubectl patch deployment nginx-deployment --patch '{"metadata": {"annotations": {"kubernetes.io/change-cause": "Update version 1"}}}'
```

## Service

### Deploy Service

```shell
kubectl create -f nodeport.yml
```

### Get url

```shell
minikube service myapp-service --url
minikube service argocd-server -n argocd --url
```

### get Service

```shell
kubectl get services
```

### describe Service

```shell
kubectl describe service myapp-service
```

### Persistent Volume

- get list Persistent Volume

```shell
kubectl get pv
```

### Persistent Volume Claims

- get list Persistent Volume Claims

```shell
kubectl get pvc
```

### Config Maps

- get list Config Map

```shell
kubectl get configmap
```

## Switch Context

```shell
aws eks --region ap-southeast-1 update-kubeconfig --name myCluster
```

### Secrets

- get list secrets

```shell
kubectl get secrets
```

- get secret

```shell
kubectl get secret mydatabase-mysql -o yaml
```

## Helm

### Repo

- list repo

```shell
helm repo list
```

- add repo

```shell
helm repo add bitnami https://charts.bitnami.com/bitnami
```

- search repo

```shell
helm search repo apache
```

- remove repo

```shell
helm repo remove bitnami
```

- update repo

```shell
helm repo update
```

### Chart

- install

```shell
helm install mydatabase bitnami/mysql
helm install mydatabase bitnami/mysql --set auth.rootPassword=toor
helm install mydatabase bitnami/mysql --values values.yaml
helm install mydatabase bitnami/mysql --values values.yaml --dry-run # only create template (not run)
helm install mydatabase bitnami/mysql --namespace mynamespace --create-namespace
```

- template

```shell
helm template mydatabase bitnami/mysql --values values.yaml
```

- upgrade

```shell
helm upgrade -n default mydatabase bitnami/mysql --set auth.rootPassword=toor1
helm upgrade -n default mydatabase bitnami/mysql --values values.yaml
helm upgrade -n default mydatabase bitnami/mysql --values values.yaml --dry-run # only create template (not run)
helm upgrade -n default mydatabase bitnami/mysql --values values.yaml --force --cleanup-on-fail
```

- status

```shell
helm status mydatabase
```

- show note

```shell
helm get notes mydatabase
```

- show values

```shell
helm get values mydatabase
helm get values mydatabase --all
helm get values mydatabase --revision 2
```

- list chart

```shell
helm list
```

- list chart in namespace

```shell
helm list -n mynamespace
```

- uninstall chart

```shell
helm uninstall mydatabase
```

- show history

```shell
helm history mydatabase
```

- rollback

```shell
helm rollback mydatabase 1
```

### Custom chart

- create chart

```shell
helm create mychart
```

- install my chart

```shell
helm install mychart mychart
```

- package chart

```shell
helm package mychart
```
