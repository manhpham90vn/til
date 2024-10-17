# Learn Kubernestes

- minikube and kubernetes

## Kuberneters

- là một nền tảng mã nguồn mở dùng để tự động hóa việc triển khai (deployment), quản lý và mở rộng các ứng dụng container

## Cluster

- Tập hợp các node hoạt động cùng nhau như một hệ thống thống nhất. Kubernetes sẽ sử dụng các node này để triển khai và quản lý các ứng dụng

## Node

- Là một máy chủ vật lý hoặc ảo trong cluster Kubernetes. Mỗi node sẽ chứa các pod và được quản lý bởi control plane của Kubernetes

### Worker Node

- Là các máy chủ nơi các ứng dụng được triển khai và chạy. Worker Node chịu trách nhiệm thực thi các tác vụ thực tế, như chạy các container trong các pod.

### Master Node

- Là thành phần trung tâm của Kubernetes chịu trách nhiệm quản lý toàn bộ cluster

## Pod

- Là đơn vị nhỏ nhất trong Kubernetes, chứa một hoặc nhiều container (thường là Docker container) cùng chia sẻ mạng và lưu trữ

## ReplicationController

## ReplicaSet

- là một đối tượng dùng để đảm bảo rằng một số lượng cụ thể các pod luôn chạy trong cluster. Nó là thành phần quan trọng giúp duy trì sự sẵn sàng của ứng dụng, bằng cách tự động tạo mới hoặc loại bỏ các pod để đảm bảo đúng số lượng pod mong muốn.

## Service

- là một đối tượng giúp quản lý và cung cấp các cách thức để tiếp cận và giao tiếp với các nhóm Pod trong cluster
- các loại service thường dùng là
  - ClusterIP
  - NodePort
  - LoadBalancer
  - ExternalName

### LoadBalancer

- Tích hợp với các dịch vụ Load Balancer của các nhà cung cấp đám mây như AWS, GCP, hoặc Azure.
- Tự động tạo một địa chỉ IP bên ngoài và phân phối lưu lượng truy cập vào service đến các Pod tương ứng.
- Thường được sử dụng khi bạn muốn truy cập ứng dụng từ bên ngoài với một địa chỉ IP tĩnh.

### NodePort

- Mở một cổng trên mỗi node của cluster và ánh xạ nó đến các Pod được service quản lý.
- Cho phép truy cập từ bên ngoài cluster bằng cách sử dụng địa chỉ IP của node và nodePort.
- Thích hợp cho các tình huống mà bạn cần truy cập ứng dụng từ bên ngoài mà không cần cấu hình phức tạp.

### ClusterIP

- Tạo một địa chỉ IP nội bộ để các Pod khác trong cùng cluster có thể truy cập.
- Không thể truy cập từ bên ngoài cluster.
- Thích hợp cho các ứng dụng hoặc dịch vụ chỉ cần giao tiếp nội bộ.

### ExternalName

- Ánh xạ service đến một tên DNS bên ngoài cluster.
- Không liên quan đến các Pod hay IP trong cluster mà đơn giản là cung cấp một cách để truy cập các dịch vụ bên ngoài bằng tên DNS.

## Deployment

- là một đối tượng dùng để quản lý việc triển khai và mở rộng các ứng dụng container dưới dạng Pod. Nó giúp tự động hoá quá trình tạo mới, cập nhật, mở rộng và rollback các phiên bản của ứng dụng một cách dễ dàng và có kiểm soát.

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
