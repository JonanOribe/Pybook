from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name' : 'Mont Blac',
        'user' : 'Yésica Cortés',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/id/237/200/200'
    },
    {
        'name' : 'Danilo',
        'user' : 'Daniel Lopez',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/id/237/200/200'
    },
    {
        'name' : 'MVargas',
        'user' : 'Manuel Vargas',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/id/237/200/200'
    }
]

def list_posts(request):
    content=[]
    for post in posts:
        for post in posts:
            content.append("""
                <p><strong>{name}</strong></p>
                <p><small>{user} - <i>{timestamp}</i></small></p>
                <figure><img src="{picture}"/></figure>
                """.format(**post))
    return HttpResponse('<br>'.join(content))