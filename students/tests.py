from django.test import TestCase
from .models import Student
from django.urls import reverse

class StudentModelTest(TestCase):
    def test_create_student(self):
        student = Student.objects.create(
            name="Ali",
            roll_no="101",
            email="ali@test.com"
        )
        self.assertEqual(student.name, "Ali")
        self.assertEqual(student.roll_no, "101")
        self.assertEqual(student.email, "ali@test.com")


class StudentViewTest(TestCase):
    def test_admin_login_page(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)