terraform {
  required_version = "=1.7.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "=5.35.0"
    }
  }
}

provider "aws" {
  region = "ap-southeast-1"
}

data "aws_availability_zones" "Availability_Zones" {}

locals {
  azs = slice(data.aws_availability_zones.Availability_Zones.names, 0, 3)
  vpc_cidr = "10.0.0.0/16"
}

module "ssh" {
  source = "./ssh"
  ssh_key_name = var.ssh_key_name
}

module "vpc" {
  source = "./vpc"
  cidr_block = local.vpc_cidr
  private_subnet = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 4, k)]
  public_subnet  = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k + 48)]
  availability_zone = local.azs
  ssh_ip = var.ssh_ip
}

module "ec2" {
  source = "./ec2"
  countInstancesPublic = 1 // 1 instance for nginx load balancer
  countInstancesPrivate = 2 // 2 instances for web server
  countInstancesPrivateDatabase = 1 // 1 instance for database
  ami = var.ami
  instance_type = var.instance_type
  key_name = module.ssh.data.key_name
  public_subnet_id = module.vpc.data.public_subnet_id
  private_subnet_id = module.vpc.data.private_subnet_id
  public_security_group_id = module.vpc.data.public_security_group_id
  private_security_group_id = module.vpc.data.private_security_group_id
  private_key = module.ssh.data.private_key
}


output "ec2" {
  value = {
    public_ip = module.ec2.data.public_ip
  }
}
