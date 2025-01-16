resource "scaleway_domain_record" "main" {
  dns_zone = "kiowy.net"
  name     = "calculatrice-${var.binome}-polytech-dijon"
  type     = "A"
  data     = scaleway_lb_ip.prod.ip_address
  ttl      = 300
}

resource "scaleway_domain_record" "dev" {
  dns_zone = "kiowy.net"
  name     = "calculatrice-dev-${var.binome}-polytech-dijon"
  type     = "A"
  data     = scaleway_lb_ip.dev.ip_address
  ttl      = 300
}