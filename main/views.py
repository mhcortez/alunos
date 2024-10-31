from django.shortcuts import render, redirect
from .models import Estudante, Professor
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'main/index.html')

def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, 'main/lista_professores.html', {'professores': professores})

def cria_professores(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        idade = request.POST.get('idade')
        if nome and email and idade:
            Professor.objects.create(nome=nome, email=email, idade=idade)
            return redirect('lista_professores')
    return render(request, 'main/cria_professores.html')
    
def atualiza_professores(request, id):    
    professor = get_object_or_404(Professor, id=id)
    
    if request.method == 'POST':
        professor.nome = request.POST.get('nome')        
        professor.email = request.POST.get('email')
        professor.idade = request.POST.get('idade')
        professor.save()
        return redirect('lista_professores')
        
    return render(request, 'main/atualiza_professores.html', {'professor': professor})    
    
    
def deleta_professores(request, id):    
    professor = Professor.objects.get(id=id)
    professor.delete()
    return redirect('lista_professores')


def lista_alunos(request):
    alunos = Estudante.objects.all()
    return render(request, 'main/lista_alunos.html', {'alunos': alunos})

def cria_alunos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        idade = request.POST.get('idade')
        professor = request.POST.get('professor')
        if nome and email and idade:
            Estudante.objects.create(nome=nome, email=email, idade=idade)
            return redirect('lista_alunos')
    return render(request, 'main/cria_alunos.html')

def atualiza_alunos(request, id):
    estudante = Estudante.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        idade = request.POST['idade']
        professor = request.POST['professor']
        estudante.nome = nome
        estudante.email = email
        estudante.idade = idade
        estudante.professor = professor
        estudante.save()
        return render(request, 'main/atualiza_alunos.html', {'mensagem': 'Estudante atualizado com sucesso!'})
    else:
        return render(request, 'main/lista_alunos.html', {'estudante': estudante})

def deleta_alunos(request, id):
    estudante = Estudante.objects.get(id=id)
    estudante.delete()
    return redirect('lista_alunos')
