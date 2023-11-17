#!/usr/bin/node

import { addAsync, subtractAsync } from './callbackex';

function successCallBack(result) {
  console.log(`Operación exitosa, Resultado: ${result}`);
}

function errorCallBack(error) {
  console.log(`Error en la operación: ${error}`);
}

addAsync(5, '3', (error, sumResult) => {
  if (error) {
    errorCallBack(error);
  } else {
    successCallBack(sumResult);
  }

  subtractAsync(sumResult, 2, (error, subtractResult) => {
    if (error) {
      errorCallBack(error);
    } else {
      successCallBack(subtractResult);
    }
  });
});
