def make_album(artist, album_title, song_number=None):
  if song_number:
    album = {'artist': artist.title(), 'album': album_title.title(), 'songs': song_number}
  else:
    album = {'artist': artist.title(), 'album': album_title.title()}
  return album

while True:
  print("Please enter your favorite album and artist")
  print("(Enter 'q' at any time if you would like to quit)")

  artist = input("Enter artist: ")
  if artist == 'q':
    break

  album = input("Enter album: ")
  if album == 'q':
    break

  formatted_album = make_album(artist, album)
  print(f"You favorite artist/album is: {formatted_album}")