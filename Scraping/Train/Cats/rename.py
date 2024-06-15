import os

for i in range(1, 1136):
    try:
        old_file = os.path.join("Cats/Real_cats", "%s.jpg"%i)
        new_file = os.path.join("Cats/AI_gen_cats", "Real_%s.jpg"%i)
        os.rename(old_file, new_file)
    except:
        print("file doesnot exist %s"%i)