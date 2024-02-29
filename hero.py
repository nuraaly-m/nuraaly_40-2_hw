class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def Name(self):
        print('SuperHero name: ', self.name)

    def Increase_health(self):
        self.health_points *= 2

    def __str__(self):
        return (f'nickname: {self.nickname}\n'
                f'superpower: {self.superpower}\n'
                f'health point: {self.health_points}')

hero = SuperHero('Clark Kent', 'Superman', 'flight', 100, 'i am a superman')
hero.Name()
hero.Increase_health()
print(hero)


