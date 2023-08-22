provider "aws" {
  region = "us-east-1"  # Change this to your desired region
}

resource "aws_instance" "ec2_instance" {
  ami           = "ami-0453898e98046c639"  # Amazon Linux 2 AMI ID for us-west-2
  instance_type = "t2.micro"
  associate_public_ip_address = true
  tags = {
    Name = "EC2_INSTANCE_BY_JENKINS"
  }
}
