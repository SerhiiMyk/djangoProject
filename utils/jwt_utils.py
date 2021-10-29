from datetime import timedelta

from apps.profile.models import UserModel
from exeptions.jwt_exeptions import JwtExceptions

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import BlacklistMixin, Token


class _AccessToken(BlacklistMixin, Token):
    lifetime = timedelta(hours=24)


class JwtUtils:
    def __init__(self, token_type, life_time: dict = None, token_class=_AccessToken):
        self._TokenClass = token_class
        if life_time:
            self._TokenClass.lifetime = timedelta(**life_time)
        self._TokenClass.token_type = token_type


    def create_token(self,user):
        return self._TokenClass.for_user(user)

    def validate_token(self,token):
        try:
            action_token = self._TokenClass(token)
            if not OutstandingToken.objects.filter(token=token).exists():
                raise JwtExceptions
            action_token.check_blacklist()
            action_token.blacklist()
            user_id = action_token.payload.get('user_id')
            return UserModel.objects.get(pk=user_id)
        except Exception:
            raise JwtExceptions
