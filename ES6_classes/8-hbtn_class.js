export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }
  //  https://stackoverflow.com/questions/71949115/
  //  https://stackoverflow.com/questions/33327596/

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
