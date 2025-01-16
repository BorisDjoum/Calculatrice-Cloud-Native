resource "scaleway_rdb_instance" "dev" {
  name           = "${var.project_name}-db-dev"
  node_type      = "DB-DEV-S"
  engine         = "PostgreSQL-14"
  is_ha_cluster  = false
  disable_backup = true
}

resource "scaleway_rdb_instance" "prod" {
  name           = "${var.project_name}-db-prod"
  node_type      = "DB-GP-XS"
  engine         = "PostgreSQL-14"
  is_ha_cluster  = true
  disable_backup = false
}






