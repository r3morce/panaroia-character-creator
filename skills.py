class Skills:
    def __init__(self):
        self.management = Management()
        self.stealth = Stealth()
        self.violence = Violence()

    def __str__(self):
        return "member of Skills"

class Management:
    def __init__(self):
        self.bootlicking = 7
        self.chutzpah = 7
        self.con_games = 7
        self.hygiene = 7
        self.interrogation = 7
        self.intimidation = 7
        self.moxie = 7
        self.oratorie = 7

    def __str__(self):
        return "member of Management"

class Stealth:
    def __init__(self):
        self.concealment = 7
        self.disguise = 7
        self.high_alert = 7
        self.security_systems = 7
        self.shadowing = 7
        self.sleigth_of_hand = 7
        self.sneaking = 7
        self.surveillance = 7

    def __str__(self):
        return "member of Stealth"

class Violence:
    def __init__(self):
        self.agility = 7
        self.energy_weapons = 11
        self.demolition = 7
        self.field_weapons = 7
        self.fine_manipulation = 7
        self.hand_weapons = 7
        self.projectile_weapons = 7
        self.thrown_weapons = 7
        self.unarmed_combat = 7
        self.vehicular_combat = 7

    def __str__(self):
        return "member of Violence"
