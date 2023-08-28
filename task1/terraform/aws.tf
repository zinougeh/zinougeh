provider "aws" {
  region = "us-east-1"  # Change this to your desired region
}

resource "aws_instance" "ec2_instance" {
  ami           = "ami-0261755bbcb8c4a84"  # Ubuntu
  instance_type = "t2.medium"
  associate_public_ip_address = true
  key_name = "jenkins"
  tags = {
    Name = "EC2_INSTANCE_BY_JENKINS"
  }
}

output "public_ip" {
  value = aws_instance.ec2_instance.public_ip
}
