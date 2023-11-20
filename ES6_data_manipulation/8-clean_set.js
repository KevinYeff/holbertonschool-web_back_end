export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') return '';
  const tempArray = [];
  for (const element of set) {
    if (element.startsWith(startString)) {
      tempArray.push(element.slice(startString.length));
    }
  }
  return tempArray.join('-');
}
