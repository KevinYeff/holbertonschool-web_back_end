#!/usr/bin/node

export function addAsync(a, b) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (typeof a !== 'number' || typeof b !== 'number') {
        reject(new Error('a and b must be numbers'));
      } else {
        const result = a + b;
        resolve(result);
      }
    }, 3000);
  });
}

export function subtractAsync(a, b) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (typeof a !== 'number' || typeof b !== 'number') {
        reject(new Error('a and b must be numbers'));
      } else {
        const result = a - b;
        resolve(result);
      }
    }, 3000);
  });
}
