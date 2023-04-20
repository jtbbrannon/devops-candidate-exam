data "archive_file" "lambda_script" {
  type = "zip"

  source_dir  = "${path.module}/lambda_function.py"
  output_path = "${path.module}/output.zip"
}

resource "aws_lambda_function" "lambda" {
  function_name = "jim_brannon_devops_candidate_exam"

  runtime = "python3.9"
  handler = "lambda_function.lambda_handler"

  filename = "${path.module}/output.zip"
  source_code_hash = data.archive_file.lambda_script.output_base64sha256

  role = data.aws_iam_role.lambda.arn

  environment {
    variables = {
      subnet_id = aws_subnet.main.id
    }
  }

  timeout = 5
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