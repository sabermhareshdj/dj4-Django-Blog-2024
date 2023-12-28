from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm

from django.views.generic import ListView , DetailView ,CreateView , UpdateView ,DeleteView

# def post_list(request): # query : template : context  (طريقة عمل ال def)
    # data = Post.objects.all()
    # return render(request,'post_list.html',{'posts':data}) #context

class PostList(ListView):   # template django default : post_list 
    model = Post            # context django default : post_list , object_list


# def post_detail(request,post_id):
    # data = Post.objects.get(id=post_id)
    # return render(request,'post_detail.html',{'post':data})

class PostDetail(DetailView):
    model = Post


# def post_new(request):
    # if request.method == 'POST':
        # form = PostForm(request.POST,request.FILES)
        # if form.is_valid():
            # myform = form.save(commit=False)
            # myform.author = request.user
            # myform.save()
            # return redirect('/blog')
    # else:
        # form = PostForm()
    # return render(request,'new_post.html',{'form':form})

class PostCreate(CreateView):
    model = Post
    fields = ['title','content','create_date','draft','tags','author','image']
    success_url ='/blog'


# def edit_post(request,post_id):
    # data = Post.objects.get(id=post_id)
    # if request.method == 'POST':
        # form = PostForm(request.POST,request.FILES,instance=data)
        # if form.is_valid():
            # myform = form.save(commit=False)
            # myform.author = request.user
            # myform.save()
            # return redirect('/blog')
    # else:
        # form = PostForm(instance=data)
    # return render(request,'edit_post.html',{'form':form})
class PostUpdate(UpdateView):
    model = Post
    fields = ['title','content','create_date','draft','tags','author','image']
    success_url ='/blog'
    template_name = 'blog/edit_post.html'

    

# def delete_post(request,post_id):
    # data = Post.objects.get(id=post_id)
    # data.delete()
    # return redirect('/blog')

class PostDelete(DeleteView):
    model = Post
    success_url ='/blog'



