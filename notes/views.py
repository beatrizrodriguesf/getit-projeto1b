from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        categories = request.POST.get('categoria')
        categories = categories.split()

        new_note = Note(title=title, content=content)
        new_note.save()

        for category in categories:
            category = category.strip()
        
            if not Tag.objects.filter(name=category):
                new_tag = Tag(name=category)
                new_tag.save()
            tag = Tag.objects.get(name=category)

            new_note.tags.add(tag)

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        all_categories = Tag.objects.values_list("name", flat=True)
        return render(request, 'notes/index.html', {'allNotes': all_notes, 'allCategories':all_categories})
    
def delete(request,id):
    note = Note.objects.get(pk=id).delete()
    return redirect('index')

def update_id(request, id):
    note = Note.objects.get(pk=id)
    tags = note.tags.all()
    str_tags = ""
    for i in range(len(tags)):
        if i != len(tags)-1:
            str_tags += f"{tags[i].name} "
        else:
            str_tags += f"{tags[i].name}"
    
    all_categories = Tag.objects.values_list("name", flat=True)
    
    return render(request, 'notes/update.html', {'note': note, 'tags': str_tags, 'allCategories': all_categories})

def update(request):
    id = request.POST.get('id')
    title = request.POST.get('titulo')
    content = request.POST.get('conteudo')
    categories = request.POST.get('categoria')
    categories = categories.split(" ")

    note = Note.objects.get(pk=id)
    note.title = title
    note.content = content
    note.tags.clear()
    note.save()

    for category in categories:
        category = category.strip()

        if not Tag.objects.filter(name=category):
            new_tag = Tag(name=category)
            new_tag.save()
        tag = Tag.objects.get(name=category)

        note.tags.add(tag)

    return redirect('index')

def category(request,category_name):
    all_tag_notes = Note.objects.filter(tags__name = category_name)
    return render(request, 'notes/category.html', {'tag_notes': all_tag_notes, 'category': category_name})

def categories(request):
    all_categories = Tag.objects.values_list("name", flat=True)
    return render (request, 'notes/categories.html', {'categories': all_categories})