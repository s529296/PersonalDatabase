// Onclick of the button
document.querySelector("button").onclick = function () {  
  // Call python's random_python function
  eel.random_python()(function(number){
    // Update the div with a random number returned by python
    document.querySelector(".random_number").innerHTML = number;
  })
}
function myCreateFunction() {
  var table = document.getElementById("myTable");
  var row = table.insertRow(0);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  cell1.innerHTML = "NEW CELL1";
  cell2.innerHTML = "NEW CELL2";
}