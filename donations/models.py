from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Tobias Aufenanger, David Hardt, Christian Koenig'

doc = """
Simple donation task
"""


class Constants(BaseConstants):
    name_in_url = 'donations'
    players_per_group = None
    num_rounds = 1
    endowment = c(10)
    treatment_specifications = ['richkid', 'poorkid']
    additional_specifications = ['sunset', 'noanswer']



class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.treatment = random.choice(Constants.treatment_specifications)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donation = models.CurrencyField(min=0, max=Constants.endowment,
                                    doc="donation in EUR",
                                    verbose_name='How much do you want to donate?')
    treatment = models.CharField(choices=Constants.treatment_specifications)
    claimed_content = models.CharField(choices=Constants.treatment_specifications+Constants.additional_specifications,
                                       doc="Claimed content of the picture",
                                       verbose_name="What do you see in the picture on the previous page?")
    claimed_content_correct = models.BooleanField()
    def check_claim(self):
        self.claimed_content_correct = self.treatment == self.claimed_content
    def calculate_payoff(self):
        self.payoff = Constants.endowment-self.donation
