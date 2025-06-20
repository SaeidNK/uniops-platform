variable "aws_region" {
  default = "eu-west-2"  # London
}

variable "ami_id" {
  description = "Ubuntu 22.04 AMI ID"
  type        = string
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "Your AWS EC2 Key Pair Name"
  type        = string
}
