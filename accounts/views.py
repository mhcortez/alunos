from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

