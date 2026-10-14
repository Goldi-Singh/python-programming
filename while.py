#guess game
import random;
jack=random.randint(1,1000);
guess=int(input('tell your guess: '));
count=1;
while guess!=jack:
    if guess>jack:
        print('chose lower');
    else :
        print('guess higher');
print("you got it",end=' $$');
