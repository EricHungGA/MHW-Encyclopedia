from main_app.models import Monster_Image

def run():
    Monster_Image.objects.create(name='test monster 1', image='https://i.pinimg.com/564x/bb/a9/8f/bba98f565446221b40be64105f1b368c.jpg')
    Monster_Image.objects.create(name='test monster 2', image='https://i.pinimg.com/564x/d8/ef/f4/d8eff4a70519e9395ba36a8a0303355b.jpg')
    Monster_Image.objects.create(name='test monster 3', image='https://i.pinimg.com/564x/33/52/79/3352798a086b6722aefed7dd29e4db9a.jpg')
