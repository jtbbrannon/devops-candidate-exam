pipeline{
    agent any
    stages{
        stage("TF Init"){
            steps{
                echo "Executing Terraform Init"
                sh "terraform init"
            }
        }
        stage("TF Validate"){
            steps{
                echo "Validating Terraform Code"
                sh "terraform validate"
            }
        }
        stage("TF Plan"){
            steps{
                echo "Installing python dependencies"
                sh "python --version"
                sh "python -m venv venv"
                sh "source venv/bin/activate"
                sh "pip install -r requirements.txt"

                sh "mkdir ./output"
                sh "cp -r ./venv/lib/*/site-packages/* ./output"
                sh "cp lambda_function.py ./output"

                echo "Executing Terraform Plan"
                sh "terraform plan"
            }
        }
        stage("TF Apply"){
            steps{
                echo "Executing Terraform Apply"
            }
        }
        stage("Invoke Lambda"){
            steps{
                echo "Invoking your AWS Lambda"
                sh "aws --version"
                sh "aws lambda list-functions"
            }
        }
    }
}
