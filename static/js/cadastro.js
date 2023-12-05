$(function() {

    $(document).on('click', '#submit-cadastro', function(){
        user = $('#user-cadastro').val();
        senha =$('#senha-cadastro').val();
        meuip = sessionStorage.getItem('meuip');

        var dados = JSON.stringify({userid : user, senha : senha});

    if (document.getElementById("mestre").checked){
        $.ajax({
            url: `http://${meuip}:5000/cadastrar_mestre`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: sucesso,
            error: anyError
        });
        function sucesso(retorno){
            if (retorno.resultado === 'sucesso'){
                window.alert('Cadastro realizado com sucesso!');
                sessionStorage.setItem('user',user);
                window.location.assign('/render_mestre')
            }
        }
        function anyError(retorno){
            window.alert(`cadastro Incorreto. Verifique a senha,${retorno.detalhes}`)
        }

    } else if (document.getElementById("jogador").checked){
        $.ajax({
            url: `http://${meuip}:5000/cadastrar_jogador`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: sucesso,
            error: anyError
        });
        function sucesso(retorno){
            if (retorno.resultado === 'sucesso'){
                window.alert('Cadastro realizado com sucesso');
                sessionStorage.setItem('user',user);
                window.location.assign('/render_menu');
            }}
        function anyError(retorno){
            window.alert(`cadastro Incorreto. Verifique a senha,${retorno.detalhes}`)
        }

}})});