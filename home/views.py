

from django.shortcuts import render,  redirect
from django.http import JsonResponse  
from django.http import HttpResponse
from .models import *

import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Answer
import json

from django.http import JsonResponse
from .models import Question, Answer
import json

def submit_quiz(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        answers = data.get('answers', [])
        
        score = 0
        for answer in answers:
            try:
                # Get the Question based on UID
                question = Question.objects.get(uid=answer['uid'])
                
                # Find the answer that was selected by the user
                selected_answer = Answer.objects.get(question=question, answer=answer['selectedAnswer'])
                
                # Check if the selected answer is the correct one
                if selected_answer.is_correct:
                    score += question.marks  # Increment score by the marks of the question
                
            except Question.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Question not found'}, status=404)
            except Answer.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Answer not found'}, status=404)

        total = len(answers)
        
        return JsonResponse({
            'success': True,
            'score': score,
            'total': total
        })
    
    return JsonResponse({'success': False}, status=400)


from django.shortcuts import render

def result_view(request):
    score = request.GET.get('score', 0)
    total = request.GET.get('total', 0)
    return render(request, 'home/result.html', {'score': score, 'total': total})

def home(request):
    context = {'catgories': Types.objects.all()}
    
    if request.GET.get('gfg'):
        return redirect(f"/quiz/?gfg={request.GET.get('gfg')}")
    
    return render(request, 'home/home.html', context)

def quiz(request):
    context = {'gfg': request.GET.get('gfg')}
    return render(request, 'home/quizques.html', context)



def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        
        if request.GET.get('gfg'):
            question_objs = question_objs.filter(gfg__gfg_name__icontains = request.GET.get('gfg'))
            
        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)
        
        
        for question_obj in question_objs:
            
            data.append({
                "uid" : question_obj.uid,
                "gfg": question_obj.gfg.gfg_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answer" : question_obj.get_answers(),
            })

        payload = {'status': True, 'data': data}
        
        return JsonResponse(payload)  # Return JsonResponse
        
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")

