from rest_framework.views import APIView
from api.serializers import TokenSerializer


class UserValidateTokenAPI(APIView):
    serializer_class = TokenSerializer
