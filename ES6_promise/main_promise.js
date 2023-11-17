import { addAsync, subtractAsync } from './promiseex';

function whenResolved(result) {
  console.log(`Operación exitosa, Resultado: ${result}`);
}

function whenRejected(result) {
  console.log(`Operación Fallida.\n${result}`);
}

addAsync(5, 3)
  .then((sumResult) => {
    whenResolved(sumResult);
    return (sumResult, subtractAsync(sumResult, '2'));
  })
  .then((subtractResult) => {
    whenResolved(subtractResult);
  })
  .catch((error) => {
    whenRejected(error);
  });
