export default function updateStudentGradeByCity(arrOfObjsStudents, city, arrOfObjsGrades) {
  return arrOfObjsStudents.filter((students) => (students.location === city))
    .map((student) => {
      const grades = arrOfObjsGrades.filter((grade) => (grade.studentId === student.id));
      const updatedStudent = { ...student };
      console.log(updatedStudent);
      if (grades.length !== 0) {
        updatedStudent.grade = grades[0].grade;
      } else {
        updatedStudent.grade = 'N/A';
      }
      return updatedStudent;
    });
}
