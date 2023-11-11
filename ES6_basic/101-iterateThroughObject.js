export default function iterateThroughObject(reportWithIterator) {
  let str = '';
  let i = 0;
  for (const name of reportWithIterator) {
    if (i < reportWithIterator.length - 1) {
      str += `${name} | `;
    } else {
      str += `${name}`;
    }
    i += 1;
  }
  return str;
}
