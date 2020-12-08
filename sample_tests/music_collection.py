class Song:
    def __init__(self, name, artist, album, track_number):
        self.name = name
        self.artist = artist
        self.album = album
        self.track_number = track_number
        new_artist = Artist(artist)
        new_album = Album(album, artist)

        artist.add_song(self)
        album.add_song_to_album(self)


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = {}
        self.songs = {}

    def add_song(self, song):
        self.songs[song.name] == song

        return True

    def add_album(album):
        return True

class Album:
    def __init__(self, name, artist):
        self.name = name
        self._artist = artist
        self.tracks = {}

    def add_song_to_album(song):
        self.tracks[song.track_number] = song
        return

"""
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = {}

    def add_song(song):
        self.songs[] = song
        """

"""
Music Collection
song
artist
album
playlist

album has
> 1 artist
> multiple songs

artist has
> multiple albums

songs has
> 1 artist
> 1 album

playlists has
> many songs

"""

