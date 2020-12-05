from django.shortcuts import render
from survey.models import Survey, Answer



def main(request):

    survey=Survey.objects.filter(status='y').order_by(
        '-survey_idx')[0]

    return render(request, 'survey/main.html',
                  {'survey':survey})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def save_survey(request):
    row=Answer(survey_idx=request.POST['survey_idx'],
               num=request.POST['num'])
    row.save()
    return render(request, 'survey/success.html')





def show_result(request):
    idx=request.GET['survey_idx']
    ans=Survey.objects.get(survey_idx=idx)
    answer=[ans.ans1, ans.ans2 ]

    surveyList=Survey.objects.raw('''
select survey_idx, num, count(num) sum_num,
  round((select count(*) from survey_answer
    where survey_idx=a.survey_idx and num = a.num)*100.0 /
         (select count(*) from survey_answer
          where survey_idx=a.survey_idx),1) rate
from survey_answer a
where survey_idx = %s
group by survey_idx, num
order by num
    ''', idx)
    surveyList=zip(surveyList, answer)

    return render(request, 'survey/result.html', {'surveyList':surveyList})


