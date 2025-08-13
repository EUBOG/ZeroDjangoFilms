# films/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Film
from .forms import FilmForm
from django.contrib import messages
import re

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save()  # ← Присваиваем результат в переменную
            messages.success(request, f'Фильм "{film.title}" успешно добавлен!')
            return redirect('films:film_list')  # Перенаправляем на список
    else:
        form = FilmForm()
    return render(request, 'add_film.html', {'form': form})

def film_list(request):
    query = request.GET.get('q')  # Поисковый запрос
    order = request.GET.get('order', 'newest')  # Сортировка

    films = Film.objects.all()

    # Поиск
    if query:
        # films = films.filter(title__icontains=query) # поиск учитывает регистр
        films = films.filter(title__iregex=r'^.*{}.*$'.format(re.escape(query))) # поиск без учета регистра

    # Сортировка
    if order == 'title_asc':
        films = films.order_by('title')
    elif order == 'title_desc':
        films = films.order_by('-title')
    elif order == 'oldest':
        films = films.order_by('created_at')
    else:  # по умолчанию — новые первыми
        films = films.order_by('-created_at')

    return render(request, 'film_list.html', {
        'films': films,
        'query': query,
        'order': order
    })

def edit_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('films:film_list')
    else:
        form = FilmForm(instance=film)
    return render(request, 'add_film.html', {'form': form, 'film': film})


def delete_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        title = film.title
        film.delete()
        messages.success(request, f'Фильм "{title}" успешно удалён.')
        return redirect('films:film_list')

    # Если GET — показываем страницу подтверждения
    return render(request, 'confirm_delete.html', {'film': film})