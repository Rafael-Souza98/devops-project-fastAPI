
resource "helm_release" "sealed_secrets" {
  name       = "sealed-secrets"
  repository = "https://bitnami-labs.github.io/sealed-secrets"
  chart      = "sealed-secrets"
  version    = "2.17.0"
  namespace  = "kube-system"


  set {
    name  = "fullnameOverride"
    value = "sealed-secrets-controller"
  }

}