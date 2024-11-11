

from django.shortcuts import render,  redirect
from django.http import JsonResponse  
from django.http import HttpResponse
from .models import *

import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Answer

@csrf_exempt


def submit_quiz(request):
    if request.method == 'POST':
        try:
            data = JsonResponse.loads(request.body)
            answers = data.get('answers', [])
            
            # Log the answers received for debugging
            print(f"Answers received: {answers}")
            
            # Calculate score and total (example logic)
            score = sum(1 for ans in answers if ans['selectedAnswer'] == 'correct')
            total = len(answers)

            return JsonResponse({
                'success': True,
                'score': score,
                'total': total
            })
        except Exception as e:
            print(f"Error processing quiz: {e}")
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

from django.shortcuts import render

def result_view(request):
    return render(request, 'home/result.html')

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

