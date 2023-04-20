resource "aws_subnet" "main" {
  vpc_id     = data.aws_vpc.vpc.id
  cidr_block = "10.0.24.0/24"

  tags = {
    Name = "jim.brannon"
  }
}

