# Generic Terraform starter — variables only, no real account or region hard-coded.
variable "region" { type = string }
variable "cluster_name" { type = string }
variable "environment" { type = string, default = "lab" }

# Example provider block — fill in your own provider and version in a real project.
# terraform {
#   required_providers {
#     aws = { source = "hashicorp/aws", version = "~> 5.0" }
#   }
# }
#
# resource "aws_eks_cluster" "platform" {
#   name     = var.cluster_name
#   role_arn = "<your-cluster-role-arn>"
#   vpc_config { subnet_ids = ["<your-subnet-ids>"] }
# }
output "cluster_name" { value = var.cluster_name }
output "environment" { value = var.environment }
