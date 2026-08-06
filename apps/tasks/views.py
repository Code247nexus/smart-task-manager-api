from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .ai_priority import predict_priority
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Task.objects.filter(assignee=self.request.user)

    def get_queryset(self):
        queryset = Task.objects.filter(assignee=self.request.user)
        status = self.request.query_params.get("status")
        priority = self.request.query_params.get("priority")

        if status:
            queryset = queryset.filter(status=status)

        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset

    @action(detail=False, methods=["post"])
    def suggest_priority(self, request):
        title = request.data.get("title", "")
        description = request.data.get("description", "")
        priority = predict_priority(title, description)

        return Response(
            {
                "priority": priority
            }
        )