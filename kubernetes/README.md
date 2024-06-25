# Learn Kubernestes
- minikube and kubernetes

## Kuberneters
- Kubernetes is an open-source container orchestration system for automating software deployment, scaling, and management.

## Cluster
- a set of node machines which are running the Containerized Application (Worker Nodes) or control other Nodes (Master Node)

## Node
- a node refers to a physical or virtual machine that serves as a worker machine in a Kubernetes cluster. Each node is responsible for running containers and managing networking, storage, and other components required to run applications.

### Worker Node
- A node, also known as a worker or a minion, is a machine where containers (workloads) are deployed. Every node in the cluster must run a container runtime, as well as the below-mentioned components, for communication with the primary network configuration of these containers.
- Each node in a Kubernetes cluster can run multiple pods, which are the smallest deployable units in Kubernetes, consisting of one or more containers that share resources and networking

### Master Node
- The Kubernetes master node handles the Kubernetes control plane of the cluster, managing its workload and directing communication across the system.

## Pod
- The basic scheduling unit in Kubernetes is a pod, which consists of one or more containers that are guaranteed to be co-located on the same node. Each pod in Kubernetes is assigned a unique IP address within the cluster, allowing applications to use ports without the risk of conflict. Within the pod, all containers can reference each other.

- A container resides inside a pod. The container is the lowest level of a micro-service, which holds the running application, libraries, and their dependencies.

## ReplicationController

## ReplicaSet

## Service
- a service is an abstract way to expose an application running on a set of Pods (one or more) as a network service. It provides a stable endpoint (IP address and port) that other applications can use to communicate with the Pods backing the Service

### LoadBalancer

### NodePort

### ClusterIP

## Deployment

## Volume

### emptyDir

### hostPath

### Persistent Volumes

### persistentVolumeClaim

## Network

### Core DNS

### Reverse Proxy

## Helm

### Chart
- install

- upgrade

- rollback

- uninstall
