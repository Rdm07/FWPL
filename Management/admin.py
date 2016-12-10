from django.contrib import admin

# Register your models here.

from .models import *


admin.site.site_header = 'FWPL Site Administration'


admin.site.register(Matchday)
admin.site.register(Question)

admin.site.register(SinglePlayerTeamAnswer)
admin.site.register(YesNoAnswer)
admin.site.register(WinDrawLoseAnswer)
admin.site.register(ScorelineAnswer)
admin.site.register(SingleIntegerAnswer)
admin.site.register(LineupAnswer)
admin.site.register(GroupRanksAnswer)
admin.site.register(TeamAndValueAnswer)
admin.site.register(GoalAndAssistAnswer)

admin.site.register(SinglePlayerTeamAnswerSet)
admin.site.register(YesNoAnswerSet)
admin.site.register(WinDrawLoseAnswerSet)
admin.site.register(ScorelineAnswerSet)
admin.site.register(SingleIntegerAnswerSet)
admin.site.register(LineupAnswerSet)
admin.site.register(GroupRanksAnswerSet)
admin.site.register(TeamAndValueAnswerSet)
admin.site.register(GoalAndAssistAnswerSet)