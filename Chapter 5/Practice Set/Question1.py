# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

oxford_dictionary = {
    'kutta' : 'Dog',
    'billi' : 'Cat',
    'ghoda' : 'Horse',
    'kachra' : 'Trash'
}
key = input("Enter the hindi word: ")

print(oxford_dictionary[key])