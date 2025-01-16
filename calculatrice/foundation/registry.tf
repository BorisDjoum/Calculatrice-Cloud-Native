resource "scaleway_registry_namespace" "main" {
  name        = "${var.project_name}-${var.environment}"
  description = "Container registry for ${var.project_name}"
}
