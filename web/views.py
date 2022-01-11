from django.shortcuts import render
from .models import About, Mulch, Trimming, Mowing, Tree, Stone, Powerwash, Hardscape
import random
import getpass
import datetime

# Create your views here.
osUser = getpass.getuser()
hour = datetime.datetime.now().strftime('%H')

def quote():
    x = random.choice([
        'Don\'t be pushed around by the fears in your mind. Be led by the dreams in your heart.\n― Roy T. Bennett, The Light in the Heart ',
        'Success is not how high you have climbed, but how you make a positive difference to the world.\n― Roy T. Bennett, The Light in the Heart ',
        'Pursue what catches your heart, not what catches your eyes.\n― Roy T. Bennett, The Light in the Heart ',
        'Life is about accepting the challenges along the way, choosing to keep moving forward, and savoring the journey.\n― Roy T. Bennett, The Light in the Heart ',
        'Be brave to stand for what you believe in even if you stand alone.\n― Roy T. Bennett, The Light in the Heart ',
        'Do not fear failure but rather fear not trying.\n― Roy T. Bennett, The Light in the Heart ',
        'Never lose hope. Storms make people stronger and never last forever.\n― Roy T. Bennett, The Light in the Heart ',
        'Let the improvement of yourself keep you so busy that you have no time to criticize others.\n― Roy T. Bennett, The Light in the Heart ',
        'Be grateful for what you already have while you pursue your goals. If you aren’t grateful for what you already have, what makes you think you would be happy with more?\n― Roy T. Bennett, The Light in the Heart',
        'Everything can be taken from a man but one thing: the last of the human freedoms—to choose one’s attitude in any given set of circumstances, to choose one’s own way.\n― Viktor E. Frankl, Man\'s Search for Meaning',
        'You never change your life until you step out of your comfort zone; change begins at the end of your comfort zone.\n― Roy T. Bennett',
        'I’ve missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life and that is why I succeed.\n– Michael Jordan',
        'The best time to plant a tree was 20 years ago. The second best time is now.\n– Chinese Proverb',
    ])
    return x

def error():
    x = random.choice(
        ['Cannot compute...', 'Your shit\'s fucked up brah...', 'I cannot understand you...', 'Da fuq...'])
    return x

def greeting(request):
    username = None
    if request.user.get_username:
        username = request.user.username
        morningGreeting = random.choice(['Good morning, Mr.' + username + '!', 'Glad to see you this morning, ' + 'Mr. ' + username + '!'])
        afternoonGreeting = random.choice(['Good afternoon, Mr. ' + username + '!'])
        nightGreeting = random.choice(['Good evening, Mr. ' + username + '!'])
        if hour <= '12':
            return morningGreeting
        elif hour <= '17':
            return afternoonGreeting
        elif hour <= '23':
            return nightGreeting
        else:
            return error()

def index(request):
    context = {
    'quote': quote(),
    'greeting': greeting(request),
    'about': About.objects.all(),
    'mulch': Mulch.objects.all(),
    'trimming': Trimming.objects.all(),
    'mowing': Mowing.objects.all(),
    'tree': Tree.objects.all(),
    'stone': Stone.objects.all(),
    'powerwash': Powerwash.objects.all(),
    'hardscape': Hardscape.objects.all(),
    }
    print(osUser, ' Loaded Index')
    return render(request, 'index.html', context)
