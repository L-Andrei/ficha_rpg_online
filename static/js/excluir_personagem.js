$(document).ready(function() {
    $('#form-excluir').submit(function() {
        var nomePersonagem = $('#nome').val();
        meuip = sessionStorage.getItem('meuip');

        dados=JSON.stringify({nome:nomePersonagem});

        $.ajax({
            type: 'POST', 
            url: `http://${meuip}:5000//excluir_personagem`,
            data: dados,
            dataType: 'json',
            contentType: 'application/json',
            success: sucesso,
            error: anyError
        });
            function sucesso(resposta) {
                if(resposta.retorno == 'sucesso'){
                alert('Personagem excluído com sucesso!');
                }
            };
            function anyError(error) {
                alert('Erro ao excluir personagem:', error);
            }
        });

        return false;
    });