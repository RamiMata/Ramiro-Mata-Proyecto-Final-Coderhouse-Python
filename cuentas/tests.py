

# Create your tests here.



from .forms import ProfileForm
from django.urls import reverse


def test_profile_creation(self):
    self.assertEqual(self.profile.user.username, 'testuser')
    self.assertEqual(self.profile.description, 'Test description')

def test_profile_form_valid(self):
    form_data = {'description': 'Nueva descripción', 'website': 'http://example.com'}
    form = ProfileForm(data=form_data)
    self.assertTrue(form.is_valid())

def test_edit_profile_view(self):
    response = self.client.post(reverse('edit_profile'), {
        'first_name': 'Nuevo', 'last_name': 'Nombre', 'email': 'nuevo@example.com',
        'description': 'Descripción actualizada'
    })
    self.user.refresh_from_db()
    self.assertEqual(self.user.first_name, 'Nuevo')
    self.assertEqual(self.profile.description, 'Descripción actualizada')
