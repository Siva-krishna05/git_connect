age=int(input("enter your age:"))
genre=input("enter your favourite genre (mystery/fantasy/science friction):")
if age<13:
    if genre=="mystery":
        print("recommended book: nancy drew")
    elif genre=="fantasy":
        print("recommended book: harry potter and the sorcerer's stone")
    elif genre=="science friction":
        print("recommended book: a wrinkle in time")
    else:
        print("genre not available!")
elif age>=13 and age<18:
    if genre=="mystery":
        print("recommended book: one of us is lying")
    elif genre=="fantasy":
        print("recommmended book: percy jackson")
    elif genre=="science friction":
        print("recommended book: the hunger games")
    else:
        print("genre not available!")
else:
    if genre=="mystery":
        print("recommended book: sherlock holmes")
    elif genre=="fantasy":
        print("recommended book:the lord of the rings")
    elif genre=="science friction":
        print("recommended book: dune")
    else:
        print("genre not available!")