export default function getListStudentIds(array) {
  if (array instanceof Array) {
    const newArray = [];
    for (const obj of array) {
      newArray.push(obj.id);
    }
    return newArray;
  }
  return [];
}
