from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Notification

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user)
    data = [
        {
            "id": n.id,
            "actor": str(n.actor),
            "verb": n.verb,
            "target": str(n.target) if n.target else None,
            "timestamp": n.timestamp,
            "read": n.read,
        }
        for n in notifications
    ]
    return Response(data)

