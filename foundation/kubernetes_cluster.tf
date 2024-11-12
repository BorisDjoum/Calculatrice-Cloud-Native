resource "scaleway_k8s_cluster" "main" {
  name    = "${var.project_name}-cluster-${var.environment}"
  version = "1.26.0"
  cni     = "cilium"
  delete_additional_resources = true
}

resource "scaleway_k8s_pool" "main" {
  cluster_id = scaleway_k8s_cluster.main.id
  name       = "default-pool"
  node_type  = "DEV1-M"
  size       = 3
}
