terraform {
  required_providers {
    spotify = {
      source  = "conradludgate/spotify"
      version = "0.1.1"
    }
  }
}

provider "spotify" {
  oauth_client_id     = var.spotify_client_id
  oauth_client_secret = var.spotify_client_secret
  redirect_uri        = var.spotify_redirect_uri
  access_token        = var.spotify_access_token
}

resource "spotify_playlist" "my_playlist" {
  name        = "My Terraform Playlist"
  description = "A playlist created with Terraform"
  public      = true
}
