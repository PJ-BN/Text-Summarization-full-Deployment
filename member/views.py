from django.shortcuts import render, redirect

# Create your views here.

import spacy
import pytextrank

question = []
answer = ""

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
        
        
        value = summary(text_field_value)
        
        global answer
        if(answer == value):
          pass
        else:
          answer= value
          question.append([text_field_value,value])
        
        
        return render(request,  'member/index.html',  {
            'success_message': answer,
            'question': question,
            })
    else:
        return render(request, 'member/index.html')
    
   
    