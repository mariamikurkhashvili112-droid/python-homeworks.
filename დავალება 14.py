
#Football Team Managmenet System

#შექმენით კლასი FootballTeam შემდეგი ატრიბუტებით:
#team_name (string) - კლუბის სახელი
#coach (string) - მწვრთნელი
#players - მოთამაშეების სია(შექმნისას ცარიელი უნდა იყოს)

#კლასს უნდა გააჩნდეს შემდეგი მეთოდები:
#1. მოთამაშის დამატება - მოთამაშის სახელი, პოზიცია, სათამაშო ნომერი,
 #  ასაკი და ეროვნება(დიქტის სახით უნდა დაემატოს მოთამაშეების სიაში)

#2. მოთამაშის წაშლა - მოთამაშე უნდა წაიშალოს სიიდან სათამაშო ნომრის მიხედვით

#3. მოთამაშის ინფორმაციის განახლება - მოთამაშე უნდა მონახოთ სათამაშო ნომრის მიხედვით
#  და უნდა დაუსეტოთ ისეთი ინფორმაცია, რომელსაც გადასცემთ ამ მეთოდს, მაგ: "goal": 1
#   ანუ key და value უნდა იყოს გადაცემული ამავე მეთოდის გამოძახებისას!

#4. კლუბის ინფორმაციის ჩვენება - გამოიტანეთ კლუბის სახელი, მწვრთნელის სახელი და მოთამაშეების სია

#5. მოთამაშის ინფორმაციის ჩვენება - უნდა გამოიტანოთ ინფორმაცია მოთამაშის ნომრის მიხედვით


class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, number, age, nationality):
        player_dict = {
            'name': name,
            'position': position,
            'number': number,
            'age': age,
            'nationality': nationality
        }
        self.players.append(player_dict)

    def delete_player(self, number):
        for player in self.players:
            if player['number'] == number:
                self.players.remove(player)
                break

    def update_player_info(self, number, key, value):
        for player in self.players:
            if player['number'] == number:
                player[key] = value
                break

    def display_team_info(self):
        print(f"Team Name: {self.team_name}")
        print(f"Coach: {self.coach}")
        print(f"Players List: {self.players}")

    def display_player_info(self, number):
        for player in self.players:
            if player['number'] == number:
                print(player)
                break


team = FootballTeam("Napoli", "Antonio Conte")

team.add_player("Khvicha Kvaratskhelia", "Forward", 7, 25, "Georgian")
team.add_player("Giorgi Mamardashvili", "Goalkeeper", 25, 25, "Georgian")

team.display_team_info()
team.display_player_info(7)

team.update_player_info(7, "goal", 1)
team.display_player_info(7)

team.delete_player(25)
team.display_team_info()