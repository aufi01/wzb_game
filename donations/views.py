from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

#class ResultsWaitPage(WaitPage):

#    def after_all_players_arrive(self):
#        pass

class DonationDecision(Page):
    form_model = models.Player
    form_fields = ['donation']

class ClassificationDecision(Page):
    form_model = models.Player
    form_fields = ['claimed_content']
    def before_next_page(self):
        self.player.check_claim()
        self.player.calculate_payoff()

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Results(Page):
    pass


page_sequence = [
    DonationDecision,
    ClassificationDecision,
    Results
]
