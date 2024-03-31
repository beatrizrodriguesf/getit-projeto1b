from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}.{self.name}"

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.id}.{self.title}"
    
# class Tag_Note(models.Model):
#     note = models.ForeignKey(Note, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return f"{self.id}.{self.note.title}.{self.tag.name}"