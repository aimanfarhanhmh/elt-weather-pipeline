terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.18.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project = var.project
  region  = "asia-southeast1-a"
}

resource "google_storage_bucket" "terraform-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = false

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "terraform-dataset" {
  dataset_id = var.bq_dataset_name
  location = var.location
}