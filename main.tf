terraform {
 required_providers {
   spotify = {
     source = "conradludgate/spotify"
     version = "0.1.1"
   }
 }
}
provider "spotify" {
 client_id     = var.spotify_client_id
 client_secret = var.spotify_client_secret
 redirect_uri  = var.spotify_redirect_uri
 token         = var.spotify_access_token
}
resource "spotify_playlist" "my_playlist" {
 name        = "My Terraform Playlist"
 description = "A playlist created with Terraform"
 public      = true
}