#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pypdf import PdfReader


# In[2]:


import os


# In[3]:


def insert_pdf(file_name, x_pos, y_pos, count_pages_in_leaf=[]):
    reader = PdfReader(file_name)
    
    key = '/MediaBox'
    x, y = (x_pos, y_pos)
    y_max = 0
    leaf = 1
    error_pages = {}
    lisp = ''
    
    class PageSize:
        scale = 2.83536556036556036556036556036556
        def __init__(self, points):
            self.x = round(points[2]/PageSize.scale)
            self.y = round(points[3]/PageSize.scale)
    
    for page, page_info in enumerate(reader.pages, start=1):
        if page == 1:
            continue
        if key in page_info:
            size = PageSize(page_info[key])
            y_max = max(y_max, size.y)
            lisp += f'  (command "_import" "C:/Users/Ivan/pdf-import/{file_name[4:]}" {page} \'({x} {y}) 25.4 0 )\n'
            x = x + size.x
            if count_pages_in_leaf and page % sum(count_pages_in_leaf[:leaf]) == 0:
                x, y, y_max = (0, y + y_max, 0)
                leaf += 1
        else:
            error_pages[page] = page_info
    
    if error_pages:
        print(error_pages)
    return lisp, y+y_max


# In[4]:


x, y = 0, 0
result = "(defun c:InsertPdf ()"
for name_dir, dir_, files in os.walk('pdf'):
    for file in files:
        lisp, y = insert_pdf(f'{name_dir}/{file}', x, y)
        result += lisp
result += ")"

with open('all.lsp', "w+", encoding="cp1251") as f:
    f.write(result)


# In[5]:


x, y = 0, 0

for name_dir, dir_, files in os.walk('pdf'):
    for file in files:
        lisp, y = insert_pdf(f'{name_dir}/{file}', x, y)
        with open(f'{file}.lsp', "w+", encoding="cp1251") as f:
            f.write("(defun c:InsertPdf ()")
            f.write(lisp)
            f.write(")")

