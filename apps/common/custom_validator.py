import random
import mimetypes
from django.shortcuts import get_object_or_404
from apps.bank_account import models
from django.core.files.storage import FileSystemStorage
from django.forms import ValidationError
from core.settings import FILE_UPLOAD_MAX_MEMORY_SIZE


def file_validation(value):
    file_types = ["image/png", "image/jpeg", "image/jpg", "application/pdf"]
    fs = FileSystemStorage()
    filename = fs.save(value.name, value)
    type = mimetypes.guess_type(filename)[0]
    print("TYPE OF FILE UPLOADED = ", type)

    if not value:
        raise ValidationError("No file selected.")

    if type not in file_types:
        raise ValidationError("Invalid file, please upload a clear image or pdf file")

    if value.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
        raise ValidationError("File shouldn't be larger than 10MB.")


def generate_account_number():
    account_number = random.randint(0000000000, 9999999999)
    return account_number


def account_no_validator(value):
    BankAccount = models.BankAccount.objects.all()
    for value in BankAccount:
        if value.verification_status == "Pending" or value.verification_status == "Failed":
            value.account_no = 1234567890

        if value.verification_status == "Success":
            value.account_no = generate_account_number
        value.save()
        return value