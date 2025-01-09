terraform {
  required_providers {
    aws ={
        source = "hashicorp/aws"
        version = "5.82.2"
    }
    helm ={
        source = "hashicorp/helm"
        version = "2.15"
    }
  }
}

provider "aws" {}


provider "kubernetes" {
  host                   = module.kubernetes.endpoint
  cluster_ca_certificate = base64decode(module.kubernetes.cluster_certificate_authority)
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    args        = ["eks", "get-token", "--cluster-name", module.kubernetes.cluster_name]
    command     = "aws"
  }
}

