from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm

def test_message_creation(self):
    self.assertEqual(Message.objects.count(), 1)
    self.assertEqual(self.message.sender.username, "user1")
    self.assertEqual(self.message.receiver.username, "user2")
    self.assertEqual(self.message.content, "Hola, este es un mensaje de prueba.")

def test_message_form_valid(self):
    form_data = {"receiver": self.user2.id, "content": "Mensaje de prueba"}
    form = MessageForm(data=form_data)
    self.assertTrue(form.is_valid())


def test_message_form_invalid(self):
    form_data = {"receiver": self.user2.id, "content": ""}
    form = MessageForm(data=form_data)
    self.assertFalse(form.is_valid())
