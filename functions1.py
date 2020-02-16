story = "After {} finishes his Python course he gets to download an {} game called Clash Royale. When he finishes his course he {} the game and moves on to master 1 in the first month and within the year he becomes the number 1 in the world."

def capture_input ():    
    """capture_input is a function to capture inputs noun,adjective and verb from user."""  
    noun = input ("enter noun:")
    verb = input ("enter verb:")
    adjective = input ("enter adjective:")

    return noun,verb,adjective


def create_story (story,noun,verb,adjective):

    updated_story = story.format(noun,adjective,verb)
    return updated_story

   
noun,verb,adjective = capture_input()
my_story=create_story(story,noun,verb,adjective)
print(my_story)
