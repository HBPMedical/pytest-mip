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

/** Define a function to read a JUnit XML file and return the content in JSON format.
 * @param {string} url - The URL of the JUnit XML file
 * @returns {Array<{name, status}>} - The content of the JUnit XML file in JSON format
 */
async function parseJUnitXML(
  url = "https://hbpmedical.github.io/pytest-mip/report-03-04-2023-06-59/junit-report.xml"
) {
  const parser = new DOMParser();
  return fetch(url)
    .then((response) => response.text())
    .then((text) => {
      const xml = parser.parseFromString(text, "text/xml");
      const testsuite = xml.getElementsByTagName("testsuite")[0];
      const tests = testsuite.getElementsByTagName("testcase");
      const testsArray = Array.from(tests);
      const testsJSON = testsArray
        .map((test) => {
          const name = test.getAttribute("name");
          if (name.includes("test_data")) {
            const status =
              test.getElementsByTagName("failure").length > 0
                ? "failed"
                : "passed";
            for (const [key, value] of Object.entries(
              FEDERATION_URL_NAME_MAPPING
            )) {
              if (name.includes(key)) {
                return { name: value, status: status };
              }
            }
          }
        })
        .filter((test) => test !== undefined);
      console.log(testsJSON);
      return testsJSON;
    })
    .catch((error) => console.error(error));
}

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
      // Create the table header
      const tableHead = document.querySelector("#reportsTable thead");
      const headerRow = document.createElement("tr");
      // Append the date to the table head
      const dateHeader = document.createElement("th");
      dateHeader.innerHTML = "Date";
      dateHeader.setAttribute("onclick", "sortTableByDate()");
      headerRow.appendChild(dateHeader);
      // Append the link to the report to the table head
      const linkHeader = document.createElement("th");
      linkHeader.innerHTML = "Link";
      headerRow.appendChild(linkHeader);
      // Append the overall status to the table head
      const statusHeader = document.createElement("th");
      statusHeader.textContent = "Status";
      headerRow.appendChild(statusHeader);
      // Append the federation name to the table head
      for (const [key, value] of Object.entries(FEDERATION_URL_NAME_MAPPING)) {
        const federationHeader = document.createElement("th");
        federationHeader.innerHTML = value;
        headerRow.appendChild(federationHeader);
      }
      // Append the header row to the table head
      tableHead.appendChild(headerRow);

      // Create the table body
      const tableBody = document.querySelector("#reportsTable tbody");
      // Loop through the reports
      reports.reports.forEach(async (report) => {
        // Create a new row
        const row = document.createElement("tr");
        // Append the date
        const dateCell = document.createElement("td");
        dateCell.textContent = report.date;
        row.appendChild(dateCell);
        // Append the link to the report
        const linkCell = document.createElement("td");
        const link = document.createElement("a");
        link.textContent = report.link;
        link.href = report.link;
        link.target = "_blank";
        linkCell.appendChild(link);
        row.appendChild(linkCell);
        // Append the overall status
        const statusCell = document.createElement("td");
        if (report.status === "0") {
          statusCell.innerHTML = '<span style="color: green">&#10004;</span>';
        } else {
          statusCell.innerHTML = '<span style="color: red">&#9747;</span>';
        }
        row.appendChild(statusCell);
        // Parse the JUnit XML report file to show status of each federation
        const jUnitXMLReport = await Promise.resolve(
          parseJUnitXML(report.junitxml)
        );
        for (const [key, value] of Object.entries(
          FEDERATION_URL_NAME_MAPPING
        )) {
          const federationCell = document.createElement("td");
          const test = jUnitXMLReport.find((test) => test.name === value);
          if (test.status === "passed") {
            federationCell.innerHTML =
              '<span style="color: green">&#10004;</span>';
          } else {
            federationCell.innerHTML =
              '<span style="color: red">&#9747;</span>';
          }
          row.appendChild(federationCell);
        }
        // Append the row to the table body
        tableBody.appendChild(row);
      });
    })
    .catch((error) => console.error(error));
}
