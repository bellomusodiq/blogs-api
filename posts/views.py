from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.request.GET.get("post_id")
        if post_id:
            queryset = queryset.filter(post__id=post_id)
        return queryset
