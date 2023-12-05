$(function() {

    $(document).on('click', '#submit-login', function(){
        user = $('#user-login').val();
        senha =$('#senha-login').val();
        meuip = sessionStorage.getItem('meuip');

        var dados = JSON.stringify({userid : user, senha : senha});

    if (document.getElementById("mestre").checked){
        $.ajax({
            url: `http://${meuip}:5000/login_mestre`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: sucesso,
            error: anyError
        });
        function sucesso(retorno){
            if (retorno.resultado === 'sucesso'){
                window.alert('login realizado com sucesso');
                sessionStorage.setItem('user',user);
                window.location.assign('/render_mestre')
            } else{
                window.alert('usuário ou senha incorretos')
            }
        }
        function anyError(retorno){
            window.alert(`Login Incorreto. Verifique a senha,${retorno.Detalhes}`)
        }

    } else if (document.getElementById("jogador").checked){
        $.ajax({
            url: `http://${meuip}:5000/login_jogador`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: sucesso,
            error: anyError
        });
        function sucesso(retorno){
            if (retorno.resultado === 'sucesso'){
                window.alert('login realizado com sucesso');
                sessionStorage.setItem('user',user);
                window.location.assign('/render_menu')
            } else{
                window.alert('usuário ou senha incorretos')
            }
        }
        function anyError(retorno){
            window.alert(`Login Incorreto. Verifique a senha,${retorno.Detalhes}`)
        }

}})});