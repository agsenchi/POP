from os import system
from random import randint

gametitle = "Space Rescue - gra przygodowa tekstowa w Python"
system("mode 110,30")	
system("title " + gametitle)

def cls():
	system('cls')

character_name = None
character_job = None

spaceship_name = None
spaceship_type = None

character_life = None
character_power = None

spaceship_power = None
friends_or_foes = None

cls()

print("Space Rescue - gra przygodowa tekstowa w Python")

def Intro():

    print("")
    print("Drogi Graczu, odebrałeś sygnał S.O.S. ze statku kosmicznego.")
    print("Autopilot kieruje Cię właśnie w stronę źródła pochodzenia sygnału.")
    print("Twoje wybory będą sterowały rozwojem akcji ratunkowej.")
    print("Co wybierzesz? Czy uratujesz poszkodowaną załogę?")
    input("Naciśnij Enter, aby rozpocząć grę!")

Intro()

def create_character():
	cls()

	global character_name

	character_name = input("""
Jakie się nazywasz?
Podaj imię i naciśnij Enter.
		>>> """)

	print("Wybrałeś imię: ", character_name)

	global character_job

	while character_job is None:
		job_choice = input("""
Czym się zajmujesz?
Wybierz spośród dostępnych opcji i wpisz 1 lub 2:
		1 - Przemytnik z Betelgezy
		2 - Naukowiec z Alfa Centauri
		>>> """)
		if job_choice == "1":
			character_job = "Przemytnik z Betelgezy"
		elif job_choice == "2":
			character_job = "Naukowiec z Alfa Centauri"
		else:
			print("Wybierz ponownie między wartościami 1 lub 2")

	print("Wybrałeś zawód: ", character_job)

create_character()

def create_spaceship():
	global spaceship_name

	spaceship_name = input("""
Jak chcesz ochrzcić swój statek?
Podaj nazwę i naciśnij Enter.
		>>> """)

	print("Wybrałeś nazwę statku: ", spaceship_name)

	global spaceship_type

	while spaceship_type is None:
		type_choice = input("""
Jakiego rodzaju statkiem podróżujesz?
Wybierz spośród dostępnych opcji 1 lub 2:
		1 - Składak z części Sokoła Millenium i Enterprise
		2 - Nowiutki Infinity, wygrany w karty
		>>> """)

		if type_choice == "1":
			spaceship_type = "Składak z części Sokoła Millenium i Enterprise"
		elif type_choice == "2":
			spaceship_type = "Nowiutki Infinity, wygrany w karty"
		else:
			print("Wybierz ponownie między wartościami 1 lub 2")

	print("Wybrałeś statek: ", spaceship_type)

create_spaceship()

def create_features():

    cls()

    global character_name, character_job, spaceship_name, spaceship_type, character_life, character_power, spaceship_power

    print("""
Przed Tobą decyzja losu, ile będziesz mieć punktów życia, energii i jaką moc będzie miał Twój statek.
Punkty zostają przydzielone na podstawie Twoich wcześniejszych wyborów zawodu i rodzaju statku.
    Twoje startowe punkty:
    """)

    character_life = 10
    character_power = 0
    spaceship_power = 0

    if character_job == "Przemytnik z Betelgezy":
        character_life = character_life + 1
        character_power = character_power + 6
        spaceship_power = spaceship_power + 2

    elif character_job == "Naukowiec z Alfa Centauri":
        character_life = character_life + 3
        character_power = character_power + 4

    if spaceship_type == "Składak z części Sokoła Millenium i Enterprise":
       	spaceship_power = spaceship_power + 1

    elif spaceship_type == "Nowiutki Infinity, wygrany w karty":
        spaceship_power = spaceship_power + 2

    print("""

    Imię: """ +character_name+
    """

    Zawód: """ +character_job+
    """

    Nazwa statku: """ +spaceship_name+
    """

    Rodzaj statku: """ +spaceship_type+
    """

    Życie: """ +str(character_life)+
    """

    Energia: """ +str(character_power)+
    """

    Moc statku: """ +str(spaceship_power)+
    """
    """)

    input("Naciśnij Enter, aby potwierdzić Twoje startowe punkty i rozpocząć grę")

create_features()

def Scene_1():

    cls()

    choice = None

    global friends_or_foes


    while choice is None:
        print("""
Zbliżasz się do statku, który nadaje sygnał SOS. Jesteś już na tyle blisko, że możesz rozpoznać, do kogo należy statek.
Rzut Kostką Losu, zdecyduje, czy na statku są Twoi przyjaciele, czy wrogowie:
    	""")

        input("Naciśnij Enter, aby rzucić Kostką:")
        roll = randint(1,6)

        if roll < 4:
        	friends_or_foes = "friends"
        	print("Przyjeciele!")

        else:
        	friends_or_foes = "foes"
        	print("Wrogowie...")

        user_input = input("""

Co robisz? Czy kontynuujesz misję ratunkową?:

        1 - Tak
    	2 - Nie    
    	> """)

        if user_input == "1" or user_input == "Tak" or user_input == "tak":
            choice = "1"
            Scene_2()

        elif user_input == "2" or user_input == "Nie" or user_input == "nie":
            choice = "2"
            Scene_3()

        else:
            print("Wybierz ponownie między wartościami 1 lub 2 / tak lub nie")

def Scene_2():

    cls()

    choice = None  

    while choice is None:
        print("""
Wybrałeś udzielenie pomocy załodze statku. Rozpoczynasz dokowanie, aby wejść na pokład. Wymaga to wiele skupienia i precyzji.
Rzut Kostką Losu zdecyduje, czy masz wystarczająco energii, aby tego dokonać:
   		""")

        input("Naciśnij Enter, aby rzucić Kostką:")

        roll = randint(1,6)

        if roll < character_power:
        	print("Udało się! Dokowanie zakończyło się pomyślnie")
        	input("Naciśnij Enter, aby przejść dalej")
        	Scene_4()

        else:
        	print("Nie masz wystarczająco wiele energii...")
        	input("Naciśnij Enter, aby wyjść z gry")
        	exit()


def Scene_3():
 	cls()

 	choice = None

 	while choice is None:

 		if friends_or_foes == "friends":
 			print("""
 Wybrałeś nieudzielenie pomocy załodze przyjacielskiego statku i porzucenie swoich przyjaciół w potrzebie.
 Rzut Kostką Losu zdecyduje, ile punktów życia stracisz:
 			""")

 			input("Naciśnij Enter, aby rzucić Kostką:")
 			roll = randint(1,6)
 			print("Tracisz punkty życia: " +str(roll))
 			print("Pozostałe punkty życia: " +str(character_life))
 			input("Naciśnij Enter, aby wyjść z gry")
 			exit()

 		else:
 			print("""
 Wybrałeś nieudzielenie pomocy załodze wrogiego statku. Twoja intuicja miała racje - to była pułapka!
 Fałszywy sygnał SOS miał Cię zwabić.
 			""")

 			if character_job == "Przemytnik z Betelgezy":
 				print("Jako Przemytnik z Betelgezy przewozisz nielegalnie dostawy palladu i litu. Nie możesz dopuścić, aby Twoi wrogowie go przejęli...")
 			else:
 				print("Jako Naukowiec z Alfa Centauri masz na pokładzie prototyp napędu, który może odmienić przyszłość. Nie możesz dopuścić, aby Twoi wrogowie go przejęli...")

 			print("""

 Rzut Kostką Losu zdecyduje, czy Twój statek ma wystarczająco dużo mocy, aby uciec wrogom.
 			""")

 			input("Naciśnij Enter, aby rzucić Kostką:")

 			roll = randint(1,6)



 			if roll < spaceship_power:

 				print("Udało się! Twój statek nabiera prędkości i jest poza zasięgiem... Gra zakończona!")

 				input("Naciśnij Enter, aby wyjść z gry")

 				exit()

 			else:

 				print("Twój statek nie ma wystarczającej energii... Zostajesz pojmany i przegrywasz.")

 				input("Naciśnij Enter, aby wyjść z gry")

 				exit()

 

def Scene_4():

 	cls()

 	choice = None

 	while choice is None:

 		if friends_or_foes == "friends":

 			print("""

Twój statek pomyślnie zadokował i możesz rozpocząć akcję ratunkową swoich przyjaciół.

Rzut Kostką Losu zdecyduje, czy uda Ci się uratować wszystkich:

 			""")



 			input("Naciśnij Enter, aby rzucić Kostką:")

 			roll = randint(1,6)

 			if roll < character_power:

 				print("Udało się! Uratowałeś wszystkich!")

 				input("Naciśnij Enter, aby wyjść z gry")

 				exit()

 			else:

 				print("Nie masz wystarczająco wiele energii...")

 				input("Naciśnij Enter, aby wyjść z gry")

 				exit()



 		else:

 			print("""

Twój statek pomyślnie zadokował i możesz rozpocząć akcję ratunkową swoich wrogów. Twoja intuicja nie miała racji - to była pułapka!

Fałszywy sygnał SOS miał Cię zwabić.

 			""")

 			if character_job == "Przemytnik z Betelgezy":

 				print("Jako Przemytnik z Betelgezy przewozisz nielegalnie dostawy palladu i litu. Nie możesz dopuścić, aby Twoi wrogowie go przejęli...")

 			else:

 				print("Jako Naukowiec z Alfa Centauri masz na pokładzie prototyp napędu, który może odmienić przyszłość. Nie możesz dopuścić, aby Twoi wrogowie go przejęli...")

 			

 			print("""

 			Rzut Kostką Losu zdecyduje, czy Twój statek ma wystarczająco dużo mocy, aby uciec wrogom.

 			""")

 			input("Naciśnij Enter, aby rzucić Kostką:")

 			roll = randint(1,6)



 			if roll < spaceship_power:

 				print("Udało się! Twój statek nabiera prędkości i jest poza zasięgiem... Gra zakończona!")

 				input("Naciśnij Enter, aby wyjść z gry")

 				exit()

 			else:

 				print("Twój statek nie ma wystarczającej energii... Zostajesz pojmany i przegrywasz.")

 				input("Naciśnij Enter, aby wyjść z gry")

 				exit()

 



Scene_1()