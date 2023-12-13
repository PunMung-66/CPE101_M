const axios = require('axios');

// Replace 'http://your-api-url' with the actual URL of your FastAPI application
const apiUrl = 'https://punnawat01-cpe101-fast-api.hf.space';
const name = 'Pun_o_o';
// Example data for testing
const loginData = {
    name: 'Ben',
    bank_u: 'Genshin',
    bank_p: 'Primogem',
};

const pocketData = {
    Pocket: 'TestPocket',
    Amount: 100,
};

// Testing the login endpoint
// axios.post(`${apiUrl}/login`, loginData).then(response => {
//     console.log('Login Result:', response.data.result);
// }).catch(error => console.error('Login Error:', error));
    
// Testing add_pocket endpoint
// axios.post(`${apiUrl}/add_pocket/${name}`, pocketData)
// .then(pocketResponse => {console.log('Add Pocket Result:', pocketResponse.data.result);}).catch(error => console.error('Add Pocket Error:', error));
    