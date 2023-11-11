export default function createIteratorObject(report) {
  const array = [];
  for (const key of Object.keys(report.allEmployees)) {
    array.push(...report.allEmployees[key]);
  }
  return array;
}
