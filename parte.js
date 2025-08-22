function verificarpalavra() {
  const usuarios = [
    {id: "lia", senha: "1327"},
    {id: "rafa", senha: "1456"},
    {id: "matheus", senha: "1789"}
  ];

  const inputId = document.getElementById("palavra").value.trim();
  const inputSenha = document.getElementById("senha").value.trim();
  const mensagem = document.getElementById("mensagem");

  let encontrado = false;

  for (let i = 0; i < usuarios.length; i++) {
    if (inputId === usuarios[i].id && inputSenha === usuarios[i].senha) {
      encontrado = true;
      break;
    }
  }

  if (encontrado) {
    mensagem.innerHTML = "Cadastro correto!";

  } else {
    mensagem.innerHTML = "Erro de digitação, tente novamente.";

  }
}