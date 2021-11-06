import os
from uuid import uuid1


class ApartmentsPhotoUtils:
    @staticmethod
    def upload_to(instance, file: str):
        ext = file.split('.')[-1]
        return os.path.join(instance.profile.user.email, 'apartment_photo', f'{uuid1()}.{ext}')
