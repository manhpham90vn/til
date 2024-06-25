output "data" {
  value = {
    public_ip = [for instance in aws_instance.MyEC2InstancePublic : format("IP V4: %s", instance.public_ip)]
  }
}