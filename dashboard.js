// Fetch JSON data and render charts
fetch('dashboard_data.json')
  .then(response => response.json())
  .then(data => {
    // Specify the author to analyze
    const authorName = "Sydney Mike";
    const foodItemsData = data.author_food_items[authorName];

    if (foodItemsData) {
      new Chart(document.getElementById('authorFoodItemsPieChart'), {
        type: 'pie',
        data: {
          labels: Object.keys(foodItemsData),
          datasets: [{
            label: `Food Items by ${authorName}`,
            data: Object.values(foodItemsData),
            backgroundColor: [
              'rgba(255, 99, 132, 0.5)',
              'rgba(54, 162, 235, 0.5)',
              'rgba(255, 206, 86, 0.5)',
              'rgba(75, 192, 192, 0.5)',
              'rgba(153, 102, 255, 0.5)',
              'rgba(255, 159, 64, 0.5)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: `Food Items by ${authorName}`
            }
          }
        }
      });
    } else {
      console.error(`No data found for author: ${authorName}`);
    }
  })
  .catch(error => console.error('Error fetching dashboard data:', error));
