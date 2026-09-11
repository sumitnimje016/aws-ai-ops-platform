terraform {
  backend "s3" {
    bucket = "aws-ai-ops-terraform-state-20260911"
    key    = "aws-ai-ops/terraform.tfstate"
    region = "ap-south-1"
  }
}
