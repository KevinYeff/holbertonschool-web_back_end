export default function createInt8TypedArray(length, position, value) {
  const buffered = new ArrayBuffer(length);
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }
  const dataView = new DataView(buffered);
  dataView.setInt8(position, value);
  return dataView;
}
