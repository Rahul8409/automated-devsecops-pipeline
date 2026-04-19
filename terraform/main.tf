terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = ">= 2.0.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "flask_app" {
  name = "devsecops-flask-app"
  keep_locally = true
}

resource "docker_container" "flask_container" {
  name = "terraform-container"
  image = docker_image.flask_app.name

  ports {
    internal = var.container_port
    external = var.external_port
  }
}

