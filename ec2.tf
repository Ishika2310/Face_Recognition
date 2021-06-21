provider "aws" {
  region     = "ap-south-1"
  profile = "default"
}

resource "aws_instance" "instance1" {
  ami               = "ami-0e306788ff2473ccb"
  availability_zone = "ap-south-1a"
  instance_type     = "t2.micro"
  key_name = "task62"

  tags = {
    Name = "tf_instance"
  }
}

resource "aws_ebs_volume" "volume1" {
  availability_zone = "ap-south-1a"
  size              = 5
  tags = {
    Name = "tf_volume"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.volume1.id
  instance_id = aws_instance.instance1.id
}
