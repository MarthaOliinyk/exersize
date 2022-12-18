import axios from "axios";
const fetchPayment=id=>{
    axios.post('http://127.0.0.1:8080/create/payment', {
    subscription_type_id:id
  },{withCredentials: true})
  .then(function (response) {
    console.log(response);
  }
  .catch(function (error) {
    console.log(error.toJSON());
  }))
}
export default fetchPayment