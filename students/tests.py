from django.test import TestCase
from .models import School, Classroom


class SchoolModelTest(TestCase):
    """
    Tests for model School
    """

    def test_object_creation(self):
        school = School(name="Some University")
        self.assertTrue(isinstance(school, School))
        self.assertEqual(str(school), school.name)

    def test_save_school_and_load_from_id(self):
        school = School(name="Some School")
        self.assertEqual(school.name, "Some School")
        school.save()
        sid = school.id
        school2 = School.objects.get(pk=sid)
        self.assertEqual(school.name, school2.name)

    def test_delete_school_and_failed_to_load_from_id(self):
        school = School(name="Some School")
        self.assertEqual(school.name, "Some School")
        school.save()
        sid = school.id
        school.delete()
        with self.assertRaises(School.DoesNotExist):
            school2 = School.objects.get(pk=sid)


class ClassroomModelTest(TestCase):
    """
    Tests for model Classroom
    """

    def setUp(self):
        self.school = School(name="Some School")
        self.school.save()

    def tearDown(self):
        self.school.delete()

    def test_object_creation(self):
        class_room = Classroom(name="Classroom1", school=self.school)
        self.assertTrue(isinstance(class_room, Classroom))
        self.assertEqual(str(class_room), class_room.name)
        self.assertEqual(class_room.school.name, "Some School")

    def test_save_classroom_and_load_from_id(self):
        class_room = Classroom(name="Classroom1", school=self.school)
        class_room.save()
        self.assertEqual(class_room.name, "Classroom1")
        class_room.save()
        sid = class_room.id
        class_room2 = Classroom.objects.get(pk=sid)
        self.assertEqual(class_room.name, class_room2.name)
        self.assertEqual(class_room.school.name, "Some School")