window.onload=function(){
    var mb = document.getElementById("formid");
    mb.addEventListener("submit", formclick);
}
 function formclick(e) {
    e.preventDefault(); // Prevent the default form submission

    // Create an object to hold form data
    const formData = {
       forminput:document.getElementById("fname"),


        // Add more fields as needed
    };
    console.log(formData)
    // Send the data as JSON to the backend
    fetch('another-page/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', // Specify that you are sending JSON data
        },
        body: JSON.stringify(formData), // Convert the data to a JSON string
    })
    .then(response => response.json())
    .then((data)=>{
        var resultPage = document.createElement('div');
                resultPage.innerHTML = '<h2>Result</h2><p>' + data.result + '</p>';
                document.body.appendChild(resultPage);
    })
    .catch(error => {
        console.log('Error name:', error);
    });
}