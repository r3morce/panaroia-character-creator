from tabulate import tabulate

import skills
import osa
import mutations
import secret_organizations
import service_groups
import items

class Troubleshooter:

    def __init__(self, chosen_name, block):
        self.chosen_name = chosen_name
        self.clearance = 'R'
        self.block = block
        self.clone_nr = 1

        self.osa = osa.get_osa()
        self.service_group = service_groups.get_service_group()
        self.mutation = mutations.get_mutation()
        self.secret_organization = secret_organizations.get_secret_organizaton()

        self.skills = skills.Skills()

        self.items = items.basic

    def get_name(self):
        return self.chosen_name + '-' + self.clearance +  '-' + self.block +  '-' + str(self.clone_nr)

    def print_sheet(self):
        info = []
        info.append(['Name', self.get_name()])
        info.append(['Servicegruppe', self.service_group])
        info.append(['Obligatorische Sonderaufgabe', self.osa])
        info.append(['!Geheimorganisation', self.secret_organization])
        info.append(['!Mutantenkraft', self.mutation])
        print tabulate(info)
