provider "aws" {
  region = "ap-south-1"
}

#security-groups-for-web-applications
resource "aws_security_group" "web_sg" {
  name        = "web_sg"
  description = "Allow HTTP and SSH"

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


#create-EC2-instances

resource "aws_instance" "web" {
  ami           = "ami-0f1dcc636b69a6438"  # Amazon Linux 2 AMI (update for your region)
  instance_type = "t2.micro"
  key_name      = "my-ubuntu-key-pair" # Replace with your actual key pair
  security_groups = [aws_security_group.web_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y httpd
              echo "Hello from Terraform Web App!" > /var/www/html/index.html
              sudo systemctl start httpd
              sudo systemctl enable httpd
              EOF

  tags = {
    Name = "Terraform-WebApp"
  }
}
