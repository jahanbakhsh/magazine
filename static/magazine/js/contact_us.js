
$("#form-submit").click(function validate_form(evt) {
    var name = $("#form-name").val();
    var email = $("#form-email").val();
    var message = $("#form-message").val();
    var send = true
    $("#form-name + p").remove();
    $("#form-email + p").remove();
    $("#form-message + p").remove();
    if(name.length<5){
        $("#form-name").after("<p class='error'>نام باید دارای طول بیشتر از ۴ باشد.</p>");
        send=false
    }
    if(email.length<5){
        $("#form-email").after("<p class='error'>نام باید دارای طول بیشتر از ۴ باشد.</p>");
        send =false
    }
    console.log(send)
    if (send){
        data={
            'name':name,
            'email':email,
            'message':message
        }
        $.ajax({
        type: "POST",
        url: "message",
        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(data),
        dataType: "json",
        success: function(data){
            $("#form-message").after("<p class='error'>پیام شما با موفقیت ارسال شد.</p>");
            console.log('success')
        },
        failure: function(errMsg) {
            $("#form-message").after("<p class='error'>در ارسال پیام شما خطایی رخ داده است لطفا مجدد تلاش فرمایید</p>");
            console.log('error')
        }
    });
    }
})