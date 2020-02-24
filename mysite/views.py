# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#   return HttpResponse("hello")
#def index2(request):
#    return HttpResponse("mini")
#def index3(request):
#    return HttpResponse('''<a href="https://www.facebook.com/utkansh/">facebook Utkansh</a>''')
def index(request):
    #return HttpResponse("Home")
    return render(request, 'index.html')
def analyze(request):
    #get the text
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    capitalization=request.POST.get('capitalization', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    #print(removepunc)
    #print(djtext)
   # analyzed = djtext
    if removepunc == "on":
       punctuation = '''~!@#$%^&*()_+{}|:"<>?`-=][\';,./'''
       analyzed = ""
       for char in djtext:
           if char not in punctuation:
               analyzed = analyzed + char

       params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
       # analyze the text
       djtext=analyzed
       #return render(request, 'analyze.html', params)


    if capitalization == "on":
             analyzed= djtext.upper()

             params = {'purpose': 'Capitalization', 'analyzed_text': analyzed}
            # analyze the text
             djtext=analyzed
             #return render(request, 'analyze.html', params)
    if newlineremover == "on":
           analyzed = ""
           for char in djtext:
               if char !="\n" and char !="\r":
                   analyzed = analyzed + char

           params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        # analyze the text
           djtext=analyzed
           #return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
           analyzed = ""
           for index, char in enumerate(djtext):
              if not(djtext[index]==" " and djtext[index+1]==" "):
                  analyzed=analyzed+char
           params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        # analyze the text
           djtext=analyzed
           #return render(request, 'analyze.html', params)
    if charactercounter == "on":
        character = '''~!@#$%^&*()_+{}|:"<>?`-=][\';,./1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'''
        analyzed = 0
        for char in djtext:
            if char in character:
                analyzed = analyzed + 1

        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        djtext =analyzed

        #return render(request, 'analyze.html', params)

    #else:
       # analyzed = djtext;
       # params = {'purpose': 'Erorr', 'analyzed_text': analyzed}

        #return render(request, 'analyze.html', params)
    if charactercounter != "on" and extraspaceremover != "on" and newlineremover != "on" and capitalization != "on" and removepunc != "on":
        return HttpResponse("ERROR, please select the operation and try again")
    return render(request, 'analyze.html', params)


#def capfirst(request):
#    return HttpResponse("capitalizefirst")
#def newlineremover(request):
#    return HttpResponse("newlineremove")
#def spaceremove(request):
#    return HttpResponse("spaceremove")
#def charactercount(request):
#    return HttpResponse("charactercount <a href='home'>back</a>")