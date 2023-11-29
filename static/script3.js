/*
Include these values !!!!!!!!!!!!!!!
"Date_time"
"Angle(Deg) "
"LVDT_1(Micron)"
let o={
    "abc $ 1": 4
}
o["abc $ 1"]// 4
*/
function displayData(data) {
    const container = document.getElementById('data-container');

    // Clear the container
    container.innerHTML = '';

    // Create the table element
    const table = document.createElement('table');

    // Create the table header row
    const tableHeader = document.createElement('thead');
    const headerRow = document.createElement('tr');
    const headers = ['Date_time','Angle(Deg)', 'LVDT_1(Micron)','LVDT_2(Micron)','LVDT_3(Micron)','LVDT_4(Micron)']; // Replace with your desired headers

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
        for(let i=0;i<item["LVDT_1(Micron)"].length;i++){
        const row = document.createElement('tr');
        
        // Create table cells for each property (name, description, price)
        console.log(item)
        console.log(typeof(item["Date_Time"]))
        console.log(item["Date_Time"])
         const date = document.createElement('td');
        date.textContent = item["Date_Time"][i];
        

        const angle = document.createElement('td');
        angle.textContent = item["Angle(Deg) "][i];

        const lvdt1 = document.createElement('td');
        lvdt1.textContent =  item["LVDT_1(Micron)"][i];
        
        const lvdt2 = document.createElement('td');
        lvdt2.textContent =  item["LVDT_2(Micron)"][i];

        const lvdt3 = document.createElement('td');
        lvdt3.textContent =  item["LVDT_3(Micron)"][i];

        const lvdt4 = document.createElement('td');
        lvdt4.textContent =  item["LVDT_4(Micron)"][i];

        // Append cells to the row
        row.appendChild(date);
        row.appendChild(angle);
        row.appendChild(lvdt1);
        row.appendChild(lvdt2);
        row.appendChild(lvdt3);
        row.appendChild(lvdt4);

       
        tableBody.appendChild(row);
    }
    });

    // Append the table body to the table
    table.appendChild(tableBody);

    // Append the table to the main container
    container.appendChild(table);

}

