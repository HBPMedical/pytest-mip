/**
 * @file
 * JS for enabling table sorting by column in the reports table.
 * @author Sébastien Tourbier
 * @license Apache-2.0
 */

/** 
 * Parse a string in the format DD-MM-YYYY HH:MM and return a Date object.
 * @param {string} str - Date/Time string in the format DD-MM-YYYY HH:MM
 * @returns {Date} - a Date object
 */
function getDate(str) {
    // Parse date and time
    var ar =  /(\d{2})-(\d{2})-(\d{4}) (\d{2}):(\d{2})/.exec( str )
    // Return the Date object initialized with parsed date and time
    return new Date(
        (+ar[3]),
        (+ar[2])-1, // Careful, month starts at 0!
        (+ar[1]),
        (+ar[4]),
        (+ar[5]),
        0
    );
}

/** 
 * Sort the reports table by ordering the Date column.
 * @param {string} dir - string specifying the sort order ("asc" for ascending or "desc" for descending)
 * @returns {void}
 */
function sortTableByDate(dir = "asc") {
  // Get the reports table
  var table = document.getElementById("reportsTable");
  // Get the table body
  var tBody = table.getElementsByTagName('tbody')[0];
  // Get the rows of the table body
  var rows = tBody.getElementsByTagName('tr');
  // Initialize variables to switch ascending/descending order
  var switching = true;
  var switchcount = 0;
  while (switching) {
    switching = false;
    for (var i = 0; i < (rows.length - 1); i++) {
      var shouldSwitch = false;
      // Extract the dates of two report rows
      var date1 = getDate(rows[i].cells[0].innerHTML.trim());
      var date2 = getDate(rows[i + 1].cells[0].innerHTML.trim());
      // Check if the two rows should switch place,
      // based on the direction, asc or desc
      if (dir == "asc") {
        if (date1 > date2) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (date1 < date2) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount++;
    } else {
      // If no switching has been done AND the direction is "asc",
      // set the direction to "desc" and run the while loop again
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
