$(function (){
    $(document).on('click', '#submit_personagem', function(){
        meuip = sessionStorage.getItem('meuip')
        personagem = sessionStorage.getItem('personagem')
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

    var log = JSON.stringify({id:personagem,nome:nome,nex:nex,vd_max:vida,san_max:san,
    pe_max:pe,forca:forca,agi:agi,int:int,vig:vig,pre:pre});

    $.ajax({
            url: `http://${meuip}:5000/update_personagem/complexo`,
            type: 'PUT',
            dataType: 'json',
            contentType: 'application/json',
            data: log,
            success: sucesso,
            error: anyError
    })
    function sucesso(retorno){
        if(retorno.resultado==='sucesso'){
            window.alert('Personagem alterado com sucesso!');
            window.location.assign('/render_menu');
        }
    }
    function anyError(retorno){
        window.alert(`cadastro Incorreto. Verifique a senha,${retorno.detalhes}`)
    }
})})