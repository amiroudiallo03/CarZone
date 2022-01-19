from .models import Team


def teams(request):

    teams = Team.objects.all()
    return dict(teams=teams)