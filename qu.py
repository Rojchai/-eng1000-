import random
from vv import vv

def quiz():
    words = list(vv.keys())
    random.shuffle(words)
    
    for word in words:
        print(f" '{word}' ")
        answer = input("").strip()
        
        if answer.lower() == vv[word].lower():
            print("✓")
        else:
            print(f" '{vv[word]}'")
            print()

while True:
	quiz()
