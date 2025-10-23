<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>outubro rosinha</title>
    <style>
        body{
            background-color: #ffe6f0;
            text-align: center;
            ;
        }
        </style>
</head>
<body>
    <h2>Formulário Outubro Rosa </h2>
    <form action="index.php" method="post">
        <label>Nome:</label><br>
        <input type="text" name="nome" required><br><br>
        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>
        <label>Idade:</label><br>
        <input type="number" name="idade" required><br><br>
        <label>Já realizou o exame de mamografia?</label><br>
        <input type="radio" name="mamografia" value="sim" required> Sim<br>
        <input type="radio" name="mamografia" value="não" required> Não<br><br>
        <input type="submit" value="Enviar">
    </form>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $idade = $_POST["idade"];
    $mamografia = $_POST["mamografia"];

    echo "<h3>Dados recebidos (POST)</h3>";
    echo "Nome:  $nome<br>";
    echo "Email:  $email<br>";
    echo "Idade:  $idade<br>";
    echo "Mamografia:  $mamografia<br>";
}
?>

</body>
</html>