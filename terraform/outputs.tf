output "vpc_id" {
  description = "ID of the AWS VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "internet_gateway_id" {
  description = "ID of the Internet Gateway"
  value       = aws_internet_gateway.main.id
}

output "aws_region" {
  description = "AWS region"
  value       = var.aws_region
}
