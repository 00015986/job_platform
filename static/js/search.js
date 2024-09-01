document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        let nameFilter = document.getElementById('filterByName').value.toLowerCase();
        let selectedLocation = document.getElementById('selectLocation').value.toLowerCase();
        let selectedJobType = document.getElementById('chooseJobType').value.toLowerCase();
        let selectedIndustry = document.getElementById('selectIndustry').value.toLowerCase();

        let jobs = document.querySelectorAll('.job-card'); // Assuming each job is inside a div with class 'job-card'

        jobs.forEach(function(job) {
            let title = job.querySelector('.card-title').textContent.toLowerCase();
            let location = job.querySelector('.job-location').textContent.toLowerCase();
            let jobType = job.querySelector('.job-type').textContent.toLowerCase();
            let industry = job.querySelector('.job-industry').textContent.toLowerCase();

            if (
                (nameFilter === '' || title.includes(nameFilter)) &&
                (selectedLocation === '' || location.includes(selectedLocation)) &&
                (selectedJobType === '' || jobType.includes(selectedJobType)) &&
                (selectedIndustry === '' || industry.includes(selectedIndustry))
            ) {
                job.style.display = 'block';
            } else {
                job.style.display = 'none';
            }
        });
    });
});
