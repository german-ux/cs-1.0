songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[1:3])
songs[2] = "Paper Planes"
print(songs)
songs.extend(["The Spins", "Set to Attack", "Windowpane"])
print(songs)
del  songs[1]
print(songs)

for song in songs:
    print(song)

for i in range(len(songs)):
    print(songs[i])

animals = ["cat", "dog", "bird"]
animals.append("snake")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)