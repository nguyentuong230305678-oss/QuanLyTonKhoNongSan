from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer
from .permissions import role_required

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = []

class MeView(APIView):
    def get(self, request):
        u = request.user
        return Response({"username": u.username,
                         "roles": list(u.groups.values_list("name", flat=True))})

class AdminOnlyView(APIView):
    permission_classes = [role_required("ADMIN")]
    def get(self, request):
        return Response({"message": "Chỉ ADMIN mới thấy"})