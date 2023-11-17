#!/usr/bin/node

export function addAsync(a, b, callback) {
  setTimeout(() => {
    if (typeof a !== 'number' || typeof b !== 'number') {
      const error = 'a or b must be a number';
      callback(error, null);
    } else {
      const result = a + b;
      callback(null, result);
    }
  }, 3000);
}

export function subtractAsync(a, b, callback) {
  setTimeout(() => {
    if (typeof a !== 'number' || typeof b !== 'number') {
      const error = 'a or b must be a number';
      callback(error, null);
    } else {
      const result = a - b;
      callback(null, result);
    }
  }, 3000);
}
