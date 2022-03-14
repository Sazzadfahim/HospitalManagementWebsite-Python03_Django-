var selectedRow = null


function onFormSubmit() {

    var formData = readFormData();
    insertNewRecord(formData);
    
}




function readFormData() {
    var formData = {};
    formData["hospitsl_name"] = document.getElementById("hospitsl_name").value;
    formData["booking_type"] = document.getElementById("booking_type").value;
    formData["name"] = document.getElementById("name").value;
    formData["email"] = document.getElementById("email").value;
    formData["phone"] = document.getElementById("phone").value;
    return formData;
}


function insertNewRecord(data) {
    var table = document.getElementById("employeeList").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.hospitsl_name;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.booking_type;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.name;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.email;

    cell4 = newRow.insertCell(4);
    cell4.innerHTML = data.phone;
    

    cell4 = newRow.insertCell(5);
    cell4.innerHTML = `<a onClick="onEdit(this)">Edit</a>
                       <a onClick="onDelete(this)">Delete</a>`;
    cell4 = newRow.insertCell(6);
    cell4.innerHTML = "3 hours";

    cell4 = newRow.insertCell(7);
    cell4.innerHTML = "1,500";

    
}