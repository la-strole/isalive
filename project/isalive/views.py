from django.shortcuts import render
import wikipedia
import re
from django.http import HttpResponse


# Create your views here.
def is_alive(request):
    """
    Only one question - is he alive?
    :return: Yes or No
    """

    # Get info from wikipedia
    wikipedia.set_lang('ru')
    page = wikipedia.page('Путин')
    first_line = re.findall(r'\(.+\) ', page.summary)
    if first_line:
        dates = re.findall(r'\d.+?\d{4}', first_line[0])
        if dates:
            if len(dates) == 1:
                text = 'yes'
            else:
                text = 'no'
        else:
            text = 'Error'
    else:
        text = 'Error'

    return render(request, 'isalive/isalive.html', {'text': text, })
