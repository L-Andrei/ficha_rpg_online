$(function (){
    $(document).on('click', '#submit_personagem', function(){
        meuip = sessionStorage.getItem('meuip')
        jogador = sessionStorage.getItem('user')
        mestre = $('#mestre').val();
        nome = $('#nome').val();
        nex = $('#nex').val();
        vida = $('#vida').val();
        san = $('#san').val();
        pe = $('#pe').val();
        forca = $('#forca').val();
        agi = $("#agi").val();
        int = $("#int").val();
        vig = $("#vig").val();
        pre = $("#pre").val();

        var log = JSON.stringify({mestreid:mestre,jogadorid:jogador,nome_do_personagem:nome,nex:nex,vd_max:vida,vd_atual:vida,san_atual:san,san_max:san,
        pe_atual:pe,pe_max:pe,forca:forca,agi:agi,int:int,vig:vig,pre:pre});

    $.ajax({
            url: `http://${meuip}:5000/criar_personagem`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: log,
            success: sucesso,
            error: anyError
    })
    function sucesso(retorno){
        if(retorno.resultado==='sucesso'){
            window.alert('Personagem criado com sucesso!')
            sessionStorage.setItem('personagem',retorno.detalhes)
            window.location.assign('/render_personagem')
        }
    }
    function anyError(retorno){
        window.alert(`${retorno.detalhes}`)
    }
})})