from django.shortcuts import render, redirect

# Create your views here.

import spacy
import pytextrank

def summary(example_text):

  nlp = spacy.load("en_core_web_lg")
  nlp.add_pipe("textrank")

  doc = nlp(example_text)

  sents = ""
  for sent in doc._.textrank.summary(limit_phrases=3, limit_sentences=4):
        sents = sents + sent.text
      
  
  print(sents)
  return sents

def submit_form(request):
    if request.method == 'POST':
        text_field_value = request.POST.get('my_text_field')
        # Do something with the text_field_value, such as saving it to a database
        # You can also pass it to a template if you want to display it on another page
        
        value = summary(text_field_value)
        
        return render(request,  'member/index.html',  {
            'success_message': value,
            'question': text_field_value,
            })
    else:
        return render(request, 'member/index.html')
    
   
    