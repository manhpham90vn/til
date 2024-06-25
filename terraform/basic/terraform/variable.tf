variable "instance_type" {
  type = string
  description = "Instance type of the EC2"

  validation {
    condition = contains(["t2.micro", "t3.small"], var.instance_type)
    error_message = "Value not allow."
  }
}

variable "ami" {
  type = string
  description = "AMI ID"
  default = ""
}

variable "ssh_key_name" {
  type = string
  description = "SSH Key Pair Name"
  default = ""
}

variable "ssh_ip" {
  type        = string
  description = "IP address to allow SSH access"
  default     = ""
}
