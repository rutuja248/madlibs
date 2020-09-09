#madlibs generator
from random import randint
import copy


story=(
    "One day my {} friend and I decided to go to the {} game in {}. "+
    "We really wanted to see the {} play the {}. "
    )

#create a dictionary to lookup words by type
word_dict={
    
    "Adjective":['greedy','passionate','lovely','funny','adorable'],
    "city name":['Kolkata','Pune','Mumbai','Kolhapur','Bangaluru'],
    "noun":['people','map','music','table','chair','mouse'],
    'action verb':['cut','run','walk','jump','dance','look'],
    'sports noun':['ball','bat','stump']
    }

def get_word(type,local_dict):
    words=local_dict[type]
    cnt=len(words)-1
    index=randint(0,cnt)
    return local_dict[type].pop(index)
def create_story():
    local_dict=copy.deepcopy(word_dict)
    return story.format(
    get_word('Adjective',local_dict),
    get_word('sports noun',local_dict),
    get_word('city name',local_dict),
    get_word('noun',local_dict),
    get_word('noun',local_dict)
)
print("Story 1:")
print(create_story())
print()
print("Story 2:")
print(create_story())   
        