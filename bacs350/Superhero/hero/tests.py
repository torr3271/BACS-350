from django.test import TestCase

class ViewTests(SimpleTestCase):

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('hulk')
        self.assertEqual(response.status_code, 200)


## This class is testing CRUD operations
class HeroTests(TestCase):
    # all test functions must strat with test
    def test_hero_model(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
    
    def test_create(self):
        Superhero.objects.create(name='test', identity='testing')
        #for s in Superhero.objects.all():
        #    print(s.name, s.identity)
        self.assertEqual(len(Superhero.objects.all()), 1)
        self.assertEqual((Superhero.objects.get(pk=1).name, 'test')
        self.assertEqual((Superhero.objects.get(pk=1).identity, 'testing')

    def test_update(self):
        Superhero.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        x.name = 'Iron Man'
        x.save()
        y = Superhero.objects.get(pk=1)
        self.assertEqual(y.name, 'Iron Man')
        self.assertEqual(y.identity, 'Hulk')
        # Iron man != Hulk
        # only updated one of the fields in the database

    def test_read(self):
        Superhero.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        self.assertEqual(x.name, 'Bruce Banner')
        self.assertEqual(x.identity, 'Hulk')
        # huld != bruce banner

    def test_image(self):
        Superhero.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        x.image = 'Hulk.jpg'
        x.save()
        self.assertEqual(x.image, 'Hulk.jpg')