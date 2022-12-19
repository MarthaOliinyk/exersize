import axios from "axios";

const fetchPayment = id => {
    axios.post('http://localhost:8080/create/payment', {
        subscription_type_id: id
    }, {withCredentials: true})
        .then(res => {
                let url = res.data['payment_url'];
                window.location = url;
            }
        )
}
export default fetchPayment
