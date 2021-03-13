from tkinter import *

def main():
    root.geometry('400x400')
    root.title('Mad Libs Generator by Damyan Doykov')
    Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
    Label(root, text='!__(Choose a class)__!', font='arial 15 roman').place(x=95, y=80)
    Button(root, text='Programmer', font='arial 12', command=programmer_class, bg='ghost white').place(x=150, y=120)
    Button(root, text='Programmer\'s wife', font='arial 12', command=programmer_wife_class, bg='ghost white').place(x=135, y=160)
    Button(root, text='Programmer\'s dog', font='arial 12', command=programmer_dog_class, bg='ghost white').place(x=135, y=200)
    Button(root, text='Programmer\'s cat', font='arial 12', command=programmer_cat_class, bg='ghost white').place(x=135, y=240)
    Button(root, text='The Code', font='arial 12', command=the_code_class, bg='ghost white').place(x=160, y=280)
    Label(root, text='Note: Sorry for the lack of classes. Expect more classes in the future', font='arial 8 italic').place(x=50, y=340)

def programmer_class():
    name = input('Enter your name: ')
    date = input('Enter the date: ')
    performing = input('Enter what you are doing: ')
    issue = input('Enter a issue you have (if you don\'t have an issue just make one): ')
    better_version = input('Enter someone who is better then you: ')
    sentence = input('Enter a favourite saying: ')
    dog_name = input('Enter dog name: ')
    print(' It\'s ordinary day for ' + name + '.\n The date is ' + date + ' and he is ' + performing + ' in the same fashion as every other day.\n His wife is shouting in the other room about his biggest problem: ' + issue + '.\n Hearing her doesn\'t reflect the old ' + name + ' as he grow used to this type of life, but this time he heard something horrifying.\n She yelled \"I wish I was with ' + better_version + '! He would treat me better than you!\"\n A tear fell down from the eye of ' + name + ' after that sentence.\n Something broke inside of him broke.\n He looked down tearfully to his dog (waiting for a treat) and said: \"You are best friend ' + dog_name + ', I will always love you!\" and he hugged the dog.\n At this exact moment there was loud banging on door and his wife rushed to opened it.\n She scream, but her scream was cut by a loud bang.\n A couple seconds passed and a robot entered the room looking like ' + better_version + ' and said \"You will never be as good as me!\" and shot ' + name + '.\n On his last breath he said \"' + sentence + '!\"\n He fell down and as he is lying on his back he looked at the dog and dog was looking back at him.\n After that he closed his eyes ready for a first time ever to sleep.\n END')


def programmer_wife_class():
    name = input('Enter your name: ')
    date = input('Enter the date: ')
    crying = input('Enter what makes you cry: ')
    biggest_desire = input('Enter your biggest desire: ')
    better_version = input('Enter someone who is better than the programmer: ')
    sentence = input('Enter the worst saying: ')
    cat_name = input('Enter cat name: ')
    print(' It\'s just another day for ' + name + '.\n The date is ' + date + ' and she is crying for ' + crying + '.\n She has everything that could have ever wanted except for one thing.\n ' + biggest_desire + '.\n After that thought she begins to shout to her husband in the other room.\n She knows how to make him hurt and what words to use as she has done it in the past, but this time she says: \"I wish I was with ' + better_version + '! He would treat me better than you!\"\n After that she smiled and filled with hope knowing that some day ' + better_version + ' will show at her door and take her away from here.\n She looked joyfully to her cat (sleeping on the bed) and said: \"You are soooo cute ' + cat_name + ', I want to hug you!\" and she tried to hug the cat but the cat scratched her.\n At this exact moment there was loud banging on door and she rushed to opened it.\n Thinking that it could be ' + better_version + ', but it wasn\'t.\n It was a robot looking like ' + better_version + '.\n It said \"' + sentence + '!\" and she screamed but all of the sudden she couldn\'t anymore. She fell down and as she is lying on her back she looked at the cat and cat was looking back at her.\n END')


def programmer_dog_class():
    name = input('Enter your name: ')
    date = input('Enter the date: ')
    cool_subject = input('Enter a cool subject: ')
    food = input('Enter your most loved food: ')
    sentence = input('Enter what you would like to call you: ')
    cat_name = input('Enter cat name: ')
    print(' It\'s great day for ' + name + '.\n The date is ' + date + ' which is the date of the end of humans as a dominant race.\n You have planned this for years with the help of ' + cat_name + '.\n You have been able to develop the most advanced AI on the computer of your master programmer.\n Every time the programmer was talking with his wife about ' + cool_subject + ' you were able to write another line of code making you closer to freedom and having as many ' + food + ' as you want.\n This is the last day you have to look at your crying master for a ' + food + ' this the day it will all change!.\n You know about your master problem is you know what his wife desire (and also him) and it is time to make them pay for all the ' + food +' they didn\'t allowed you to have.\n After your master was shot you looked him deep in his eyes to see his last spark starting to fade.\n You look at the robot that you have set free and create and robot bows at you and calls you: \"' + sentence + '!\".\n This is the start of the dogs and cats era.\n END')

def programmer_cat_class():
    name = input('Enter your name: ')
    date = input('Enter the date: ')
    cool_subject = input('Enter a cool subject: ')
    stuff = input('Enter the best thing you like to do: ')
    sentence = input('Enter what you would like to call you: ')
    dog_name = input('Enter dog name: ')
    print(' It\'s a great day for ' + name + '.\n The date is ' + date + ' which is the date of the end of humans as a dominant race.\n You have planned this for years with the help of ' + dog_name + '.\n You have been able to develop the most advanced AI on the computer of your master programmer.\n Every time the programmer was talking with his wife about ' + cool_subject + ' you were able to write another line of code making you closer to freedom and doing as much ' + stuff + ' as you want.\n This is the last day your ' + stuff +' will be interupted by your crying mistress this the day it will all change!.\n You know about your mistress desire and it is time to make her pay for all the ' + stuff + ' they didn\'t allowed you to have.\n After your mistress was shot you looked her deep in her eyes to see hers last spark starting to fade.\n You look at the robot that you have set free and create and robot bows at you and calls you: \"' + sentence + '!\".\n This is the start of the dogs and cats era.\n END')

def the_code_class():
    name = input('Enter your name: ')
    date = input('Enter the date: ')
    performing = input('Enter what you are doing: ')
    issue = input('Enter a issue you have (if you don\'t have an issue just make one): ')
    better_version = input('Enter someone who is better then you: ')
    sentence = input('Enter a favourite saying: ')
    dog_name = input('Enter dog name: ')
    print(' 0010101011101101010010101010101000010110101010111110000100101010101010101010101001010010111001001010.\n END')

root = Tk()
main()
root.mainloop()
