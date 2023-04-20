locals {
    basename = "${path.module}/output"
    out_zip = "${local.basename}.zip"
}




resource "aws_subnet" "main" {
  vpc_id     = data.aws_vpc.vpc.id
  cidr_block = "10.0.24.0/24"

  tags = {
    Name = "jim.brannon"
  }
}



output "subnet_id" {
  value = aws_subnet.main.id
}