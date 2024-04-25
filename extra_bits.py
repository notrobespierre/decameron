#first story
URL = return_URL(1, 1)
story_string = clean_story(URL)
first = story_string

with open("0101.txt", 'w', encoding='unicode-escape') as f:
    f.write(story_string)

#third story
URL = return_URL(1, 3)
story_string = clean_story(URL)
third = story_string


with open("0103.txt", 'w', encoding='unicode-escape') as f:
    f.write(story_string)



#first = open("0101.txt")
#third = open("0103.txt")