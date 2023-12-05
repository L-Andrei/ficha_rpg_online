$(function (){
    $(document).on('click', '#submit_personagem', function(){
        meuip = sessionStorage.getItem('meuip');
        user = sessionStorage.getItem('user');
        dano_sofrido = $('#dano_sofrido').val();
        cura = $('#cura').val();
        dano_mental = $('#dano_mental').val();
        san_regen = $('#san_regen').val();
        pe_gasto = $('#pe_gasto').val();
        pe_ganho = $('#pe_ganho').val();

    var log = JSON.stringify({id:user,dano_sofrido:dano_sofrido,dano_mental:dano_mental,cura:cura,san_regen:san_regen,pe_ganho:pe_ganho,pe_gasto:pe_gasto});

    $.ajax({
        url:`http://${meuip}:5000/update_personagem/simples`,
        type:'PUT',
        dataType:'json',
        contentType: 'application/json',
        data: log,
        success: sucesso,
        error: anyerror
    })
    function sucesso(retorno){
        if(retorno.resultado === 'sucesso'){
            window.alert('Alteração feita');
            window.location.assign('/render_personagem');
        }
    }
    function anyerror(retorno){
        window.alert(retorno.detalhes);
    }
})})
