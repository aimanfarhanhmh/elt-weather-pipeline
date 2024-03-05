variable "credentials" {
  description = "My Credentials"
  default = "~/.gc/project/terraform-runner.json"
}

variable "project" {
  description = "Project Name"
  default = "weather-elt-pipeline"
}

variable "location" {
  description = "Project Location"
  default = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default = "weather_data"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default = "weather-elt-pipeline-forecast-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARD"
}