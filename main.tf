terraform {
  required_providers {
    spotify = {
      source  = "conradludgate/spotify"
      version = "0.2.7"
    }
  }
}

provider "spotify" {
  client_id     = var.spotify_client_id
  client_secret = var.spotify_client_secret
  redirect_uri  = "http://localhost:27228/spotify_callback"
}

resource "spotify_playlist" "my_playlist" {
  name        = "My Terraform Playlist"
  description = "A playlist created using Terraform"
  public      = true
}
resource "spotify_playlist_tracks" "my_playlist_tracks" {
  playlist_id = spotify_playlist.my_playlist.id
  tracks      = [
    "spotify:track:3I3kZyHUtEA9Y59rJkxtk6",  # Example track URIs
    "spotify:track:1301WleyT98MSxVHPZCA6M"
  ]
}