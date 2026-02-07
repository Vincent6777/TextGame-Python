print("Welcome to the game")
print("In this game you get to chose between multiple options and try to survive")
print("This game is about you being stranded in a world, frozen over, and you need to chose correctly to survive")
x = input("You now have the choice to go try to find other people by typing A, or you can go to the woods to make a campfire ny typing B")
if x == 'A':
    print("You died from hypothermia trying to find other people")
elif x == 'B':
    print("You are now in the woods")
    y = input("and you now have the choice to either, go punch a tree for wood by typing A, or you can collect sticks by typing B")
    if y == 'A':
        print("You broke your hand while punching the tree")
        z = input("You now have a broken hand, what do you do?, you can either ignore it by typing A, or you can use leaves to make a sling by typing B")
        if z == 'A':
            print("You die from the pain of your broken arm")
        elif z == 'B':
            print("You fail to make a sling from leaves and still die from the pain")
    elif y == 'B':
        print("You collect sticks and place them on top of eachother, now you need to make fire,")
        q = input("what will you do, are you going to try to find flint by typing A, are you going to try without flint by typing B")
        if q == 'B':
            print("You die trying to start a fire without flint")
        elif q == 'A':
            print("You find flint and use it to start a fire")
            w = int(input("Give a number between 1 and 10"))
            if w < 5 & w > 0:
                print("You fail to light the fire and still die")
            elif w >= 5 & w <= 10:
                print("You succesfully started a fire") 
                e = input("You can now collect rocks by typing A, or you can collect sticks by typing B")
                if e == 'A':
                    print("You die because you cant do anything with rocks")
                elif e == 'B':
                    print("You use the sticks you collected to build a shelter")
                    r = input("You come across a bear, what do you do, are you going to fight it for food then type A, if you are going to run press B")
                    if r == 'A':
                        print("You lose the fight against the bear and you die")
                    elif r == 'B':
                        print("You have escaped the bear")
                        print("After that bear attack you are starving")
                        t = input("What are you going to do?, if you are going to eat berries you found type A, if you are going to kill rabbits for meat type B")
                        if t == 'A':
                            print("The berries you ate are poisonous, you died")
                        elif t == 'B':
                            print("You killed rabbits for meat and can cook it now")
                            print("You put the meat on the campfire")
                            u = int(input("Choose a number between 1 and 10"))
                            if u == 1 or 3 or 5 or 7 or 9:
                                print("You burned the food and you starve to death")
                            elif u == 2 or 4 or 6 or 8 or 10:
                                print("Your meat is perfectly cooked and you")
                                print("Its starting to become night and its getting cold")
                                i = input("and you need to choose if you use leaves as a cover by typing A, or choose to find a sheep and use its wool by typing B")
                                if i == 'A':
                                    print("You used leaves to cover yourself and you froze to death")
                                elif i == 'B':
                                    print("You found a sheep and use his wool to cover yourself and you sleep through the night")
                                    print("when you wake up a you see other humans for the first time, what will you do")
                                    o = input("if you want to become friends with them and have them as allies type A, and if you want to fight and kill them for your safety")
                                    if o == 'B':
                                        print("They were stronger then you and outnumbered you and they easily killed you")
                                    if o == 'A':
                                        print("You invited them to be allies and they accepted you")
                                        print("Now you all are dying from dehydration, what will you do")
                                        p = input("if you want to drink your own pee type A, and if you want to search for water under the ice type B")
                                        if p == 'A':
                                            print("You dont have enough and die from dehydration")
                                        elif p == 'B':
                                            print("You go get water from underneath the ice and you survive")
                                            print("Your shelter isnt enough anymore for the 4 of you, what will you do")
                                            a = input("Will you stay here in your shelter then type A or go and look for a better place then type B")
                                            if a == 'A':
                                                print("You all die because one small shelter isnt enough for all of you")
                                            elif a == 'B':
                                                print("You go find a new shelter")
                                                print("You find a cave and take shelter there")
                                                d = input("You still have it cold, you can either do nothing by typing A, or you can build a campfire by typing B")
                                                if d == 'A':
                                                    print("You die from the cold")
                                                elif d == 'B':
                                                    print("You build a campfire and survive the second night, congrats")
                                                    print("The next morning you all wake up and you have ran out of food, what will you do")
                                                    f = input("If you are going to kill more rabbits then type A, and if you want to build a spear for fish type B")
                                                    if f == 'A':
                                                        print("You kill some rabbits and cook it but it cant last long and you all still starve")
                                                    elif f == 'B':
                                                        print("You want to build a spear to kill fish, but you still need to build a spear")
                                                        g = input("Choose a number from 1 to 10")
                                                        if g == 1 or 3 or 5 or 7 or 9:
                                                            print("You failed to make a spear and starve to death")
                                                        elif g == 2 or 4 or 6 or 8 or 10:
                                                            print("You made a spear and you kill fish for food")
                                                            print("You now cook the fish and have a good food source")
                                                            h = input("Whats next, you can choose to make an axe by typing A, or you can continue like this by typing B")
                                                            if h == 'B':
                                                                print("You die because your cave cant hold you guys warm for to long")
                                                            elif h == 'A':
                                                                j = int(input("Give a number from 1 to 10"))
                                                                if j == 1 or 3 or 7 or 9:
                                                                    print("You failed to make an axe")
                                                                elif j == 2 or 4 or 5 or 6 or 8 or 10:
                                                                    print("You succesfully made an axe")
                                                                    print("With this axe you can now chop trees and make houses")
                                                                    print("1 week later you all have houses and can stay warm for a long time")
                                                                    print("You have now build a small village and have the ability to stay outside for longer")
                                                                    k = input("You can now choose if you want to stay here and continue living here by typing A, or you can choose to find more people and become travellers by typing B")
                                                                    if k == 'A':
                                                                        print("You survived and continue living here, Congratulations")
                                                                    elif k == 'B':
                                                                        print("You have now become travellers and left your place behind")
                                                                        l = input("You now need to choose to go north by typing A, or go south by typing B")
                                                                        if l == 'A':
                                                                            print("You go all 4km north and you find sea and while sailing your boat sinks and you all drown")
                                                                        elif l == 'B':
                                                                            print("You all go south and you find an abandoned village, what do you do")
                                                                            c = input("You can now choose to go to the abandoned village by typing A, or skip it by typing B")
                                                                            if c == 'A':
                                                                                print("You go to the abandoned village and you find people there and they look hostile, what will you do")
                                                                                v = input("You can fight them by typing A, you can try to befriend them by typing B, or you can run from them by typing C")
                                                                                if v == 'A':
                                                                                    print("You die because you couldnt win a fight against them")
                                                                                elif v == 'B':
                                                                                    print("You die because they didnt want to be friends but killed you guys")
                                                                                elif v == 'C':
                                                                                    print("You die because they ran faster then you")
                                                                            elif c == 'B':
                                                                                print("You ignore the village and continue walking untill you find a city with people")
                                                                                print("The city is away from the snow and away from the cold")
                                                                                b = input("You can now choose to get back to normal life in the city by typing A, or you can go back in the winter to continue surviving by typing B")
                                                                                if b == 'A':
                                                                                    print("Congratulations, you survived")
                                                                                elif b == 'B':
                                                                                    print("You have chosen to go back to the winter, what will you do")
                                                                                    n = input("Will you go back to your established camp by typing A, or will you go and find a new place to build your home by typing B")
                                                                                    if n == 'A':
                                                                                        print("You have gone back to your camp and you live there for the rest of your live, congratulations, you survived")
                                                                                    elif n == 'B':
                                                                                        print("You have chosen to find a new place to call home, you go west since thats the only unexplored place in winter, what will you do")
                                                                                        m = input("If you want to go far west type A, if you want to go not that far type B")
                                                                                        if m == 'B':
                                                                                            print("You go not that far west and you find a mountain where you build your house")
                                                                                            print("Not long after a snowstorm destroys the camp and kills you all")
                                                                                        elif m == 'A':
                                                                                            print("You go far west and you find")