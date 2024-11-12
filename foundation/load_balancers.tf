resource "scaleway_lb_ip" "dev" {}

resource "scaleway_lb" "dev" {
  ip_id = scaleway_lb_ip.dev.id
  name  = "${var.project_name}-lb-dev"
  type  = "LB-S"
}

resource "scaleway_lb_ip" "prod" {}

resource "scaleway_lb" "prod" {
  ip_id = scaleway_lb_ip.prod.id
  name  = "${var.project_name}-lb-prod"
  type  = "LB-S"
}