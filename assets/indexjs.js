function displayData(data) {
    const container = document.getElementById('data-container');

    // Clear the container
    container.innerHTML = '';

    // Iterate through the data and create HTML elements
    data.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = item.name; // Replace with your JSON structure

        container.appendChild(listItem);
    });
}
document.addEventListener("DOMContentLoaded", function(){
    let form = document.getElementById("formid")
    form.addEventListener("submit", (e)=>{
        e.preventDefault()

        let formData= new FormData(form)

        fetch("/another-page/", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then((data) =>{
            displayData(data)
        })
        .catch(err=>{console.error("Error:",err)})
    })
})