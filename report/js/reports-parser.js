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
function parseJUnitXML(
  url = "https://hbpmedical.github.io/pytest-mip/report-03-04-2023-06-59/junit-report.xml"
) {
  const parser = new DOMParser();
  fetch(url)
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
            return { name, status };
          }
        })
        .filter((test) => test !== undefined);
      console.log(testsJSON);
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
