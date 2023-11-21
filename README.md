## MathOCR
Modelo de reconhecimento de caracteres matemáticos manuscritos, através de uma Rede Neural Convolucional (CNN). Criado a fim de ser utilizado no projeto de um Tutor Inteligente, à ser utilizado na área da educação. <br><br>

<h2>Treinar</h2>
Para utilizar o código acima e realizar o treino do modelo, siga essas etapas:
<br><br>
1) Acesse o link fornecido abaixo para fazer o download do dataset.<br>
2) Descompacte o dataset<br>
3) Altere o diretório para o dataset no código do arquivo "data_loader.py"<br>
4) Abra o terminal<br>
5) No windows: digite "python main.py"<br>
   No linux: digite "python3 main.py"<br>


<h2>Testar</h2>
1) Baixe o modelo pré-treinado no link fornecido abaixo.<br>
2) Altere o caminho em "teste.py" para o diretório do modelo baixado.<br>
3) Altere o caminho em "teste.py" para a imagem que deseja testar.<br>
4) Abra o terminal.<br>
5) No windows, digite: "python teste.py"

<h2>Dataset e Modelo pré-treinado</h2>
Link para o drive: https://drive.google.com/drive/folders/1NCkfvu4bruAAUm7MHWEfmmp5TPcANPF_?usp=sharing

<h2>Especificações</h2>
- Necessário Python 3 ou superior e tensorflow 2.14<br>
- Memória ram mínima: 8 GB<br>
- Caracteres reconhecidos: (, ), +, 0, 2, 3, 4, 5, 6, 7, 8, 9, a, α, b, β, cos, d, δ, /, e, f, γ, g, >, h, i, ∈, ∞, ∫, k, <=, lim, log, <, m, n, >=, o, p, Φ, π, +/-, q, r, s, σ, sin, √, ∑, tan, t, θ, *, u, v, w, x, y, z, {, }.
