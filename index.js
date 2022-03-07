// POST API REQUEST
async function post_visitor() {
try {
    //let response = await fetch('https://t8olnedkte.execute-api.us-east-2.amazonaws.com/prod/resume-visitor-hit', {
    let response = await fetch('https://t8olnedkte.execute-api.us-east-2.amazonaws.com/prod/', {
        method: 'POST',
        headers: {
             //'x-api-key': ''
         }
     });
     let data = await response.json()
    //console.log(data);
    return data;
} catch (err) {
    console.error(err);
}
}

// GET API REQUEST
async function get_visitors() {
    // call post api request function
    //await post_visitor();
    try {
        let response = await fetch('https://t8olnedkte.execute-api.us-east-2.amazonaws.com/prod/', {
            method: 'GET',
            headers: {
                //'x-api-key': '',
            }
        });
        let data = await response.json()
        document.querySelector(".website-counter").innerHTML = data.count;
        console.log(data);
        return data;
    } catch (err) {
        console.error(err);
    }
}

get_visitors();