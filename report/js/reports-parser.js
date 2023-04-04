/**
 * @file
 * This file contains the JavaScript code to parse the reports.json and the
 * individual JUnit XML report files to render the reports table.
 * @author Sébastien Tourbier
 * @license Apache-2.0
 */

/* Define mapping between MIP federation URL and Name displayed in the report table.*/
const FEDERATION_URL_NAME_MAPPING = {
  "test_data[https://hbpmip.link/]": "Public",
  "test_data[https://qa.hbpmip.link/]": "QA",
};

        })
        .catch(error => console.error(error));
/** Define a function to fetch the JSON data and populate the table
 * @param {string} url - The URL of the main reports.json file listing all the reports
 * @returns {void}
 */
function parseJSONReports(
  url = "https://hbpmedical.github.io/pytest-mip/reports.json"
) {
  fetch(url)
    .then((reports) => reports.json())
    .then((reports) => {
      const tableBody = document.querySelector("#reportsTable tbody");

      reports.reports.forEach((report) => {
        const row = document.createElement("tr");

        const dateCell = document.createElement("td");
        dateCell.textContent = report.date;
        row.appendChild(dateCell);

        const linkCell = document.createElement("td");
        const link = document.createElement("a");
        link.textContent = report.link;
        link.href = report.link;
        link.target = "_blank";
        linkCell.appendChild(link);
        row.appendChild(linkCell);

        const statusCell = document.createElement("td");
        if (report.status === "0") {
          statusCell.innerHTML = '<span style="color: green">&#10004;</span>';
        } else {
          statusCell.innerHTML = '<span style="color: red">&#9747;</span>';
        }
        row.appendChild(statusCell);

        tableBody.appendChild(row);
      });
    })
    .catch((error) => console.error(error));
}
