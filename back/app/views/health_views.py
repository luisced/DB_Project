from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Basic health check endpoint to verify API is running
    """
    return Response(
        {"status": "healthy", "message": "API is running"},
        status=status.HTTP_200_OK
    )
