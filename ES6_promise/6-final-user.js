import singUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([singUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((promisesResults) => {
      const formatedStructure = [];
      for (const result of promisesResults) {
        if (result.status === 'rejected') {
          formatedStructure.push({
            status: result.status,
            value: `${result.reason.name}: ${result.reason.message}`,
          });
        } else {
          formatedStructure.push({
            status: result.status,
            value: result.value,
          });
        }
      }
      //  console.log(formatedStructure);
      return formatedStructure;
    })
    .catch((error) => error);
}
