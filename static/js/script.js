$("#add-category").click(function(){
    $("#category").append(" <div class='col s5'> <input type='text' id='nameCategory' name='nameCategory' placeholder='Nome da Categoria'>" +    
    '</div>'+
    '<div class="col s2">'+
        '<input type="text" id="originalValue" name="originalValue" placeholder="Valor Original">'+
    '</div>'+
    '<div class="col s1">'+
        "<img src='static/img/icons8-chevron-right-64.png'>"+
    '</div>'+
    '<div class="col s2">'+
        '<input type="text" id="patternValue" name="patternValue" placeholder="Valor Padronizado">'+
    '</div>'+
    '<div class="col s2">'+
    "</div>");
  });