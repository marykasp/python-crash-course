def make_album(artist, album_title, song_number=None):
  if song_number:
    album = {'artist': artist.title(), 'album': album_title.title(), 'songs': song_number}
  else:
    album = {'artist': artist.title(), 'album': album_title.title()}
  return album

print(make_album('radiohead', 'rainbow'))
print(make_album('thee oh sees', 'orcs'))
print(make_album('album leaf', 'suburbs', 4))