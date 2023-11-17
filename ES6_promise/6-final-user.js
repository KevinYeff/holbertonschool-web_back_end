import singUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([singUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((promisesResults) => {
      for (const result of promisesResults) {
        if (result.status === 'rejected') {
          result.value = `${result.reason.name}: ${result.reason.message}`;
        }
      }
      //     //console.log(result);
      //   } else {
      //     result.status = 'rejected'
      //     // result.value = `${result.reason.name}: ${result.reason.message}`;
      //     //  console.log(result);
      //   }
      // }
      //  console.log(promisesResults);
      return promisesResults;
    })
    .catch((error) => error);
}
