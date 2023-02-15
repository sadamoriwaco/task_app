import re
from tabnanny import check
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse_lazy

# from info.models import モデルで作ったクラス名
# from .forms import (Formで作ったクラス名)

class IndexView(generic.TemplateView):
    template_name = "index.html"
    # form_class = Form
    success_url = reverse_lazy('diary:inquiry')    