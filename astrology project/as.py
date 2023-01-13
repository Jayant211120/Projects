from tkinter import Entry, Menu, PhotoImage,BOTH,X,Y,LEFT,TOP,RIGHT,BOTTOM,RAISED
import tkinter as gui
import tkinter.ttk as ttk
import pyaztro
import tkvideo

# For Screen
screen = gui.Tk()
screen.title('Jayant Astrologer')
screen.minsize(100, 100)
labell=gui.Label(screen)
labell.grid()
vdo=tkvideo.tkvideo('video.mp4',labell,loop=1,size=(1550,800))
vdo.play()

def fun():
    global label
    alphabet = entry.get()
    if alphabet == 'j' or alphabet == 'J' or alphabet == 'kha' or alphabet == 'KHA':
        label = gui.Label(screen,text=f"{alphabet}:is belongs to Capricornus(Makar).\nThe lord of Capricorn is Saturn, which is considered to be an sin planet,but Saturn is a very justice-loving planet \n which makes the native hardworking and also gives proper results of hard work.  Capricornsare very hardworking.\n They hate easy paths. Discipline is an integral part of his personality.\n Although it may seem that thnatives may look arrogant and strict, but in reality they are very humble and open-minded.\n They play the role of a responsible citizen.They are also determined and extremely practical.\n The feeling of dedication is also present in their personality.\n They are vertolerant.\n Usually they do not get angry and are patient.\n Even if they get angry, they come very late, but after getting angry, they take a long time to calm down. \nPeople do every work selflessly and considering it as their duty.\n"
,font=5,foreground='blue')
        label.place(x=10,y=290)
    elif alphabet == 'a' or alphabet == 'A' or alphabet == 'l' or alphabet == 'L' or alphabet == 'e' or alphabet == 'E':
        label = gui.Label(screen, text=f"{alphabet}:is belongs to Aries(Mesh).\nPeople belonging to this sign are often fearless, full of energy, impulsive, passionate and sometimes even self centred.\n Their energy and passion sometimes drive them crazy and they never stay idle at one place.\n Action is a major part of their life and they are always on the run. 2021 HoroscopeKnow patterns in your life and predictions for 2021.\n Detailed astrology analysis and forecast on Career, Income, Health, Love and Marriage.\nCheckHighly courageous and fearless, they are never hesitant of any challenge in life.\n Always ready for the next move, they adapt and adjust very well with the new situations and move along with the flow.\n They are so passionate about things in their life that sometimes they tend to follow it foolishly, without being practical.\n They like to live life on their own terms and conditions and rarely surrender their values, beliefs or ideas.\n Even though they are very friendly and sociable, they rarely are willing to compromise their opinions or accommodate other people's ideas and opinions.\n When they set out to achieve something they make sure that they achieve it and do not easily give up on their goals and dreams and remain focused to it all the times.\n",font=5,foreground='blue')
        label.place(x=10,y=290)
    elif alphabet == 'k' or alphabet == 'K' or alphabet == 'chh' or alphabet == 'CHH' or alphabet == 'gh' or alphabet == 'GH':
        label = gui.Label(
            screen, text=f"{alphabet}:is belongs to Gemini(Mithun).Gemini (Date: May 22 - June 21) is a mutable sign ruled by Mercury. People belonging to Gemini are very energetic, curious, and charismatic and have a very good sense of humour. They have very strong imaginative powers and love to live in the world of fantasy. 2021 Horoscope Know patterns in your life and predictions for 2021. Detailed astrology analysis and forecast on Career, Income, Health, Love and Marriage.CheckThey have a very inquisitive nature, thus they explore everything that comes their way and holds good knowledge about everything. They love gathering information and ideas and sharing them with people. They are very good in making conversations and find it easy to articulate their thoughts. They are intelligent and are logical. They hate staying idle and will always be fondling or playing with something. They like to get to the roots of anything that comes across them. They are good in multitasking and are interested in anything that comes their way. Being the sign of the twins they are always jostling between two personalities. When one personality tries to be dominant the other tries to take over, leaving them confused. Hence this is the reason why they cannot stick to one thing for a long time. They will easily lose interest in one thing and start wandering to other sources of adventure and fun.",font=5,foreground='blue')
        label.place()
    elif alphabet == 'd' or alphabet == 'D' or alphabet == 'h' or alphabet == 'H':
        label = gui.Label(
            screen, text=f"{alphabet}:is belongs to Cancer(Kark).People born in Cancer (Kark Rashi) are usually of normal height. Moon affects the people of this zodiac. The natives are governed by the water element. The zodiac sign of the natives is Cancer i.e. Crab. Therefore, playfulness, coolness, emotionality and sensitivity are full of them. The specialty of their personality is that they create a family-like environment around them, that is, their nature is very friendly. When it comes to friendship, Cancerians are always ready to extend a hand of friendship. They have great respect for their friends. People who like to be social in the house are at the top of the native's friend list. Their innate nature makes them very kind, but sometimes it becomes impossible to understand them. These worry about family and karibis and value household comfort more than anything else. Natives are proficient in retaining family memories. Cancerians like to share their life experiences with their family. They love their soil very much.",font=5,foreground='blue')
        label.place(x=10,y=290)
    elif alphabet == 'p' or alphabet == 'P' or alphabet == 'th' or alphabet == 'TH' or alphabet == 'n' or alphabet == 'N':
        label = gui.Label(
            screen, text=f"{alphabet}:is belongs to Virgo(Kanya).Virgo natives are sincere and caring to the fault - towards their families, friends, and loved ones.Virgo is known as Kanya Rashi and is ruled by Mercury according to Vedic astrology. Kanya Rashi rules the 6th house of Ari Bhava of the horoscope wheel. Ari Bhava is the house of health and daily life activities whose ruling planet is Budh (Mercury).Nakshatras on Kanya Rashi are 2/3rd of Uttara Phalguni, Hasta, and half of the Chitra. As one of the hard-working zodiacs, Virgos want everything to be perfect. That’s why they analyze everything that interests them. Apart from that, they are great admirers of nature and optimistic",font=5,foreground='blue')
        label.place(x=10,y=290)
    elif alphabet == 'r' or alphabet == 'R' or alphabet == 'T' or alphabet == 't':
        label = gui.Label(screen, text=f"{alphabet}:is belongs to Libra(Tula)Thula Rasi people are sincere, hard-working, and interested in achieving success in whatever venture they take up. Success will always follow them if the environment is peaceful and harmonious. They dislike pretenses and unnecessary showmanship. They are pleasant and gracious in their dealings with others. In communication, they can be brief but to the point.Tula Rasi people take time in making important decisions. They think about all the possible outcomes of their action before committing to something. They are always active and ready to start some new venture or the other. These people are fair and cooperative. They love being social and enjoying themselves with colleagues, friends and family.",font=5,foreground='blue')
        label.place(x=10,y=290)
    elif alphabet == 'n' or alphabet == 'N' or alphabet == 'Y' or alphabet == 'y':
        label = gui.Label(
            screen, text=f"{alphabet}:is belongs to Scorpio(Vrishchik).Scorpio rashi is the eight sign described by constellation of stars , people born between  October 23 to November 22 have Scorpio as their rashi. Talking more about this rashi, it is ruled by planet's Pluto and Mars and has a deep running water element in it.It's emblem is a poisoning scorpio or snake which exemplifies person rigidity and hidden wish to succeed in life, people having scorpio as their sign or rashi mirror  Negative and Fierce characteristics. And with noteworthy qualities like energetic, truthful, self dependent, passionate and ambitious. they don't fall easily in other talks. Scorpio represents a very rigid nature which is very difficult to handle. They are sometimes intolerable and destructive while handling some situations.They are perverse  but are ready to bow down towards the happiness for their loved ones, they share a very secretive bond which no one can understand. And they love their personal space.But looking on the positive side they are very energetic and focused on their goals, the flowing water makes them fearless and devoted.They are also big dreamers and passionate about what they like, and have the attitude which never says no to any work.",font=5,foreground='blue')
        label.place(x=10,y=290)
    elif alphabet == 'pha' or alphabet == 'PHA' or alphabet == 'DHA' or alphabet == 'dha' or alphabet == 'bha' or alphabet == "BHA":
        label = gui.Label(
            screen, text=f"{alphabet}:is belongs to Sagittarius(Dhanu).Sagittarius (Date: November 23 - December 22) - A Sagittarius astrology sign is one of the most positive and optimistic signs of all. They are free spirited freedom loving individuals who are very fun loving. 2021 Horoscope Know patterns in your life and predictions for 2021. Detailed astrology analysis and forecast on Career, Income, Health, Love and Marriage.CheckThey have a very good sense of humour and will keep people jovial in their company. They are very honest and straightforward who are also intelligent and philosophical. Some of their bad qualities are that they are too optimistic to the level of being impractical. They are careless and do not take their responsibilities seriously. They are too superficial and have dual personality. They appear something from the outside but are different people on the inside. They value their freedom a lot and will not compromise with it at any cost.",font=5,foreground='blue')
        label.place(x=10,y=290)
    elif alphabet == 'G' or alphabet == 'g' or alphabet == 's' or alphabet == 'S' or alphabet == 'SH' or alphabet == 'sh':
        label = gui.Label(
            screen, text=f'{alphabet}:is belongs to Aquarius(Kumbh).They are perverse  but are ready to bow down towards the happiness for their loved ones, they share a very secretive bond which no one can understand. And they love their personal space.But looking on the positive side they are very energetic and focused on their goals, the flowing water makes them fearless and devoted.They are also big dreamers and passionate about what they like, and have the attitude which never says no to any work.',font=5,foreground='blue')
        label.place(x=10,y=290)
    elif alphabet == 'd' or alphabet == 'D' or alphabet == 'c' or alphabet == 'C' or alphabet == 'jha' or 'JHA' or alphabet == 'tha' or alphabet == 'THA':
        label = gui.Label(
            screen, text=f"{alphabet}:is belongs to Pisces(Meen).The Pisces (Meen) symbolised by two fish swimming in two different belongs to the twelfth house of the zodiac. It falls under the water sign and therefore they have a submissive yet rebellious nature. The Pisceans have a mystical, unusual, spiritual yet charming and pleasing personality. The typical fish is gentle, selfless, highly emotional, restless and anxious in nature. 2021 Horoscope Know patterns in your life and predictions for 2021. Detailed astrology analysis and forecast on Career, Income, Health, Love and Marriage.CheckThey are usually lost in their own thoughts, either soul searching or planting strategies that can be quite intellectual. Their creative juices flow naturally and they can come up with the most unique ideas effortlessly. Governed by the mystical and spiritual planet Neptune, they are usually drawn to a superficial world rather than focussing on reality. Thus, when reality actually bites them, it becomes unbearably difficult for them to accept the harsh realities of life and they tend to hibernate instinctively.",font=5,foreground='blue')
        label.place(x=10,y=290)
    else:
        label=gui.Label(screen,text='Please Enter valid Alphabet',font=5,foreground='blue')
        label.pack(x=10,y=290)
def fun2():
    global label2
    lst=entry2.get()
    p=pyaztro.Aztro(sign=lst)
    label2=gui.Label(screen,text=f"Favourite Color is:{p.color}\nUnderStanding with:{p.compatibility}\nCurrent date is:{(p.current_date)}\nPerday about:{(p.description)}\nYour Lucky Number:{(p.lucky_number)}\nYour Lucky Time:{(p.lucky_time)}\nYour Today's mood:{(p.mood)}\n Your Sign:{(p.sign)}\n The load of Capricorn and Saturn is:Saturn\nThe load of Aries and scorpio is:Mars\nThe load of Pisces and Sagittarius is:Jupiter\nThe load of Cancer is:Moon\nThe load of Gemini and Virgo is:Mercury\nThe load of Taurus and Libra is:Venus\n",font=5,foreground='blue')
    label2.place(x=10,y=290)
def clr():
    label.destroy()
    label2.destroy()
# Labels
firstLabel=gui.Label(screen,font=10,text='Enter your first alphabet for your sunsign')
firstLabel.place(x=235,y=20)
firstLabel=gui.Label(screen,font=10,text='Enter Your sunsign for find your sunsign perday ')
firstLabel.place(x=1020,y=20)
# Entry
entry = gui.Entry(screen, background='skyblue',fg='black',width=40,border=7,font=20)
entry.place(x=193,y=55)

button = gui.Button(screen, text="Search", padx='20',
                    pady='20', background='pink', command=fun)
button.place(x=350,y=150)
entry2 = gui.Entry(screen,background='skyblue',fg='black',width=40,border=7,font=20)
entry2.place(x=1000,y=55)
button2 = gui.Button(screen, text="Search", padx='20',
                    pady='20', background='pink', command=fun2)
button2.place(x=1200,y=150)
clear=gui.Button(screen,text="Clear", padx='20',
                    pady='20', background='tomato',cursor='man',relief=RAISED, command=clr)
clear.place(x=800,y=150)
# For Screen Stable
screen.mainloop()