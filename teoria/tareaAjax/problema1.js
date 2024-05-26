$(document).ready(function(){
    $.getJSON("data.json", function(data){
        $.each(data.regiones, function(index, region){
            $("#regiones").append(`<option value="${region.nombre}">${region.nombre}</option>`);
        });
    });

    $("#regiones").change(function(){
        var regionesSeleccionadas = $(this).val();
        $.ajax({
            url: "obtener_datos.php", 
            method: "POST",
            data: {regiones: regionesSeleccionadas},
            success: function(response){
                var datos = JSON.parse(response);
                dibujarGrafico(datos);
            }
        });
    });
});

function dibujarGrafico(datos){
    var etiquetas = [];
    var casos = [];
    datos.forEach(function(region){
        etiquetas.push(region.nombre);
        casos.push(region.casos);
    });

    var ctx = document.getElementById('grafico').getContext('2d');
    var grafico = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: etiquetas,
            datasets: [{
                label: 'Casos Confirmados',
                data: casos,
                backgroundColor: 'rgba(54, 162, 235, 0.5)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}
