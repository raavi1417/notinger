from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    #return HttpResponse('''<h1>Facebook</h1> <a href="https://www.facebook.com/">Click</a>''')
    #return HttpResponse('<h1>Hello sudhanshu</h1><br>'
                      #  '<a href="/instagram">Next</a>')
    return render(request,'index.html')
def analyze(request):
    #get the text
    djtxt=request.POST.get('text','default')
    punc=request.POST.get('removepunc','off')
    cap=request.POST.get('capital','off')
    linermv=request.POST.get('newlinermv','off')
    #analyze the text
    if punc =='on':
        analyzed=""
        puncuation_list='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtxt:
            if char not in puncuation_list:
                analyzed=analyzed+char
        params={'purpose':'remove Punctuation','Analyze_text':analyzed}
        djtxt=analyzed
    if cap == 'on':
        analyzed=""
        for char in djtxt:
            analyzed=analyzed+char.upper()
        params={'purpose':'Capitalized','Analyze_text':analyzed}
        djtxt=analyzed
    if linermv == 'on':
        analyzed=""
        for char in djtxt:
            if char !='\n' and char !='\r':
                analyzed=analyzed+char
        params={'purpose':'New Line Remover','Analyze_text':analyzed}
    if (punc == 'off'  and cap == 'off' and linermv == 'off'):
        return HttpResponse('''<script>alert("Error");location.href='/'</script>''')
   
    return render(request,'analze.html',params)
