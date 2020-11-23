import pytest
from music_collection import Song,Artist

@pytest.fixture
def song():
    song_name = "Dynamite"
    artist_name = "BTS"
    album_name = "BE"
    track_number = 1
    return Song(song_name, artist_name, album_name, track_number)

@pytest.fixture
def artist():
    artist_name = "BTS"
    return Artist(artist_name)

def test_create_new_song_with_new_artist_and_album(song, artist):
    assert song.name == "Dynamite"
    assert song.artist == "BTS"
    assert song.album == "BE"
    assert song.track_number == 1
    assert song.album in artist.albums
    assert song.name in artist.songs

def test_create_artist(artist):
    assert artist.name == "BTS"
