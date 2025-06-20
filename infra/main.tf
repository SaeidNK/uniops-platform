provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "uniops_node" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "UniOps-Monitoring-Node"
  }
}
