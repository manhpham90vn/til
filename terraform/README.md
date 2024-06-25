# Learn terraform
- terraform and ansible

## Version
```shell
➜  ~ terraform --version
Terraform v1.7.3
on linux_amd64

➜  ~ ansible --version
ansible [core 2.15.9]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/manh/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  ansible collection location = /home/manh/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible
  python version = 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (/usr/bin/python3)
  jinja version = 3.0.3
  libyaml = True
```
## Install
### Install Terraform
```shell
https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
```

### Install Ansible
```shell
https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html
```

## Command
### Terraform init
```shell
terraform init
```

### Terraform show changes
```shell
terraform plan -var-file="vars/terraform.tfvars"
```

### Terraform apply env production
```shell
terraform apply -var-file="vars/terraform.tfvars" -auto-approve
```

### Terraform destroy
```shell
terraform destroy -var-file="vars/terraform.tfvars" -auto-approve
```

## Architecture
- 1 nginx load balancer
- 1 database
- 2 web wordpress web server
