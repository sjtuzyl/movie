from flask import Blueprint

# ������ͼ
admin =Blueprint('admin',__name__)

from . import views
