const ctx = document.getElementById('myChart').getContext('2d');


const graph = {
    type: 'line',
    data: {
        labels : [],
        datasets: [{
            label: "Temperature",
            data : [],
            backgroundColor: 'rgba(192, 75, 192, 0.2)',
            borderColor: 'rgba(192, 75, 192, 1)',
            borderWidth: 1
        },{
            label: "Humidity",
            data : [],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {}
};

const myChart = new Chart(ctx, graph)




var socket = new WebSocket('ws://192.168.1.169:8000/ws/iot/');

socket.onmessage = function(e){
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);
    var temp = [];
    var hum = [];
    var dates = [];
    for (let i = 0; i < djangoData.length; i++){
        temp.push(djangoData[i].temp_value);
        hum.push(djangoData[i].hum_value);
        dates.push(djangoData[i].pub_date);
    }

    graph.data.datasets[0].data = temp;
    graph.data.datasets[1].data = hum;
    graph.data.labels = dates;

    myChart.update();
}
