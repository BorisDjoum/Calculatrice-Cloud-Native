terraform {
  required_providers {
    scaleway = {
      source = "scaleway/scaleway"
    }
  }
  required_version = ">= 0.13"
}

provider "scaleway" {
  region = "fr-par"   # Région Scaleway France Paris
  zone   = "fr-par-1" # Zone Scaleway France Paris 1
}

variable "project_name" {
  default = "calculatrice"
}

variable "environment" {
  default = "dev"
}

variable "binome" {
  default = "gilles"
}