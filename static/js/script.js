//Dropdown in menu using Materialize JS

  $(document).ready(function(){
    $(".dropdown-trigger").dropdown({hover:false});
  });


//Add and remove new category in box 'text two'

//Total máximo de campos que você permitirá criar em seu site:
var totalCampos = 100;

//Variaveis de controle
var iLoop = 1;
var iCount = 0;
var linhaAtual;

function AddCampos() {    
    var hidden1 = document.getElementById("hidden1");
    var hidden2 = document.getElementById("hidden2");

    //Executar apenas se houver possibilidade de inserção de novos campos:
    if (iCount < totalCampos) {
        //Limpar hidden1, para atualizar a lista dos campos que ainda estão vazios:
        hidden2.value = "";

        //Atualizando a lista dos campos que estão ocultos.
        //Essa lista ficará armazenada temporiariamente em hidden2;
        for (iLoop = 1; iLoop <= totalCampos; iLoop++) {
            if (document.getElementById("linha"+iLoop).style.display == "none") {
                    if (hidden2.value == "") {
                            hidden2.value = "linha"+iLoop;
                    }else{
                            hidden2.value += ",linha"+iLoop;
                    }
            }
        }
        //Quebrando a lista que foi armazenada em hidden2 em array:
        linhasOcultas = hidden2.value.split(",");
        if (linhasOcultas.length > 0) {
            //Tornar visível o primeiro elemento de linhasOcultas:
            document.getElementById(linhasOcultas[0]).style.display = "block"; iCount++;
            
            //Acrescentando o índice zero a hidden1:
            if (hidden1.value == "") {
                    hidden1.value = linhasOcultas[0];
            }else{
                    hidden1.value += ","+linhasOcultas[0];
            }
            
        }
    }
}

function RemoverCampos(id) {
    //Criando ponteiro para hidden1:        
    var hidden1 = document.getElementById("hidden1");
    //Pegar o valor do campo que será excluído:
    var campoValor = document.getElementById("nameCategory"+id).value;
    //Se o campo não tiver nenhum valor, atribuir a string: vazio:
    if (campoValor == "") {
            campoValor = "vazio";
    }

    if(confirm("O campo que contém o valor:\n» "+campoValor+"\nserá excluído!\n\nDeseja prosseguir?")){
            document.getElementById("linha"+id).style.display = "none"; iCount--;
            
            //Removendo o valor de hidden1:
            if (hidden1.value.indexOf(",linha"+id) != -1) {
                    hidden1.value = hidden1.value.replace(",linha"+id,"");
            }else if (hidden1.value.indexOf("linha"+id+",") == 0) {
                    hidden1.value = hidden1.value.replace("linha"+id+",","");
            }else{
                    hidden1.value = "";
            }
    }
} 

//Incluindo o box somente para o tipo Byte

function selected(value){
    var categorias = document.getElementById('boxCategorys');
        if(value == "Byte"){
            categorias.style.display = 'block';
        }else{
            categorias.style.display = 'none';
    }
}

//Desabilitar os buttons add e compile caso o type esteja null
function type_disabled(){
        var tipo = document.getElementById('type');
        var name = document.getElementById('nameVariable');
        if(tipo == 'Type' || name == null || name == ""){
                if(!document.getElementById('add').disabled) document.getElementById('add').disabled=true;
                if(!document.getElementById('compile').disabled) document.getElementById('compile').disabled=true;
        }else{
                if(document.getElementById('add').disabled) document.getElementById('add').disabled=false;
                if(document.getElementById('compile').disabled) document.getElementById('compile').disabled=false;
        }
}

//Abilitar botão submit
function submit_show(){
       if (document.getElementById('add').disabled){
                document.getElementById('submit').disabled=true;
       }else{
                document.getElementById('submit').disabled=false;
       }

}


//Criação do modal de alerta para o delete!
$(document).ready(function(){
        $('.modal').modal();
});
              





 