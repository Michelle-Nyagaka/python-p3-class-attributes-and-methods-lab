class Song:
    # Class attributes: store data related to the class as a whole
    count = 0              # Total number of Song instances
    artists = []           # Unique list of artists
    genres = []            # Unique list of genres
    artist_count = {}      # Dictionary: artist -> number of songs
    genre_count = {}       # Dictionary: genre -> number of songs

    def __init__(self, name, artist, genre):
        # Instance attributes: data specific to this song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level data whenever a new song is created
        Song.add_song_to_count()         # Increment total song count
        Song.add_to_artists(self.artist) # Add artist to unique artists list
        Song.add_to_genres(self.genre)   # Add genre to unique genres list
        Song.add_to_artist_count(self.artist) # Update artist histogram
        Song.add_to_genre_count(self.genre)   # Update genre histogram

    # Class method to increment the song count
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Class method to add a new artist to the list if not already present
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # Class method to add a new genre to the list if not already present
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    # Class method to increment the count of songs by a specific artist
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    # Class method to increment the count of songs of a specific genre
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
