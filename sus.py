import os
import fitz

for i in os.listdir("."):
    if os.path.isdir(i):
        for j in os.listdir(i):
            if j.endswith(".pdf"):
                pages = fitz.open(i+"/"+j)
                if not os.path.exists("images/"+i):
                    os.makedirs("images/"+i)
                page = pages.load_page(0)  # number of page
                pix = page.get_pixmap()
                output = "images/"+i+"/"+j[:-4]+".jpg"
                pix.save(output)