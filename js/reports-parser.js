/*
 * JS for parsing our reports.json to render the reports table.
 *
*/

/* Define a function to fetch the JSON data and populate the table */
function parseJSONReports(url = 'https://hbpmedical.github.io/pytest-mip/reports.json') {
    fetch(url)
        .then(reports => reports.json())
        .then(reports => {
            const tableBody = document.querySelector('#reportsTable tbody');

            reports.reports.forEach(report => {
                const row = document.createElement('tr');

                const dateCell = document.createElement('td');
                dateCell.textContent = report.date;
                row.appendChild(dateCell);

                const linkCell = document.createElement('td');
                const link = document.createElement('a');
                link.textContent = report.link;
                link.href = report.link;
                link.target = '_blank';
                linkCell.appendChild(link);
                row.appendChild(linkCell);

                const statusCell = document.createElement('td');
                if (report.status === '0'){
                    statusCell.innerHTML = '<span style="color: green">&#10004;</span>';
                }
                else{
                    statusCell.innerHTML = '<span style="color: red">&#9747;</span>';
                }
                row.appendChild(statusCell);

                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error(error));
}
