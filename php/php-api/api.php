<?php
header("Content-Type: application/json");

require "config.php";

$sql = "SELECT * FROM usuarios";
$result = $conn->query($sql);

$datos = [];

while($row = $result->fetch_assoc()){
    $datos[] = $row;
}

echo json_encode($datos);