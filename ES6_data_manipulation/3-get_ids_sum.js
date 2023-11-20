export default function getStudentIdsSum(arrayOfObjs) {
  return arrayOfObjs.reduce((accumulator, arrayOfObjs) => accumulator + arrayOfObjs.id, 0);
}
