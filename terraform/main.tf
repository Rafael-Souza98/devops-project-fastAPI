module "kubernetes" {
    source       = "./kubernetes"
    cidr_block   = "10.27.0.0/16"
    project_name = "restapi"
    region       = "us-east-2"
    tags = {
        Owner                  = "Rafael"
        "Managed by terraform" = "true"
    }
}