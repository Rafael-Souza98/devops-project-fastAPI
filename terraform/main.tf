module "kubernetes" {
  source = "git@github.com:Rafael-Souza98/terraform-for-aws.git"

  project_name = "project-restapi"
  instance_types = [ "t3.medium" ]
  region = "us-east-2"
}