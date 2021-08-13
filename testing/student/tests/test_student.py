from project.student import Student

from unittest import TestCase,main

class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("Test")

    def test_student_init_no_courses(self):
        self.student = Student("Test")
        self.assertEqual("Test", self.student.name)
        self.assertEqual({},self.student.courses)

    def test_student_init_none_courses(self):
        self.student = Student("Test", None)
        self.assertEqual("Test", self.student.name)
        self.assertEqual({},self.student.courses)

    def test_student_init_with_courses(self):
        self.student = Student("Test", {"Math":["note 1"]})
        self.assertEqual("Test", self.student.name)
        self.assertEqual({"Math":["note 1"]},self.student.courses)


    def test_student_enroll_with_course_in(self):
        self.student.courses = {"Math": ["note1"]}
        res = self.student.enroll("Math", ["note2"])
        self.assertEqual("Course already added. Notes have been updated.", res)
        self.assertEqual({"Math": ["note1", "note2"]},self.student.courses)

    def test_student_enroll_new_course_and_update_notes(self):
        res = self.student.enroll("Physics", ["note1"])
        self.assertEqual("Course and course notes have been added." ,res)
        self.assertEqual({"Physics": ["note1"]} ,self.student.courses)

    def test_student_enroll_new_course_and_yes_update_notes(self):
        res = self.student.enroll("Physics", ["note1"] , "Y")
        self.assertEqual("Course and course notes have been added." ,res)
        self.assertEqual({"Physics": ["note1"]} ,self.student.courses)  

    def test_student_enroll_dont_add_notes(self):
        res = self.student.enroll("Physics", "note1", "N")
        self.assertEqual("Course has been added.", res)
        self.assertEqual([],self.student.courses["Physics"])    


    def test_student_add_notes(self):
        self.student.courses = {"Math": ["some notes"]}
        self.assertEqual("Notes have been updated", str(self.student.add_notes("Math", "add note")))
        self.assertEqual({"Math": ["some notes", "add note"]}, self.student.courses)
        

    def test_student_add_notes_raises(self):
        self.student.courses = {"Math": ["some notes"]}
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Physics", "add note")
        self.assertEqual({"Math":["some notes"]}, self.student.courses)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_student_leave_course(self):
        self.student.courses = {"Math": []}
        res = self.student.leave_course("Math")
        self.assertEqual("Course has been removed", res)
        self.assertEqual({}, self.student.courses)

    def test_student_leave_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
   


if __name__ == "__main__":
    main()


