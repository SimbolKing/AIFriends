from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.character import Character, Voice
from web.models.user import UserProfile


class CreateCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            name = request.data.get('name').strip()
            voice_id = request.data.get('voice_id')
            profile = request.data.get('profile').strip()[:100000]
            photo = request.FILES.get('photo', None)
            background_image = request.FILES.get('background_image', None)

            if not name:
                return Response({
                    'result': "character's name can not be empty"
                })
            if not profile:
                return Response({
                    'result': "character's profile can not be empty"
                })
            if not photo:
                return Response({
                    'result': "character's photo can not be empty"
                })
            if not background_image:
                return Response({
                    'result': 'chat background can not be empty'
                })

            voice = Voice.objects.get(id=voice_id)

            Character.objects.create(
                author=user_profile,
                name=name,
                voice=voice,
                profile=profile,
                photo=photo,
                background_image=background_image,
            )
            return Response({
                'result': 'success',
            })
        except:
            return Response({
                'result': 'System error'
            })
