from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        data = [{"id": post.id, "title": post.title, "author": post.author, "content": post.content,"created_at": post.created_at} for post in posts]
        return JsonResponse(data, safe=False)

    def post(self, request):
        import json
        data = json.loads(request.body)
        post = Post.objects.create(title=data['title'], content=data['content'], author=data['author'])
        return JsonResponse({"id": post.id, "title": post.title, "author": post.author, "created_at": post.created_at}, status=201)

class PostDetailView(View):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        data = {"id": post.id, "title": post.title, "author": post.author, "content": post.content, "created_at": post.created_at}
        return JsonResponse(data)