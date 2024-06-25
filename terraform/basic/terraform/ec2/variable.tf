variable "countInstancesPublic" {
  type        = number
  description = "Number of instances to create in public subnet"
  default     = 1
}

variable "countInstancesPrivate" {
  type        = number
  description = "Number of instances to create in private subnet"
  default     = 1
}

variable "countInstancesPrivateDatabase" {
  type        = number
  description = "Number of instances to create in private subnet for database"
  default     = 1
}

variable "ami" {
  type = string
  description = "AMI of the EC2"
  default = ""
}

variable "instance_type" {
  type = string
  description = "Type of instance"

  validation {
    condition = contains(["t2.micro", "t3.small"], var.instance_type)
    error_message = "Value not allow."
  }
}

variable "key_name" {
  type = string
  description = "Key Pair"
  default = ""
}

variable "private_key" {
  type = string
  description = "Private Key"
  default = ""
  
}

variable "public_subnet_id" {
  type = list(string)
  description = "Subnet Public ID"
  default = []
}

variable "private_subnet_id" {
  type = list(string)
  description = "Subnet Private ID"
  default = []
}

variable "public_security_group_id" {
  type = string
  description = "List of security group IDs public"
  default = ""
}

variable "private_security_group_id" {
  type = string
  description = "List of security group IDs private"
  default = ""
}

variable "ssh_ip" {
  type        = string
  description = "IP address to allow SSH access"
  default     = ""
}
