from django.http import HttpResponse
from django.shortcuts import render
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="emmakz/GPT_text_generation")
def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        generation_ans = pipe(input_text)
        generation = generation_ans[0]['generated_text']
        return render(request,'index.html',{'generation':generation})
    return render(request,'index.html')