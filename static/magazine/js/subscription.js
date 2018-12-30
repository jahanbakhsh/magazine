
var modal = document.getElementById('roleModal');


var btn = document.getElementById("btn-role");


var span = document.getElementsByClassName("close")[0];


btn.click(function() {
  modal.style.display = "block";
});

span.click(function() {
  modal.style.display = "none";
});

$("#btn-role").click(function (evy) {
    if($(this).is(':checked')){
        $("#btn-submit").addClass('active').removeClass('disabled');
    }
})