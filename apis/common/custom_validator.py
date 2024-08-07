import mimetypes
from datetime import date, datetime
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from rest_framework.exceptions import ValidationError
from core import settings


def file_validator(file):

    file_types = ["image/png", "image/jpeg", "image/jpg"]

    if not file:
        raise ValidationError("No file selected.")

    if file.size > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
        raise ValidationError("File shouldn't be larger than 10MB.")

    if isinstance(file, UploadedFile):
        if file.size > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError(
                f"File shouldn't be larger than {settings.FILE_UPLOAD_MAX_MEMORY_SIZE}MB.")

    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    file_type = mimetypes.guess_type(filename)[0]
    if file_type not in file_types:
        raise ValidationError("Invalid file, please try again...")
    return file_type


def verify_date_of_birth(date_of_birth):
    if not date_of_birth:
        raise ValidationError("please provide your date of birth.")
    user_age = datetime.strptime(str(date_of_birth), "%Y-%m-%d").date()
    today = date.today()
    age_days = today - user_age
    age = age_days / 365.25
    age_obj = age.days

    if (user_age.year == today.year and user_age.day == today.day and user_age.month == today.month):
        return age_obj - 1
    return age_obj
