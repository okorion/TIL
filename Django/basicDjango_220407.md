0407

> ```python
> from django.shortcuts import render, redirect
> from .forms import ArticleForm
> 
> def create(request):
>     if request.method == 'POST':
>         form = ArticleForm(request.POST)
>         if form.is_valid():
>             article = form.save()
>             return redirect('articles:detail', article.pk)
>     else:
>         form = ArticleForm()
>     context = {
>         'form': form,
>     }
>     return render(reqiest, 'articles/create.html', context)
> ```
>



#### 1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어있는가?

=> 첫 번째 if문에서도 context의 내용은 적용되어야 하기 때문에 코드의 중복을 막기 위해 if else와 동일한 레벨에 작성 되어 있다.



#### 2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?

=> 함수를 이용하여 데이터베이스에 기록하기 때문에 관례적으로 POST 요청 방식을 사용한다.