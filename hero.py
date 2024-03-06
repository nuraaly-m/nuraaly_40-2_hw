class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, hp, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.hp = hp
        self.catchphrase = catchphrase

    def Name(self):
        print('name: ', self.name)

    def Increase_hp(self):
        self.hp *= 2

    def __str__(self):
        return (f'nickname: {self.nickname}\n'
                f'superpower: {self.superpower}\n'
                f'health point: {self.hp}')

    def Phrase(self):
        print('\nTrue in the True_phrase')


hero = SuperHero('Clark Kent', 'Superman', 'flight', 100, 'i am a superman')
hero.Name()
hero.Increase_hp()
print(hero)


class Land(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, hp, catchphrase, damage, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, hp, catchphrase)
        self.damage = damage
        self.fly = fly

    def Increase_hp(self):
        self.hp **= 2
        self.fly = True

    def __str__(self):
        return (f'\nnickname: {self.nickname}\n'
                f'superpower: {self.superpower}\n'
                f'health point: {self.hp}\n'
                f'damage: {self.damage}\n'
                f'fly: {self.fly}')


class Cosmic(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, hp, catchphrase, damage, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, hp, catchphrase)
        self.damage = damage
        self.fly = fly

    def Increase_hp(self):
        self.hp **= 2
        self.fly = True

    def __str__(self):
        return (f'\nnickname: {self.nickname}\n'
                f'superpower: {self.superpower}\n'
                f'health point: {self.hp}\n'
                f'damage: {self.damage}\n'
                f'fly: {self.fly}')


batman = Land('Bruce Wein', 'Batman', 'intelligence', 100, 'i am a batman', 100)
green_lantern = Cosmic('Hal Jordan', 'Green lantern', 'flight', 100, 'i am a green lantern', 100)
batman.Increase_hp()
print(batman)
batman.Name()
green_lantern.Increase_hp()
print(green_lantern)
green_lantern.Name()
batman.Phrase()


class Villain(Cosmic):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2


thanos = Villain('Thanos', 'Thanos', 'infinity stones', 100, 'i am a thanos', 100)
thanos.crit()
thanos.Increase_hp()
print(thanos)
thanos.Name()