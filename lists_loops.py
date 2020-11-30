songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0])
print(songs[2])
songs[0] = "Dynamite"
print(songs)

songs.append("The Spins")
songs.extend(["MF Gloom", "Pursuit of Happiness"])
del songs[1]
print(songs)

animals = ["Hedgohog", "Cat", "Snake"]
animals.append("Dog")
print(animals)
print(animals[2])
del animals[0]
for animal in animals: 
    print(animal)