from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic

c = Category(1, "C")
t = Topic(1, "T", "C:\\user")
d = Document(1, 1, 1, "D")
s = Storage()

print(d.id)
print(d.category_id)
print(d.topic_id)
print(d.file_name)
print(d.tags)
doc = Document.from_instances(1, c, t, "Doc")
print(doc.id)
print(doc.category_id)
print(doc.topic_id)
print(doc.file_name)
