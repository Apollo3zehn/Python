let _connection
let _sensorSet
let _mode

$(document).ready(function() 
{
  let sensor

  _sensorSet = []
  _mode = 0

  // websockets
  _connection = Connect()

  // wind speed chart
  canvas = document.getElementById("wind-speed-bar-chart")
  sensor = CreateSensor("Wind speed", "m/s", canvas)
  _sensorSet.push(sensor)

  // wind direction chart
  canvas = document.getElementById("wind-direction-bar-chart")
  sensor = CreateSensor("Wind direction", "deg", canvas)
  _sensorSet.push(sensor)

  // ambient temperature chart
  canvas = document.getElementById("ambient-temperature-bar-chart")
  sensor = CreateSensor("Ambient temperature", "°C", canvas)
  _sensorSet.push(sensor)

  // ambient pressure chart
  canvas = document.getElementById("ambient-pressure-bar-chart")
  sensor = CreateSensor("Ambient pressure", "hPa", canvas)
  _sensorSet.push(sensor)
});

function UpdateChart(eventArgs)
{
  let message = JSON.parse(eventArgs.data)
  let sensor

  type = message.type

  switch(type)
  {
    case "stream":

      message.data.forEach((value, i) => 
      {
        data = { t: new Date(), y: value }
    
        sensor = _sensorSet[i]
        sensor.StreamData.push(data)
        
        if (sensor.StreamData.length > 120)
        {
          sensor.StreamData.shift()
        }
  
        if (_mode == 0)
        { 
          sensor.Chart.options.title.text = value + " " + sensor.Unit
          sensor.Chart.options.scales.xAxes[0].time.min = moment().subtract(1, 'm')
          sensor.Chart.update() 
        }
      });

      break;

    default:

      message.data.forEach((valueSet, i) => 
      {
        sensor = _sensorSet[i]
        sensor.OfflineData.length = 0

        newValueSet = valueSet.map((value, j) => { return { t: new Date(message.date_time[j]), y: value } })
        Array.prototype.push.apply(sensor.OfflineData, newValueSet)

        sensor.Chart.update() 
      });

      break;
  }
}

function ToggleMode()
{
  _mode = (_mode + 1) % 3

  if (_mode == 0)
  {
    _sensorSet.forEach(sensor => 
    {
      sensor.Chart.data.datasets[0].data = sensor.StreamData
      sensor.Chart.options.scales.xAxes[0].time.unit = "second"
      sensor.Chart.options.animation.duration = 1500
    })
  }
  else if (_mode == 1)
  {
    _connection.send("Get10Minutes");

    _sensorSet.forEach(sensor => 
    {
      sensor.Chart.data.datasets[0].data = sensor.OfflineData
      sensor.Chart.options.title.text = "last 10 minutes"
      sensor.Chart.options.scales.xAxes[0].time.unit = "minute"
      sensor.Chart.options.scales.xAxes[0].time.min = moment().subtract(10, 'm')
      sensor.Chart.options.animation.duration = 0
    })
  }
  else if (_mode == 2)
  {
    _connection.send("Get60Minutes");

    _sensorSet.forEach(sensor => 
    {
      sensor.Chart.data.datasets[0].data = sensor.OfflineData
      sensor.Chart.options.title.text = "last 60 minutes"
      sensor.Chart.options.scales.xAxes[0].time.unit = "minute"
      sensor.Chart.options.scales.xAxes[0].time.min = moment().subtract(1, 'h')
      sensor.Chart.options.animation.duration = 0
    })
  }
}

function CreateSensor(displayName, unit, canvas)
{
  sensor = []
  sensor.DisplayName = displayName
  sensor.Unit = unit
  sensor.Canvas = canvas
  sensor.StreamData = []
  sensor.OfflineData = []
  sensor.Chart = CreateBarChart(sensor)

  return sensor
}

function Connect()
{
  let connection

  if (window.WebSocket) 
  {
    connection = new WebSocket("ws://" + location.hostname + ":9001/");

    connection.onopen = () => console.log("Websockets connection opened.")

    connection.onclose = async () => 
    {
      console.log("Websockets connection closed.")
      await Sleep(2)
      console.log("Trying to reconnect ...")
      _connection = Connect()
    }
  
    connection.onmessage = (eventArgs) => UpdateChart(eventArgs)

    return connection
  }
  else 
  {
    console.log('WebSockets are not supported.');
    return null;
  }
}

function Sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function CreateBarChart(sensor)
{
  return new Chart(sensor.Canvas,
  {
    type: "line",
    data: {
      // labels: labels,
      datasets: [{
        data: sensor.StreamData,
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235)",
        borderWidth: 1,
        lineTension: 0.25,
        pointRadius: 0
      }]
    },
    options: {
      animation: {
        duration: 1500,
        easing: "linear"
      },
      legend: {
        display: false
      },
      maintainAspectRatio: false,
      responsive: true,
      scales: {
        xAxes: [{
          type: 'time',
          time: {
            unit: "second",
            displayFormats: {
              second: 'HH:mm:ss',
              minute: 'HH:mm',
            }
          }
        }],
        yAxes: [{
          type: "linear",
          position: "left",
          scaleLabel: {
            display: true,
            labelString: sensor.Unit
          },
          ticks: {
            beginAtZero: true
          }
        }]
      },
      title: {
        display: true,
        text: ""
      },
      tooltips: {
        enabled: false
      }
    }
  })
}

