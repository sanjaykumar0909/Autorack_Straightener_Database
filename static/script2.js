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
    fetch("/fetch-csv-file/", {
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
    const headers = ['Serial number','Creation Time','X-distance','Servo Angle','Max Deflection']; // Replace with your desired headers

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
        idnum.textContent = item.csv_file_serial_num;

        const creationTime = document.createElement('td');
        creationTime.textContent = item.creation_time;

        const x_dist = document.createElement('td');
        x_dist.textContent =  item.x_distance;
        
        const servo= document.createElement('td');
        servo.textContent =  item.servo_angle;

        const max_def= document.createElement('td');
        max_def.textContent =  item.max_deflection;
        // Append cells to the row
        row.appendChild(idnum);
        row.appendChild(creationTime);
        row.appendChild(x_dist);
        row.appendChild(servo);
        row.appendChild(max_def);

        // Append the row to the table body
        tableBody.appendChild(row);

        row.addEventListener('click', () => {
            window.location.href = `/file-data-page/?id=${item.csv_file_serial_num}`;
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
