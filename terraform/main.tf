# configure the S3 backend for storing state. This allows different
# team members to control and update terraform state.
terraform {
  backend "s3" {
    # This must be updated for each unique deployment/stage!
    # should  be of the form services/APP_NAME/STAGE/terraform.tfstate
    # We can't use variables in the key name here, so we need to be extra
    # careful with this!
    key = "services/hitide/terraform.tfstate"
    region = "us-west-2"
  }
}