fetch('http://127.0.0.1:8000/api/mymodels/')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Data:', data);
        // Process the fetched data here
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
