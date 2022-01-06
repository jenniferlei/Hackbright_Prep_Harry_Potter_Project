import time
from art import *

def diagon_alley_story():
    print(diagon_alley_header)
    print()
    print("""Your first day at Hogwarts is just a few days away.
You have purchased your course books and a majority
of your required first year equipment from Diagon Alley,
London's wizarding shopping area.

    Robes... check! ✔️
    Hat... check! ✔️
    Gloves... check! ✔️
    Cloak... check! ✔️
    Cauldron... check! ✔️
    Phials... check! ✔️
    Telescope... check! ✔️
    Brass scale... check! ️️️️️✔️
""")
    
    time.sleep(1)

    print("""Oh, one more very important thing! You can't forget your wand.
Let's head to Ollivander's Wand Shop!""")

def ollivanders_story():
    print(ollivanders_header)
    print()
    print("""The sign above the shop says:

    \"Ollivanders: Makers of Fine Wands Since 382 BC\"

You step in, and before you know it, Ollivander is at your side.
He hands you a wand and you wave it around, as instructed.
""")

    time.sleep(1)
    
    print("""*boom*

No, that's no good.

The same thing happens a few more times with a variety of wands until...

finally!
""")

    time.sleep(1)

    print(wand_fireworks)

def menagerie_story():
    print(menagerie_header)
    print()
    print("""You've got your wand! Now, one last stop.
    
The Hogwarts acceptance letter states:
    \"Students may also bring, if they desire, an owl OR a cat OR a toad.\"
    
Well, off to the Magical Menagerie!
""")
    time.sleep(1)

    print("""You slowly enter the menagerie, and immediately the noises
and smells overwhelm your senses.
The menagerie is stuffed with cages, from floor to ceiling,
with all kinds of magical creatures. 

    Puffskeins
    Lacewing flies
    Fire crabs
    Kneazles
    Baby Nifflers
    Baby Pygmy Puffs
    Streelers
    Rats
    Skipping black rats
    Ravens
    Transforming rabbits
    Owls
    Double-ended newts
    Flobberworms
    Bats
    Fruit bat
    Chimps
    Ferrets
    Cats
    Toads
""")
    time.sleep(1)
    print("One cage, in particular, catches your eye.")


def welcome_story(pet):
    print(hogwarts_header)
    print()
    print(f"""The day has come! It's September 1st! 

Along with all the Hogwarts students, you and {pet} 
had hopped on the Hogwart's Express train at King's Cross Station Platform 9 3/4
and ended up at the Hogsmeade station.

From there, the first years take boats across the Great Lake.
The rest of the students separate and head down another route.
Guess you'll find out where they go next year!

Now, with Hagrid, Hogwart's gamekeeper, leading the way,
you and the rest of the first years sail on the lake towards...
""")
    print(boats)

def welcome_story2():
    print(hogwarts_header)
    print()
    print("The castle! It's amazing!")
    print()

    time.sleep(1)

    print("""You want to look at it longer, but before you know it,
Hagrid is shuffling you and the rest of the first years
into the huge main oak front doors and into the Entrance Hall.
""")

    time.sleep(1)
    print("""And up ahead, by the famous Headmaster Dumbledore, is the Sorting Hat!

It starts to sing...
""")
    # print sorting hat ascii
    print(sorting_hat)

def sorting_hat_story():
    print(sorting_hat_header)
    print()
    print("""Oh you may not think me pretty,
But don’t judge on what you see,
I’ll eat myself if you can find
A smarter hat than me.
You can keep your bowlers black,
Your top hats sleek and tall,
For I’m the Hogwarts Sorting Hat
And I can cap them all.
There’s nothing hidden in your head
The Sorting Hat can’t see,
So try me on and I will tell you
Where you ought to be.
""")
    time.sleep(1)
    print("""You might belong in Gryffindor,
Where dwell the brave at heart,
Their daring, nerve, and chivalry
Set Gryffindors apart;
You might belong in Hufflepuff,
Where they are just and loyal,
Those patient Hufflepuffs are true
And unafraid of toil;
Or yet in wise old Ravenclaw,
if you’ve a ready mind,
Where those of wit and learning,
Will always find their kind;
Or perhaps in Slytherin
You’ll make your real friends,
Those cunning folks use any means
To achieve their ends.
""")
    time.sleep(1)
    print("""So put me on! Don’t be afraid!
And don’t get in a flap!
You’re in safe hands (though I have none)
For I’m a Thinking Cap!""")

def year1_story():
    print(year1_header)
    print()
    print("""Your first year goes by smoothly.

You've been doing ok in your classes:
    Transfiguration, taught by 
    Charms, taught by Professor Flitwick
    Potions, taught by Professor Snape
    History of Magic, taught by Professor Binns (ZZZZZ, BORING 👻)
    Defence Against the Dark Arts, taught by Professor Quirrel
                                    (otherwise known as quivering Quirrel)
    Astronomy, taught by Professor Sinistra
    Herbology, taught by Professor Sprout
    Flying, taught by Madam Hooch (you rode your first broomstick! Maybe you
                                    can get on the Quidditch team next year?)

Everything seems normal...
""")

    time.sleep(1)
    
    print("""with the exception of stumbling into a room with
a trap door guarded by a three-headed dog and a room with a mirror.

Not to mention, the Daily Prophet (the wizarding world's newspaper)
reported an attempted robbery at Gringotts Wizarding Bank (nothing stolen!)
and a troll that managed to stumble its way into Hogwarts.

Very, very interesting news, as Gringotts and Hogwarts are VERY well
protected by strong magic.

...
""")
    time.sleep(1)
    print("""Could it be?

Someone tried to take something from Gringotts but that item is now hidden at Hogwarts!
It must be the sorcerer's stone that you read about in the library!
The sorcerer's stone could extend life, of even give immortality.

You must get to the stone before it's too late!""")
    

def fluffy_story():
    print(fluffy_header)
    print()

    print("""It's past curfew. You better hurry...
Filch, Hogwart's caretaker, is roaming the halls, ready to dole out punishment
to any rule-breaking student.

You stumble into a room - and you're safe! For now.

You hear the sound of a harp fading out, and all of sudden you hear a low growl.

...
""")

    time.sleep(1)

    print("""It's Fluffy, Hagrid's gigantic three-headed dog!
    
Someone has been here! Fluffy's guarding the trap door.
They must have gone through there."

Luckily, you're prepared for Fluffy.
Thanks to Hagrid's slip of the tongue, you know Fluffy can be lulled to sleep with the sound of music.
You take the flute out from your pocket...
""")

    time.sleep(1)

    print("*" * 60)
    print()

    print("""Rules:

Play the flute to lull Fluffy to sleep.
Reach 10 points to put Fluffy into deep slumber.
However, Fluffy also has the chance to wake up suddenly!
If his likeliness to waken reaches 10 points, game over!
""")

    print("*" * 60)

def devils_snare_story():
    print(devils_snare_header)
    print()
    print("""You jump into the trap door, and land on something soft.
Oh, this isn't too bad...
""")

    time.sleep(1)

    print("""Never mind! All of a sudden, there are strangling vines everywhere!
You can't move and the vines are wrapping around you, tighter and tighter.
It's a Devil's Snare! 
""")
    
    time.sleep(1)

    print("*" * 60)
    print()

    print("""Rules:

You need to guess the word that pertains to the wizarding world in order to escape the Devil's Snare!
At each turn, guess one letter. Lose a turn if you guess the incorrect letter.
If your 8 turns run out, the Devil's Snare will strangle you!
Good luck!
""")

    print("*" * 60)

def guess_potion_story():
    print(guess_potion_header)
    print()
    print("""Whew. You've gotten past the Devil's Snare...
and into another chamber.

All of a sudden, the way back bursts into purple flames.
The way forward bursts into black flames.
In the center of the chamber are 10 potions.
    
    \"Danger lies before you, while safety lies behind,
    Two of us will help you, whichever you would find,
    One among us ten will let you move ahead,
    Another will transport the drinker back instead,
    Two among our number hold only nettle wine,
    Six of us are killers, waiting hidden in line.
    Choose, unless you wish to stay here for evermore...\"
""")
    
    time.sleep(1)

    print("*" * 60)
    print()

    print("""Rules:

There are 8 potions with poison.
1 potion that will get you back safely through the purple flames
to warn Dumbledore.
1 potion that will allow you to safely walk forward through the black
flames to face whatever is in the chamber of the Sorcerer's Stone.
You have four chances to guess the correct potion (1 - 10) that will get you through
the black fire.
""")

    print("*" * 60)

def mirror_of_erised_story():
    print(mirror_of_erised_header)
    print()
    print("""You step through the black fire, and now you're in the room with the mirror.
Professor Quirrel is standing before the mirror.

Professor Quirrel? Who could have guessed it was Professor Quirrel?!

He still looks the same, with his head wrapped in a turban, but he is now a
completely different person from the usually nervous professor.

Professor Quirrel sneers your way and demands you to look at the mirror.
Somehow he thinks you can get the sorcerer's stone by looking at the mirror.

Up close, the mirror says:
    \"Erised stra ehru oyt ube cafru oyt on wohsi.\"
    
I show not your face but your hearts desire.
""")
    
    time.sleep(1)

    print("*" * 60)
    print()

    print("""Rules:

Look into the Mirror of Erised and guess the location of where the stone could be.
You have 12 chances to find the stone, before Professor Quirrel finds it!
""")

    print("*" * 60)

def voldemort_encounter_story():
    print(voldemort_encounter_header)
    print()
    print("""You watch your reflection in the Mirror of Erised put your reflection's hand
into your reflection's pocket...
and you suddenly feel something hefty in your own pocket.

It's the sorcerer's stone!

But you're definitely not revealing that to Professor Quirrel.

An angry Professor Quirrel removes his turban and turns around...
""")
    
    time.sleep(1)

    print("""Lord Voldemort! His face is on the back of Professor Quirrel's bald head.
His eyes and nose are slits, similar to that of a snake's.
    """)

    print("*" * 60)
    print()

    print("""Rules:

Cast a spell to duel with Lord Voldemort for three rounds!
Similar to rock paper scissors-
Rock/Stupefy defeats Scissors/Confundo
Paper/Expelliarmus defeats Rock/Stupefy
Scissors/Confundo defeats Paper/Expelliarmus
""")

    print("*" * 60)

def year1_end_story(house):
    print(end_of_year_header)
    print()
    print(f"""It's the last day of your first year at Hogwarts, and what a year it has been!
You've done what no other first year has done - defeated Voldemort.
Now Hogwart's end of the year banquet is in full swing.

""")
    time.sleep(1)

    print(f"""Dumbledore starts his end of the year speech:

    \"Another year, gone! And now, as I understand it, the house cup needs awarded
    and the points stand thus...

    ...recent events must be taken into account and I have a few last minute
    points to award. To {house} for the cool use of intellect while others were
    in grave peril: fifty points! And for pure love and outstanding courage, I
    award {house} house: sixty points! And finally: it takes a great deal of
    bravery to stand up to your enemies, but a great deal more to stand up to your
    friends. I award ten points!
    
    {house} wins the House Cup!\"

Hooray! Your house has won!
""")
    time.sleep(1)

    print("""You can't believe the year is over and it is time to return home.
But you're not going home. Not really.

Who knows what next year will bring?""")

def credits():
    print(credits_header)
    print()
    print("""Thank you for playing my game!
    
The game is loosely based off of Harry Potter and the Sorcerer's Stone by JK Rowling

Some texts are from the book and movie, as well as from the following sites:
    https://www.wizardingworld.com/
    https://harrypotter.fandom.com/
    
ASCII art is from the following sites:
    https://texteditor.com/ascii-art/
    https://ascii.co.uk/
    https://cloudapps.herokuapp.com/imagetoascii/
    https://www.asciiart.eu/
    https://textart.io/
    
Sorting Hat quiz questions are based off the quiz from:
    https://www.hypable.com/two-question-sorting-hat-quiz/""")