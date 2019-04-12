from django.contrib.auth.models import User
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app_kochbuch.serializers.user import UserSerializer, ChangePasswordSerializer


class ViewUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['post'], detail=True)
    def change_password(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({'status':'successful'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, format=None):
        if not request.data.get('new_password') or not request.data.get('username'):
            return Response({'error':'required attributs username and new_password'}, status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(request.data.get('username'),
                                     request.data.get('email'),
                                     request.data.get('new_password'),
                                     first_name=request.data.get('first_name'),
                                     last_name=request.data.get('last_name'))
        return Response({'status': 'successful'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        user.is_active = False
        try:
            user.save()
            return Response({'status': 'successful'}, status=status.HTTP_200_OK)
        except:
            return Response({'error':'user could not be deactivated'}, status.HTTP_400_BAD_REQUEST)