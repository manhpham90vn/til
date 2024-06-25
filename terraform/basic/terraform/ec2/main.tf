locals {
  user = "ubuntu"
  name = "MyEC2Instance"
}

resource "aws_instance" "MyEC2InstancePublic" {
  count                       = var.countInstancesPublic
  ami                         = var.ami
  instance_type               = var.instance_type
  key_name                    = var.key_name
  subnet_id                   = var.public_subnet_id[count.index]
  vpc_security_group_ids      = [var.public_security_group_id]
  associate_public_ip_address = true

  timeouts {
    create = "1h30m"
    update = "2h"
    delete = "20m"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt install -y git"
    ]
  }

  connection {
    type        = "ssh"
    user        = local.user
    private_key = var.private_key
    host        = self.public_ip
  }

  tags = {
    Name = "${local.name}-${count.index}-Public"
  }
}

resource "aws_eip" "Elastic_IP_MyEC2InstancePublic" {
  domain = "vpc"
  count = var.countInstancesPublic
  instance = aws_instance.MyEC2InstancePublic[count.index].id

  tags = {
    Name = "${local.name}-Elastic-IP"
  }
}

resource "aws_instance" "MyEC2InstancePrivate" {
  count                       = var.countInstancesPrivate
  ami                         = var.ami
  instance_type               = var.instance_type
  key_name                    = var.key_name
  subnet_id                   = var.private_subnet_id[count.index]
  vpc_security_group_ids      = [var.private_security_group_id]
  
  tags = {
    Name = "${local.name}-${count.index}-Private"
  }
}

resource "aws_instance" "MyEC2InstancePrivateDatabase" {
  count                       = var.countInstancesPrivateDatabase
  ami                         = var.ami
  instance_type               = var.instance_type
  key_name                    = var.key_name
  subnet_id                   = var.private_subnet_id[count.index]
  vpc_security_group_ids      = [var.private_security_group_id]
  
  tags = {
    Name = "${local.name}-${count.index}-Private-Database"
  }
}

resource "local_file" "config_hosts" {
  content = templatefile("${path.module}/hosts.tpl",
    {
      nginx_lb = aws_instance.MyEC2InstancePublic.*.public_ip
      mysql_server = aws_instance.MyEC2InstancePrivateDatabase.*.private_ip
      php_fpm_servers = aws_instance.MyEC2InstancePrivate.*.private_ip
    }
  )
  filename = "${path.root}/../ansible/hosts"
}

resource "null_resource" "run_ansible_playbook" {
  provisioner "local-exec" {
    working_dir = "${path.root}/.."
    command = "ansible-playbook -i ansible/hosts ansible/nginx_lb.yaml -u ${local.user} --private-key=terraform/${var.key_name}.pem"
  }
}