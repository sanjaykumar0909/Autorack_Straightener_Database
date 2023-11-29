window.onload=function(){
    var mb = document.getElementById("myForm");
    mb.addEventListener("submit",formclick);
}

function formclick(e){
    e.preventDefault();
    // displayData(data);
    let formElem= document.getElementById("myForm")
    let formdata = new FormData(formElem)
    console.log(formdata);
    fetch("/fetch-components/", {
        method: "POST",
        body: formdata
    })
    .then(response => response.json())
    .then((data)=>{
        console.log(data)
        console.log("-------------------------------------")
        displayData(data);
    })
    
}

index1="index1.html"
function displayData(data) {
    const container = document.getElementById('data-container');

    // Clear the #
    container.innerHTML = '';

    // Create the table element
    const table = document.createElement('table');

    // Create the table header row
    const tableHeader = document.createElement('thead');
    const headerRow = document.createElement('tr');
    const headers = ['Rod Id','Start Time', 'End Time']; // Replace with your desired headers

    headers.forEach(headerText => {
        const headerCell = document.createElement('th');
        headerCell.textContent = headerText;
        headerRow.appendChild(headerCell);
    });

    tableHeader.appendChild(headerRow);
    table.appendChild(tableHeader);

    // Create the table body
    const tableBody = document.createElement('tbody');

    // Iterate through the data and create table rows
    data.forEach(item => {
        const row = document.createElement('tr');

        // Create table cells for each property (name, description, price)
         const idnum = document.createElement('td');
        idnum.textContent = item.component_serial_num;

        const starttime = document.createElement('td');
        starttime.textContent = item.start_time;
        console.log(item.start_time)

        const endtime = document.createElement('td');
        endtime.textContent =  item.end_time;

        // Append cells to the row
        row.appendChild(idnum);
        row.appendChild(starttime);
        row.appendChild(endtime);

        // Append the row to the table body
        tableBody.appendChild(row);

        row.addEventListener('click', () => {
            window.location.href = `/backend-url/?id=${item.component_serial_num}`;
        });

    });

    // Append the table body to the table
    table.appendChild(tableBody);

    // Append the table to the main container
    container.appendChild(table);
}

// function sendDataToBackend(itemId) {
//     let formdata = new FormData();
//     formdata.append('id',itemId);
//     fetch('/backend-url/', {
//         method: 'POST',
//         body:formdata
//     })
//     .then(response => {
//         if (response.ok) {
//             console.log('Data sent to backend successfully.');
//         } else {
//             console.error('Error sending data to backend.');
//         }
//     })
//     .catch(error => {
//         console.error('Error sending data to backend:', error);
//     });

// }
