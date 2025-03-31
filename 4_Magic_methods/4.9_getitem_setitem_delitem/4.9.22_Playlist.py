class Song:
    def __init__(
        self,
        title: str,
        artist: str
    ):
        self.title = title
        self.artist = artist
    
class Playlist:
    def __init__(
        self       
    ):
        self.songs: list = []
        
    def __getitem__(
        self,
        index: int
    ):
        return self.songs[index]
    
    def __setitem__(
        self,
        index: int,
        song: Song
    ):
        self.songs.insert(index, song)
        
    def add_song(
        self,
        song: Song
    ):
        self.songs.append(song)
        
        
        
#TESTS

playlist = Playlist()
assert len(playlist.songs) == 0
assert isinstance(playlist, Playlist)
playlist.add_song(Song("Paradise", "Coldplay"))
assert playlist[0].title == 'Paradise'
assert playlist[0].artist == 'Coldplay'
assert len(playlist.songs) == 1

playlist[0] = Song("Resistance", "Muse")
assert playlist[0].title == 'Resistance'
assert playlist[0].artist == 'Muse'
assert playlist[1].title == 'Paradise'
assert playlist[1].artist == 'Coldplay'

playlist[1] = Song("Helena", "My Chemical Romance")
assert playlist[1].title == 'Helena'
assert playlist[1].artist == 'My Chemical Romance'

assert playlist[2].title == 'Paradise'
assert playlist[2].artist == 'Coldplay'
print('Good')