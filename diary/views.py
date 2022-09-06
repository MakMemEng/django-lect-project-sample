from django.shortcuts import render, redirect
from .forms import DayCreateForm


# Create your views here.
def index(request):
    return render(request, 'diary/day_list.html')


def add(request):
    # 送信内容を基にフォーム作成, POSTでなければ空のフォーム
    form = DayCreateForm(request.POST or None)

    # method=POST 送信ボタン押下時,入力内容に問題が無ければ実行
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    # 通常時のページアクセスや入力内容に誤りがある場合,再度ページを表示
    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)
