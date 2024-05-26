<?php
$data = file_get_contents("data.json");
$datos = json_decode($data, true);

$regionesSeleccionadas = $_POST['regiones'];

$datosFiltrados = [];
foreach ($datos['regiones'] as $region) {
    if (in_array($region['nombre'], $regionesSeleccionadas)) {
        $datosFiltrados[] = $region;
    }
}

echo json_encode($datosFiltrados);
?>
