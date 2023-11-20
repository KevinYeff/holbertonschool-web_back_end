export default function getStudentsByLocation(arrayOfObj, city) {
  return arrayOfObj.filter((obj) => (obj.location === city));
}
